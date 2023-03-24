def confusion_matrix_B(all_y_pred, all_y_true, t, margin=20):
    """calculates a confusion matrix from two 2D matrices"""
    ts, tm, fs, fm = 0, 0, 0, 0
    for (y_pred, y_true) in zip(all_y_pred, all_y_true):
        y_true = np.copy(y_true)
        y_pred = np.copy(median_seq(np.where(y_pred > t, 1, 0), y_pred))

        true_num = np.sum(y_true)
        pred_num = np.sum(y_pred)
        if int(true_num) == 0 and int(pred_num) == 0:
            ts += 1
        
        if int(true_num) > 0 and int(pred_num) > 0:
            tm += 1

        if int(true_num) == 0 and int(pred_num) > 0:
            fm += 1

        if int(true_num) > 0 and int(pred_num) == 0:
            fs += 1
    return (ts, tm, fs, fm)

def mcc_single_multi(ts, tm, fs, fm):
    """finds the MCC given the true/false positives/negatives count"""
    mcc_num = (tm * ts) - (fm * fs)
    mcc_den = ((tm + fm) * (tm + fs) * (fm + ts) * (ts + fs))**0.5
    mcc = mcc_num / mcc_den if mcc_den != 0 else 0
    return mcc

def optimise_single_multi_mcc(all_y_pred, all_y_true, max_num_iterations=10, linspace_size=16, start=0, end=1, ):
    """finds an optimal value for t which maximises MCC"""
    best_score = 0
    i = 0
    flag = True
    pairs = []
    while max_num_iterations > i and flag:
        flag = False
        for t in np.linspace(start, end, linspace_size):
            ts, tm, fs, fm = confusion_matrix_B(all_y_pred, all_y_true, t)
            ps, rs, pm, rm, acc, mcc = num_of_domains_metrics((ts, tm, fs, fm))
            score = mcc
            # score = mcc_single_multi(ts, tm, fs, fm)
            pairs.append((ps, rs, pm, rm, acc, mcc, t))
            if score > best_score:
                best_t = t
                best_score = score
                flag = True
        start = best_t * 0.7
        end = best_t * 1.3
        i += 1
        linspace_size += 2
    return best_score, best_t, pairs

def dbd_score(y_pred, y_true, margin=20):
    """finds the domain boundary distance score"""
    scores = []
    number_of_true_boundaries = np.sum(y_true)
    number_of_pred_boundaries = np.sum(y_pred)
    denominator = max(number_of_true_boundaries,number_of_pred_boundaries)

    if denominator == 0:
        return 'n/a'

    y_true_cp = np.copy(y_true)
    for i in range(len(y_pred)):
        window = y_true_cp[max(0, i-margin):min(len(y_true_cp), i+margin+1)]
        indices_window = list(range(max(0, i-margin), min(len(y_true_cp), i+margin+1)))
        if y_pred[i] == 1.0:
            if 1.0 in window:
                positions_with_boundaries = np.argwhere(window == 1).flatten()
                js = [indices_window[pos] for pos in positions_with_boundaries]
                closest_j = js[0]
                for j in js:
                    if abs(j - i) < abs(closest_j - i):
                        closest_j = j
                diff = abs(i - closest_j)
                score = ((margin - diff) + 1) / (margin + 1)
                y_true_cp[closest_j] = 0
                scores.append(score)
    return np.sum(scores) / denominator

def num_of_domains_metrics(confusion_matrix_num):
    """calcualtes the precision, recall, accuracy and MCC from a confusion matrix"""
    ts, tm, fs, fm = confusion_matrix_num
    # single
    pre_single = ts / (ts + fs) if (ts + fs) != 0 else 0
    rec_single = ts / (ts + fm) if (ts + fm) != 0 else 0
    
    # multi
    pre_multi = tm / (tm + fm) if (tm + fm) != 0 else 0
    rec_multi = tm / (tm + fs) if (tm + fs) != 0 else 0

    acc = (tm + ts) / (tm + ts + fm + fs)

    # mcc
    mcc_num = (tm * ts) - (fm * fs)
    mcc_den = ((tm + fm) * (tm + fs) * (fm + ts) * (ts + fs))**0.5
    mcc = mcc_num / mcc_den if mcc_den != 0 else 0

    return (pre_single, rec_single, pre_multi, rec_multi, acc, mcc)

def test_number_of_domains_predicted(model, validation_loader, threshold):
    """finds the number of domains (predicted and true) and generates a confusion matrix used to visualise data"""
    n_samples = len(validation_loader)
    confusion_matrix = np.zeros((12,12))
    model.eval()
    coords = []
    with torch.no_grad():
        for i, (input, y_true, _, key, seq_len) in enumerate(validation_loader):
            input = input.float().to(device)
            y_pred = model(input)

            y_pred = y_pred.cpu()
            y_true = y_true.cpu().detach().numpy()

            y_pred = y_pred.reshape(-1)
            y_true = y_true.reshape(-1)

            y_pred = median_seq((y_pred > threshold).float().cpu().detach().numpy(),y_pred)
            # y_pred = median_seq(y_pred)

            predicted_number = int(np.sum(y_pred))
            true_number = int(np.sum(y_true))
            coords.append((predicted_number, true_number))
            
            confusion_matrix[predicted_number, true_number] += 1

    return confusion_matrix

def single_multi_cf(model, validation_loader, threshold):
    """finds the number of single/multi domains and generates a confusion matrix used to visualise data"""
    n_samples = len(validation_loader)
    confusion_matrix = np.zeros((2,2))
    model.eval()
    with torch.no_grad():
        for i, (input, y_true, _, key, seq_len) in enumerate(validation_loader):
            input = input.float().to(device)
            y_pred = model(input)

            y_pred = y_pred.cpu()
            y_true = y_true.cpu().detach().numpy()

            y_pred = y_pred.reshape(-1)
            y_true = y_true.reshape(-1)

            y_pred = median_seq((y_pred > threshold).float().cpu().detach().numpy(),y_pred)

            prediction = min(int(np.sum(y_pred)), 1)

            truth = min(int(np.sum(y_true)), 1)
            
            confusion_matrix[prediction, truth] += 1

    return confusion_matrix

def domain_number_sequence_length(model, validation_loader, threshold):
    """returns two vectors: predictions and truths which hold tuples of (sequence length, number of domains)
    used to visualise the relatioship between the two variables"""
    n_samples = len(validation_loader)
    predictions = []
    truths = []
    model.eval()
    with torch.no_grad():
        for i, (input, y_true, _, key, seq_len) in enumerate(validation_loader):
            input = input.float().to(device)
            y_pred = model(input)

            y_pred = y_pred.cpu()
            y_true = y_true.cpu().detach().numpy()

            y_pred = y_pred.reshape(-1)
            y_true = y_true.reshape(-1)

            y_pred = median_seq((y_pred > threshold).float().cpu().detach().numpy(),y_pred)

            prediction = int(np.sum(y_pred))
            truth = int(np.sum(y_true))

            predictions.append((prediction, seq_len))
            truths.append((truth, seq_len))

    return predictions, truths