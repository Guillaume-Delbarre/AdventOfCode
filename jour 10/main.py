# Exercice 1
data = open("jour 10/input.txt", "r").read().split("\n")
data = [[char for char in line] for line in data]

# print(data)

for index_ligne, line in enumerate(data) :
    if 'S' in line :
        coord_S = (index_ligne, line.index('S'))

current = []
passed = []
if coord_S[0] > 0 and data[coord_S[0] - 1][coord_S[1]] in ['|', '7', 'F']:
    current.append(((coord_S[0] - 1, coord_S[1]), 1))
    passed.append((coord_S[0] - 1, coord_S[1]))
if coord_S[0] < len(data) - 1 and data[coord_S[0] + 1][coord_S[1]] in ('L', '|', 'J'):
    current.append(((coord_S[0] + 1, coord_S[1]), 1))
    passed.append((coord_S[0] + 1, coord_S[1]))
if coord_S[1] > 0 and data[coord_S[0]][coord_S[1] - 1] in ['L', '-', 'F']:
    current.append(((coord_S[0], coord_S[1] - 1), 1))
    passed.append((coord_S[0], coord_S[1] - 1))
if coord_S[1] < len(data[0]) and data[coord_S[0]][coord_S[1] + 1] in ['J', '-', '7']:
    current.append(((coord_S[0], coord_S[1] + 1), 1))
    passed.append((coord_S[0], coord_S[1] + 1))

# print(current)

boucle = False
while not boucle :
    coords, score = current.pop(0)
    passed.append(coords)
    # print(coords, score)
    if coords[0] > 0 and data[coords[0] - 1][coords[1]] in ['|', '7', 'F'] and data[coords[0]][coords[1]] in ['L', '|', 'J'] and (coords[0] - 1, coords[1]) not in passed :
        current.append(((coords[0] - 1, coords[1]), score + 1))
        # print(f'On est dans le 1 avec {data[coords[0] - 1][coords[1]]}')
    elif coords[0] < len(data) - 1 and data[coords[0] + 1][coords[1]] in ['L', '|', 'J'] and data[coords[0]][coords[1]] in ['|', '7', 'F'] and (coords[0] + 1, coords[1]) not in passed :
        current.append(((coords[0] + 1, coords[1]), score + 1))
        # print(f'On est dans le 2 avec {data[coords[0] + 1][coords[1]]}')
    elif coords[1] > 0 and data[coords[0]][coords[1] - 1] in ['L', '-', 'F'] and data[coords[0]][coords[1]] in ['J', '-', '7'] and (coords[0], coords[1] - 1) not in passed :
        current.append(((coords[0], coords[1] - 1), score + 1))
        # print(f'On est dans le 3 avec {data[coords[0]][coords[1] - 1]}')
    elif coords[1] < len(data[0]) and data[coords[0]][coords[1] + 1] in ['J', '-', '7'] and data[coords[0]][coords[1]] in ['L', '-', 'F'] and (coords[0], coords[1] + 1) not in passed :
        current.append(((coords[0], coords[1] + 1), score + 1))
        # print(f'On est dans le 4 avec {data[coords[0]][coords[1] + 1]}')
    # input(f"{current[0][0]} == {current[-1][0]} avec {current[0][1]} et {current[-1][1]}")
    if current[0][0] == current[-1][0] :
        boucle = True


print(current[0][1])



# Exercice 2

# Compter le nombre de fois qu'on croise le tuyau (si c'est impair alors on est dans la boucle)
data = open("jour 10/exemple_input.txt", "r").read().split("\n")
data = [[char for char in line] for line in data]