import copy

# Exercice 1
data = open("2024/jour 6/input.txt", "r").read().split("\n")
data = [list(d) for d in data]
#print(data)

# Récupération des coordonnées initiales
for y in range(len(data)) :
    for x in range(len(data[y])) :
        if data[y][x] == '^' :
            coords = [y, x]
            break
    else :
        continue
    break

dir = [-1, 0]
sortie = False
while not sortie :
    data[coords[0]][coords[1]] = 'X'
    old_coords = [coords[0], coords[1]]
    coords = [coords[0] + dir[0], coords[1] + dir[1]]
    if coords[0] < 0 or coords[0] >= len(data) or coords[1] < 0 or coords[1] >= len(data[coords[0]]) :
        # On est sortie
        sortie = True
        break
    elif data[coords[0]][coords[1]] == '#' :
        # tourne droite
        if dir == [-1, 0] :
            dir = [0, 1]
        elif dir == [0, 1] :
            dir = [1, 0]
        elif dir == [1, 0] :
            dir = [0, -1]
        elif dir == [0, -1] :
            dir = [-1, 0]
        coords = [old_coords[0] + dir[0], old_coords[1] + dir[1]]

# Compte des cases
score = len([data[y][x] for x in range(len(data[y])) for y in range(len(data)) if data[y][x] == 'X'])
print(score)


# Exercice 2
data = open("2024/jour 6/input.txt", "r").read().split("\n")
data = [list(d) for d in data]
#print(data)


# Récupération des coordonnées initiales
for y in range(len(data)) :
    for x in range(len(data[y])) :
        if data[y][x] == '^' :
            start_coords = [y, x]
            break
    else :
        continue
    break

score = 0
for pos_y in range(len(data)) :
    for pos_x in range(len(data[pos_y])) :
        if data[pos_y][pos_x] == '.' :
            new_data = copy.deepcopy(data)
            coords = copy.deepcopy(start_coords)
            new_data[pos_y][pos_x] = '#'
            directions = [[[] for _ in range(len(data[0]))] for _ in range(len(data))]
            dir = [-1, 0]

            sortie = False
            boucle = False
            while not sortie or not boucle :
                if (dir[0], dir[1]) in directions[coords[0]][coords[1]] :
                    boucle = True
                    break
                else :
                    directions[coords[0]][coords[1]].append((dir[0], dir[1]))
                old_coords = [coords[0], coords[1]]
                coords = [coords[0] + dir[0], coords[1] + dir[1]]
                if coords[0] < 0 or coords[0] >= len(data) or coords[1] < 0 or coords[1] >= len(data[coords[0]]) :
                    # On est sortie
                    sortie = True
                    break
                elif new_data[coords[0]][coords[1]] == '#' :
                    # tourne droite
                    if dir == [-1, 0] :
                        dir = [0, 1]
                    elif dir == [0, 1] :
                        dir = [1, 0]
                    elif dir == [1, 0] :
                        dir = [0, -1]
                    elif dir == [0, -1] :
                        dir = [-1, 0]
                    coords = [old_coords[0] + dir[0], old_coords[1] + dir[1]]
            if boucle :
                score += 1
print(score)