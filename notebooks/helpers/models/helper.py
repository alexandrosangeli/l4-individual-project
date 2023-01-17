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
