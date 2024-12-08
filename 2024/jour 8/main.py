# Exercice 1
data = open("2024/jour 8/input.txt", "r").read().split("\n")
data = [list(d) for d in data]

# Récupération des nodes
nodes = {}
for row in range(len(data)) :
    for col in range(len(data[0])) :
        if data[row][col] != "." :
            if data[row][col] in nodes.keys() :
                nodes[data[row][col]].append((row, col))
            else :
                nodes[data[row][col]] = [(row, col)]


antinodes = set()
for node in nodes.keys() :
    for i_pn in range(len(nodes[node])) :
        for i_sn in range(len(nodes[node])) :
            if i_pn != i_sn :
                d_row, d_col = nodes[node][i_pn][0] - nodes[node][i_sn][0], nodes[node][i_pn][1] - nodes[node][i_sn][1]
                if nodes[node][i_pn][0] + d_row < 0 or nodes[node][i_pn][0] + d_row >= len(data) or nodes[node][i_pn][1] + d_col < 0 or nodes[node][i_pn][1] + d_col >= len(data[0]) :
                    continue
                else :
                    antinodes.add((nodes[node][i_pn][0] + d_row, nodes[node][i_pn][1] + d_col))

print(len(antinodes))



# Exercice 2
data = open("2024/jour 8/input.txt", "r").read().split("\n")
data = [list(d) for d in data]

# Récupération des nodes
nodes = {}
for row in range(len(data)) :
    for col in range(len(data[0])) :
        if data[row][col] != "." :
            if data[row][col] in nodes.keys() :
                nodes[data[row][col]].append((row, col))
            else :
                nodes[data[row][col]] = [(row, col)]

l = []
for nod in nodes.keys() :
    l += nodes[nod]

antinodes = set(l)
for node in nodes.keys() :
    for i_pn in range(len(nodes[node])) :
        for i_sn in range(len(nodes[node])) :
            if i_pn != i_sn :
                d_row, d_col = nodes[node][i_pn][0] - nodes[node][i_sn][0], nodes[node][i_pn][1] - nodes[node][i_sn][1]
                sortie = False
                i = 0
                while not sortie :
                    i += 1
                    if nodes[node][i_pn][0] + i*d_row < 0 or nodes[node][i_pn][0] + i*d_row >= len(data) or nodes[node][i_pn][1] + i*d_col < 0 or nodes[node][i_pn][1] + i*d_col >= len(data[0]) :
                        sortie = True
                    else :
                        antinodes.add((nodes[node][i_pn][0] + i*d_row, nodes[node][i_pn][1] + i*d_col))

print(len(antinodes))