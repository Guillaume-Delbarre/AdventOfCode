# Exercice 1
data = open("jour 22/exemple_input.txt", "r").read().split('\n')
data = [line.split('~') for line in data]

blocks = {}

for index, block in enumerate(data) :
    coor1 = list(map(int, block[0].split(',')))
    coor2 = list(map(int, block[1].split(',')))

    b = [[x, y, z] for x in range(min(coor1[0], coor2[0]), max(coor1[0], coor2[0]) + 1)
                        for y in range(min(coor1[1], coor2[1]), max(coor1[1], coor2[1]) + 1)
                        for z in range(min(coor1[2], coor2[2]), max(coor1[2], coor2[2]) + 1)]

    blocks[index] = {"pos"    : b,
                     "sup"    : [],
                     "is_sup" : []}

moved = True
while moved :
    moved = False
    for index, block in blocks.items() :
        blocks[index]["sup"] = []
        blocks[index]["is_sup"] = []

    # Récupération des infos des blocks
    for index, block in blocks.items() :
        for x, y, z in block["pos"] :
            if z > 1 :
                for other_index, other_block in blocks.items() :
                    if [x, y, z-1] in other_block["pos"] and index not in other_block["sup"] and other_index != index:
                        blocks[index]["is_sup"].append(other_index)
                        blocks[other_index]["sup"].append(index)

    # Fait tomber les bricks
    for index, block in blocks.items() :
        if len(block["is_sup"]) == 0 and min(blocks[index]["pos"], key=lambda x : x[2])[2] > 1 :
            moved = True
            blocks[index]["pos"] = [[x, y, z-1] for x, y, z in blocks[index]["pos"]]
    
    
score = 0
for index, block in blocks.items() :
    # print(index, block)
    enlevable = True
    for i in block["sup"] :
        if len(blocks[i]["is_sup"]) <= 1 :
            enlevable = False
    if enlevable :
        # print(f"{index} est enlevable")
        score += 1

print(score)
# Tres long avec les données input, une idée aurait été de descendre les briques le plus possible en commençant par celles qui ont la coord z la plus faible


# Exercice 2
data = open("jour 22/input.txt", "r").read().split('\n')
data = [line.split('~') for line in data]

blocks = {}

for index, block in enumerate(data) :
    coor1 = list(map(int, block[0].split(',')))
    coor2 = list(map(int, block[1].split(',')))

    b = [[x, y, z] for x in range(min(coor1[0], coor2[0]), max(coor1[0], coor2[0]) + 1)
                        for y in range(min(coor1[1], coor2[1]), max(coor1[1], coor2[1]) + 1)
                        for z in range(min(coor1[2], coor2[2]), max(coor1[2], coor2[2]) + 1)]

    blocks[index] = {"pos"    : b,
                     "sup"    : [],
                     "is_sup" : []}

moved = True
while moved :
    moved = False
    for index, block in blocks.items() :
        blocks[index]["sup"] = []
        blocks[index]["is_sup"] = []

    # Récupération des infos des blocks
    for index, block in blocks.items() :
        for x, y, z in block["pos"] :
            if z > 1 :
                for other_index, other_block in blocks.items() :
                    if [x, y, z-1] in other_block["pos"] and index not in other_block["sup"] and other_index != index:
                        blocks[index]["is_sup"].append(other_index)
                        blocks[other_index]["sup"].append(index)

    # Fait tomber les bricks
    for index, block in blocks.items() :
        if len(block["is_sup"]) == 0 and min(blocks[index]["pos"], key=lambda x : x[2])[2] > 1 :
            moved = True
            blocks[index]["pos"] = [[x, y, z-1] for x, y, z in blocks[index]["pos"]]
    
score = 0
for index, block in blocks.items() :
    # print(index, block)
    enlevable = True
    for i in block["sup"] :
        if len(blocks[i]["is_sup"]) <= 1 :
            enlevable = False
    
    if not enlevable :
        nb_pour_ind = 0
        b = block["sup"]
        deja_tomb = []
        while len(b) > 0 :
            bl = b.pop()
            deja_tomb.append(bl)
            nb_pour_ind += 1
            b += [i for i in blocks[bl]["sup"] if i not in deja_tomb]
        score += nb_pour_ind

print(score)
# Tres long avec les données input, une idée aurait été de descendre les briques le plus possible en commençant par celles qui ont la coord z la plus faible
