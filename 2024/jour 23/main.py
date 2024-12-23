# Exercice 1
data = open("2024/jour 23/input.txt", "r").read().split("\n")
data = [d.split('-') for d in data]

con = {}
for c1, c2 in data :
    if c1 not in con.keys() :
        con[c1] = [c2]
    elif c2 not in con[c1] :
        con[c1].append(c2)
    if c2 not in con.keys() :
        con[c2] = [c1]
    elif c1 not in con[c2] :
        con[c2].append(c1)

res = []
for c in [c for c in con.keys() if c[0] == 't'] :
    for c1 in con[c] :
        for c2 in con[c1] :
            if c2 != c and c2 in con[c] :
                el = [c, c1, c2]
                el.sort()
                if el not in res :
                    res.append(el)

print(len(res))