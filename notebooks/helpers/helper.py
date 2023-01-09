from pprint import pprint
import numpy as np
import pandas as pd


def update_dict(data, code, chain, domain, boundaries):
    data[code] = data.get(code, {})
    if chain not in data[code].keys():
        data[code][chain] = {}
    data[code][chain][str(int(domain))] = boundaries
    return data


def get_cath(lines_range = None, file="../data/cath/cath_domain_boundaries.txt", verb=False):
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
    verb and pprint(data)
    return data


def get_sword2(code, chain, verb=False):
    
    file = f"../data/sword2/SWORD2/results/{code}_{chain.upper()}/sword.txt"
    with open(file, "r") as f:
        data = {}
        lines = f.readlines()
        option = 0
        for i, line in enumerate(lines):
            lines[i] = "".join([c for c in line if c not in ["\n",'']])
            if line != "\n":
                if not line.startswith(("PDB:", "#D", "A")):
                    res = lines[i].split("|")
                    boundaries = res[2]
                    domains = boundaries.strip().split(" ")
                    data[f"option{option}"] = {}
                    for j in range(len(domains)):
                        data[f"option{option}"][str(j+1)] = domains[j]
                    option += 1
    verb and pprint(data)
    return data