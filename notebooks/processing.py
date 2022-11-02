from pprint import pprint

def update_dict(data, code, chain, domain, boundaries):
    data[code] = data.get(code, {})
    # try:
    #     x = data[code][chain]
    # except:
    #     x = None
    data[code][chain] = data.get(chain, {})
    data[code][chain].update({domain : boundaries})
    return data

    
# import os 
# cwd = os.getcwd()
# print()
# print()

with open("data/cath/cath_domain_boundaries.txt") as f:
    lines = f.readlines()[62:65]
    lines = map(lambda x : x.strip(), lines)
    big = 0
    data = {}
    for line in lines:
#         check that the name is always 7 chars long
#         if len(name) > big:
#             big = len(name)

        name, boundaries = line.split("\t")
        code = name[:4]
        chain = name[4]
        domain = name[5:]
        data = update_dict(data, code, chain, domain, boundaries)

    pprint(data)
