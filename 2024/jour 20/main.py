import copy
# Exercice 1
data = open("2024/jour 20/exemple_input.txt", "r").read().split("\n")
data = [list(d) for d in data]

# Récupération du point de départ
for y in range(len(data)) :
    for x in range(len(data[y])) :
        if data[y][x] == 'S' :
            break
    else :
        continue
    break
start = (x, y)

# Création du nouveau tableau avec les distances
distances = copy.deepcopy(data)
d=1
fini = False
while not fini :
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
        if distances[y+dy][x+dx] == '.' :
            x += dx
            y += dy
            distances[y][x] = d
            d += 1
            break
        elif distances[y+dy][x+dx] == 'E' :
            x += dx
            y += dy
            distances[y][x] = d
            fini = True

shortcuts = []