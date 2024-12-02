# Exercice 1
data = open("2023/jour 11/exemple_input.txt", "r").read().split("\n")

# print(data)

# Expention des données
col_empt = [index for index in range(len(data[0])) if all([data[i][index] == '.' for i in range(len(data))])]
li_empt = [index for index, ligne in enumerate(data) if all([i == '.' for i in ligne])]


for dej_rajoute, index_li in enumerate(li_empt) :
    data.insert(index_li+dej_rajoute, '.'*len(data[0]))

for dej_rajoute, index_col in enumerate(col_empt) :
    for i in range(len(data)) :
        data[i] = data[i][:index_col + dej_rajoute] + '.' + data[i][index_col + dej_rajoute:]


points = [(x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == '#']

score = 0

for index, (x1, y1) in enumerate(points) :
    if index != len(points) - 1 :
        for x2, y2 in points[index+1:] :
            score += abs(y2 - y1) + abs(x2 - x1)
            # print(f"ajout de {abs(y2 - y1) + abs(x2 - x1)} pour les points {x1, y1} / {x2, y2}")

print(score)


# Exercice 2
data = open("2023/jour 11/input.txt", "r").read().split("\n")

# print(data)

# Expention des données
col_empt = [index for index in range(len(data[0])) if all([data[i][index] == '.' for i in range(len(data))])]
li_empt = [index for index, ligne in enumerate(data) if all([i == '.' for i in ligne])]

points = [(x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == '#']


def modify_coords(x, y) :
    x_modif = 0
    y_modif = 0
    for col in col_empt :
        if col < x :
            x_modif += 1000000 - 1
    for li in li_empt :
        if li < y :
            y_modif += 1000000 - 1
    return ((x+x_modif), (y + y_modif))

points = list(map(lambda p : modify_coords(p[0],p[1]), points))


score = 0
for index, (x1, y1) in enumerate(points) :
    if index != len(points) - 1 :
        for x2, y2 in points[index+1:] :
            score += abs(y2 - y1) + abs(x2 - x1)
            # print(f"ajout de {abs(y2 - y1) + abs(x2 - x1)} pour les points {x1, y1} / {x2, y2}")

print(score)