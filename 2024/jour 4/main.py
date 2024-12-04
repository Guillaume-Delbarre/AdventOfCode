# Exercice 1
data = open("2024/jour 4/input.txt", "r").read().split("\n")
data = [[el for el in d] for d in data]
# data = [data[0]]
#print(data)

order = ['X', 'M', 'A', 'S']
score = 0

for y in range(len(data)) :
    for x in range(len(data[y])) :
        i = 0
        if data[y][x] == 'X' :
            for d_y in [-1, 1, 0] :
                for d_x in [-1, 1, 0] :
                    valid = True
                    for index, l in enumerate(order) :
                        n_x = x + (d_x * index)
                        n_y = y + (d_y * index)
                        if not (n_x >= 0 and n_y >= 0 and n_y < len(data) and n_x < len(data[n_y]) and data[n_y][n_x] == l):
                            valid = False
                            break
                    if valid :
                        score += 1

print(score)


# Exercice 2
data = open("2024/jour 4/input.txt", "r").read().split("\n")
data = [[el for el in d] for d in data]

score = 0

for y in range(len(data)) :
    for x in range(len(data[y])) :
        if data[y][x] == 'A' :
            if x-1 >= 0 and y-1 >= 0 and y+1 < len(data) and x+1 < len(data[y+1]) :
                if data[y-1][x-1] in ['M', 'S'] and data[y+1][x+1] in ['M', 'S'] and data[y+1][x+1] != data[y-1][x-1] :
                    if data[y+1][x-1] in ['M', 'S'] and data[y-1][x+1] in ['M', 'S'] and data[y-1][x+1] != data[y+1][x-1] :
                        score += 1

print(score)
                    
