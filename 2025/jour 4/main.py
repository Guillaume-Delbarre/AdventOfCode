# Exercice 1
data = open("2025/jour 4/input.txt", "r").read().split("\n")
data = [[el for el in ligne] for ligne in data]

def print_table(data) :
    for line in data :
        print("".join(line))

res = 0
diff = 1

while diff != 0 :
    diff = 0
    modifs = []
    for y in range(len(data[0])) :
        for x in range(len(data)) :
            if data[y][x] == "@" :
                count = 0
                for dx in (-1, 0, 1) :
                    for dy in (-1, 0, 1) :
                        nx = x+dx
                        ny = y+dy
                        if nx >= 0 and nx < len(data[0]) and ny >= 0 and ny < len(data) and (nx != x or ny != y) :
                            if data[ny][nx] == "@" :
                                count += 1
                if count < 4 :
                    diff += 1
                    modifs.append((y, x))

    new_data = [[el for el in line] for line in data]
    for y,x in modifs :
        new_data[y][x] = '.'

    data = new_data
    res += diff

print(res)
