def test(model, validation_loader):
    n_samples = len(validation_loader)
    # mcc_single_multi, threshold = model.mcc_history[-1]
    best_score, threshold, _ = get_best_mcc(model, casp_loader)
    scores = {}
    all_y_pred, all_y_true = None, None
    print("Starting Testing")
    model.eval()
    with torch.no_grad():
        for i, (input, y_true, _, key, seq_len) in enumerate(validation_loader):
            input = input.float().to(device)
            y_pred = model(input)

            y_pred = y_pred.cpu()
            y_true = y_true.cpu().detach().numpy()

            y_pred = y_pred.reshape(-1)
            y_true = y_true.reshape(-1)

            logits = np.copy(y_pred.float().cpu().detach().numpy())
            y_pred = (y_pred > threshold).float().cpu().detach().numpy()
            y_pred = median_seq(y_pred, logits)


            if  (all_y_true is None) and (all_y_pred is None):
                all_y_true = y_true
                all_y_pred = y_pred
            else:
                all_y_true = np.vstack((all_y_true, y_true))
                all_y_pred = np.vstack((all_y_pred, y_pred))

            # undo padding
            y_true = y_true[:seq_len]
            y_pred = y_pred[:seq_len]

            key = key[0] # this is a tuple before indexing the first element which is a string
            number_of_domains = num_of_domains(key)
            category = str(number_of_domains)

            ndo, dbd, mcc_bp = boundary_prediction_metrics(y_pred, y_true, key)
            if not scores.get(category):
                scores[category] = {'boundary_prediction' : []}
            scores[category]['boundary_prediction'].append((ndo, dbd, mcc_bp))
            
            if (i+1) % 150 == 0:
                print(f'Step: [{i+1}/{n_samples}]')

        ps, rs, pm, rm, acc, mcc_sm = domain_number_metrics(all_y_pred, all_y_true, threshold)
        scores['domain_number'] = (ps, pm, rs, rm, acc, mcc_sm)


    model.train()

    print("Finished Testing")
    return scores

def train(model, optimizer, scheduler, train_loader, num_epochs, validation_loader):
    n_total_steps = len(train_loader)
    print("Starting Training")
    model.train()
    for epoch in range(num_epochs):
        all_y_true = None
        all_y_pred = None
        running_loss = []
        validation_loss = []
        for i, (x, y_true, y_amplified, _, _) in enumerate(train_loader):
            x = x.to(device).float()
            y_true = y_true.reshape(-1)
            y_amplified = y_amplified.to(device).float().reshape(-1)
            y_pred = model(x).reshape(-1)
            loss = criterion(y_pred, y_amplified)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            running_loss.append(loss.item())

            if (i+1) % 10 == 0:
                print(f'Epoch: [{epoch+1}/{num_epochs}], Step: [{i+1}/{n_total_steps}], Running Loss: {np.mean(running_loss):.4f}')
                model.loss_history.append(np.mean(running_loss))
                running_loss = []

        model.eval()
        with torch.no_grad():
            for i, (x, y_true, y_amplified, _, seq_len) in enumerate(validation_loader):
                seq_len = seq_len.to(device)
                x = x.to(device).float()
                y_amplified = y_amplified.to(device).float().reshape(-1)
                y_pred = model(x).reshape(-1).float().to(device)
                loss = criterion(y_pred, y_amplified)
                validation_loss.append(loss.item())

                if (i+1) % 2 == 0:
                    print(f'Epoch: [{epoch+1}/{num_epochs}], Step: [{i+1}/{len(validation_loader)}], Running (Val) Loss: {np.mean(validation_loss):.4f}')
                    model.validation_loss_history.append(np.mean(validation_loss))
                    validation_loss = []    

            print(f'Epoch: [{epoch+1}/{num_epochs}], Step: [{i+1}/{len(validation_loader)}], Running (Val) Loss: {np.mean(validation_loss):.4f}')
            model.validation_loss_history.append(np.mean(validation_loss))

        print(f'Epoch: [{epoch+1}/{num_epochs}], Training Loss: {np.mean(running_loss):.4f}, Validation Loss: {np.mean(validation_loss):.4f}')
        scheduler.step()
        
    print(f'Finished training')

    return model