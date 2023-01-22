def accuracy(input, target):
    """
        Let the score of accuracy be the correctly predicted boundaries divided by the total number of boundaries (ones) in the protein
    """
    total = 0
    correct = 0
    for i, x in enumerate(target):
        if int(x) == 1:
            total += 1

            if int(input[i]) == 1:
                correct += 1
    return correct / total


def metrics(input, target):
    true_positive = 0
    true_negative = 0
    false_negative = 0
    false_positive = 0

    for i, x in enumerate(target):
        if int(x) == 1 and int(input[i]) == 1:
            true_positive += 1
        if int(x) == 1 and int(input[i]) == 0:
            false_negative += 1
        if int(x) == 0 and int(input[i]) == 1:
            false_positive += 1
        if int(x) == 0 and int(input[i]) == 0:
            true_negative += 1

    try:
        accuracy = (true_negative + true_positive) / (true_negative + true_positive + false_negative + false_positive)
    except ZeroDivisionError:
        accuracy = 0

    try:
        precision = true_positive / (true_positive + false_positive)
    except ZeroDivisionError:
        precision = 0

    try:
        recall = true_positive / (true_positive + false_negative)
    except ZeroDivisionError:
        recall = 0

    try:
        f1 = (2 * precision * recall) / (precision + recall)
    except ZeroDivisionError:
        f1 = 0

    return (accuracy, precision, recall, f1)


def accuracyΝ(y_pred, y_true, n=8):
    """
        A residue is correct if it's within +- 20 residues of the ground truth
    """
    total = 0
    correct = 0
    for i, x in enumerate(y_true):
        if int(x) == 1:
            total += 1
            
        start = max(i - n, 0)
        end = min(i + n, len(y_true)-1)
        for j in range(start, end+1):
            if int(y_pred[j]) == 1:
                correct += 1
                y_pred[j] = 0
                break

    return correct / total


if __name__ == '__main__':
    in_data = [0] * 100
    in_data[4] = 1
    in_data[45] = 1
    in_data[90] = 1
    in_data[91] = 1

    target_data = [0] * 100
    target_data[3] = 1
    target_data[40] = 1
    target_data[95] = 1

    a = accuracy(in_data, target_data)
    print(a)