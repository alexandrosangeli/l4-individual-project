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

def accuracy20(input, target, n=8):
    """
        A residue is correct if it's within +- 20 residues of the ground truth
    """
    total = 0
    correct = 0
    for i, x in enumerate(target):
        if x == 1:
            total += 1
            
        start = max(i - n, 0)
        end = min(i + n, len(target)-1)
        for j in range(start, end+1):
            if input[j] == 1:
                correct += 1
                input[j] = 0
                break

        
    print(f'{correct}/{total}')
    return correct / total


if __name__ == '__main__':
    in_data = [0] * 100
    in_data[4] = 0.9
    in_data[45] = 0.9
    in_data[90] = 0.9


    target_data = [0] * 100
    target_data[3] = 0.8
    target_data[40] = 0.8
    target_data[95] = 0.8


    a = accuracy20(in_data, target_data)
    print(a)

