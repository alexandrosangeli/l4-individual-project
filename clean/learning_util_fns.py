def is_disc(chain):
    """checks if a domain is discontinuous based on the CASP13 dataset"""
    domains = casp13_dict['domains'][chain]
    for _, bounds in domains.items():
        if ';' in bounds:
            return True
    return False

def boundaries_to_domains(binary_vector):
    """converts a binary vector of boundaries to domains"""
    binary_vector = np.copy(binary_vector)
    domain = 1
    for i in range(len(binary_vector)):
        if int(binary_vector[i]) == 1:
            # this is the start of a new domain
            domain += 1
        binary_vector[i] = domain
    return binary_vector.astype(int)

def ndo_score(y_pred, y_true, key):
    """an attempt to implement the NDO evaluation metric
    the algorithm is not well defined in literature and we were
    getting scores of greater than 1 which shouldn't be possible
    Therefore, we did not employ this algorithm"""
    if is_disc(key):
        return 'n/a'

    y_pred = boundaries_to_domains(y_pred)
    y_true = boundaries_to_domains(y_true)

    table = np.zeros((max(y_pred)+2,max(y_true)+2))
    
    for d_pred, d_true in zip(y_pred, y_true):
        table[d_pred, d_true] += 1

    # columns
    for i in range(1, table.shape[1]-1):
        table[-1, i] = 2 * max(table[:, i]) - sum(table[:, i])

    # rows
    for i in range(1, table.shape[0]-1):
        table[i, -1] = 2 * max(table[i, :]) - sum(table[i, :])

    table[-1, -1] = (sum(table[:, -1]) + sum(table[-1, :])) / 2


    num_of_defined_domains = 0
    for elt in y_true:
        if elt > 0:
            num_of_defined_domains += 1
    score = table[-1, -1] / num_of_defined_domains

    return score



def plot_losses(losses):
    x_label = "Steps"
    y_label = "Running loss"

    # Plot the losses
    plt.figure(figsize=(8, 6), dpi=80)
    plt.title("Running loss over time")
    plt.plot(losses)

    # Add x and y labels to the plot
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Display the plot
    plt.show()


def update_dict(data, code, chain, domain, boundaries):
    data[code] = data.get(code, {})
    if chain not in data[code].keys():
        data[code][chain] = {}
    data[code][chain][str(int(domain))] = boundaries
    return data


def num_of_domains(key):
    return len(casp13_dict['domains'][key])


def get_cath(lines_range = None, file="drive/My Drive/University of Glasgow/L4/L4 Project/cath_domain_boundaries.txt", verb=False):
    """creates a dictionary from the CATH domain boundaries text file"""
    with open(file, "r") as f:
        lines = f.readlines() if lines_range is None else f.readlines()[lines_range[0]:lines_range[1]]
        lines = map(lambda x : x.strip(), lines)
        big = 0
        data = {}
        for line in lines:
            name, boundaries = line.split("\t")
            code = name[:4]
            chain = name[4]
            domain = name[5:]
            data = update_dict(data, code, chain, domain, boundaries)
    # verb and pprint(data)
    return data

def load_data(path, encoding):
    encoding_file = encoding_map[encoding]
    data = pd.read_pickle(path + encoding_file)
    return data


def median_seq(seq, logits):
    """converts a binary vector with boundary regions to just a binary vector
    with one boundary per region"""
    
    new_seq = np.zeros(len(seq))
    consecutive_ones_indices = []
    medians = []

    # marks if the first consecutive zeros that are less than the typical size is the first (meaning is the beginning of the first domain)
    for i in range(len(seq)):
        if seq[i] == 0:
            if len(consecutive_ones_indices) > 0:
                h = [logits[elt] for elt in consecutive_ones_indices]
                point = consecutive_ones_indices[np.argmax(h)]
                medians.append(point)
            consecutive_ones_indices = []

        if seq[i] == 1:
            consecutive_ones_indices.append(i)

    if len(consecutive_ones_indices) > 0:
        h = [logits[elt] for elt in consecutive_ones_indices]
        point = consecutive_ones_indices[np.argmax(h)]
        medians.append(point)

    for elt in medians:
        new_seq[elt] = 1

    return new_seq

def amplify_sharp(arr, size=41):
    conv = np.ones((size))
    result = np.convolve(arr, conv, mode='same')
    normalize_by = np.max(result)
    result = result / max(normalize_by, 1)
    return result 