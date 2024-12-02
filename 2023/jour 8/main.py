# Exercice 1
data = open("2023/jour 8/input.txt", "r").read().split("\n")

chemin = data[0]
nodes = [line.split(' = ') for line in data[2:]]

# print(chemin, nodes)

nodes = {dep : arr[1:-1].split(', ') for dep, arr in nodes}

count = 0
en_cours = 'AAA'
index_chemin = 0
while en_cours != 'ZZZ' :
    if chemin[index_chemin] == 'R' :
        choix = 1
    elif chemin[index_chemin] == 'L' :
        choix = 0
    en_cours = nodes[en_cours][choix]
    count += 1
    index_chemin = (index_chemin + 1) % len(chemin)

print(count)



# Exercice 1
data = open("2023/jour 8/input.txt", "r").read().split("\n")

chemin = data[0]
nodes = [line.split(' = ') for line in data[2:]]

# print(chemin, nodes)

nodes = {dep : arr[1:-1].split(', ') for dep, arr in nodes}

def arrivee(tab_nodes) :
    for node in tab_nodes :
        if node[-1] != 'Z' :
            return True
    return False

en_cours = [node for node in nodes.keys() if node[-1] == 'A']

print(en_cours)

res = []

for node in en_cours :
    count = 0
    index_chemin = 0
    node_deb = node
    while node[-1] != 'Z' :
        if chemin[index_chemin] == 'R' :
            choix = 1
        elif chemin[index_chemin] == 'L' :
            choix = 0
        node = nodes[node][choix]
        count += 1
        index_chemin = (index_chemin + 1) % len(chemin)
    res.append([node_deb, node, count, index_chemin])

print(res)

final_nodes = [elem[1] for elem in res]

for index, node in enumerate(final_nodes) :
    count = 1
    index_chemin = 1
    if chemin[0] == 'R' :
        choix = 1
    elif chemin[0] == 'L' :
        choix = 0
    node = nodes[node][choix]
    while node[-1] != 'Z' :
        if chemin[index_chemin] == 'R' :
            choix = 1
        elif chemin[index_chemin] == 'L' :
            choix = 0
        node = nodes[node][choix]
        count += 1
        index_chemin = (index_chemin + 1) % len(chemin)

    res[index] += [count, node, index_chemin]

length_boucle = [[node[2], node[2]] for node in res]


# while min(length_boucle, key=lambda x : x[1]) != max(length_boucle, key=lambda x : x[1]) :
#     index_min = length_boucle.index(min(length_boucle, key=lambda x : x[1]))
#     length_boucle[index_min][1] += length_boucle[index_min][0]

print(length_boucle)

import math
# Les longueures sont [16409, 12643, 21251, 15871, 19637, 11567]
# But trouver le plus petit multiple commun de ces nombre

print(math.lcm(16409, 12643, 21251, 15871, 19637, 11567))