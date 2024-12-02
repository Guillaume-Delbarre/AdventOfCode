# Exercice 1
data = open("2023/jour 14/input.txt", "r").read().split("\n")

# print(data)

rocks = [(col, row) for row in range(len(data)) for col in range(len(data[0])) if data[row][col] == 'O']

while len(rocks) > 0 :
    rock = rocks.pop(0)
    # print(f"On traite la rock {rock} et pour le moment on a : ")
    # print('\n'.join(data))
    # print()
    row = rock[1]
    while data[row - 1][rock[0]] == '.' and row > 0:
        row -= 1

    if rock[0] + 1 == len(data[0]) :
        data[rock[1]] = data[rock[1]][:rock[0]] + '.'
        data[row] = data[row][:rock[0]] + 'O'
    else :
        data[rock[1]] = data[rock[1]][:rock[0]] + '.' + data[rock[1]][rock[0]+1:]
        data[row] = data[row][:rock[0]] + 'O' + data[row][rock[0]+1:]

score = [len(data) - row for row in range(len(data)) for col in range(len(data[0])) if data[row][col] == 'O']
print(sum(score))


# Exercice 2
import copy
data = open("2023/jour 14/input.txt", "r").read().split("\n")

def get_rocks(data) :
    return [(col, row) for row in range(len(data)) for col in range(len(data[0])) if data[row][col] == 'O']

def rool_north(data) :
    rocks = get_rocks(data)
    while len(rocks) > 0 :
        rock = rocks.pop(0)
        row = rock[1]
        while data[row - 1][rock[0]] == '.' and row > 0:
            row -= 1

        if rock[0] + 1 == len(data[0]) :
            data[rock[1]] = data[rock[1]][:rock[0]] + '.'
            data[row] = data[row][:rock[0]] + 'O'
        else :
            data[rock[1]] = data[rock[1]][:rock[0]] + '.' + data[rock[1]][rock[0]+1:]
            data[row] = data[row][:rock[0]] + 'O' + data[row][rock[0]+1:]
    return data

def rool_west(data) :
    rocks = get_rocks(data)
    while len(rocks) > 0 :
        rock = rocks.pop(0)
        col = rock[0]
        while data[rock[1]][col - 1] == '.' and col > 0:
            col -= 1

        if col + 1 == len(data[0]) :
            data[rock[1]] = data[rock[1]][:rock[0]] + '.' + data[rock[1]][rock[0]+1:]
            data[rock[1]] = data[rock[1]][:col] + 'O'
        else :
            data[rock[1]] = data[rock[1]][:rock[0]] + '.' + data[rock[1]][rock[0]+1:]
            data[rock[1]] = data[rock[1]][:col] + 'O' + data[rock[1]][col+1:]
    return data

def rool_south(data) :
    rocks = get_rocks(data)
    rocks = [rocks[i-1] for i in range(len(rocks),0, -1)]
    while len(rocks) > 0 :
        rock = rocks.pop(0)
        row = rock[1]
        while row < len(data) - 1 and data[row + 1][rock[0]] == '.':
            row += 1

        if rock[0] + 1 == len(data[0]) :
            data[rock[1]] = data[rock[1]][:rock[0]] + '.'
            data[row] = data[row][:rock[0]] + 'O'
        else :
            data[rock[1]] = data[rock[1]][:rock[0]] + '.' + data[rock[1]][rock[0]+1:]
            data[row] = data[row][:rock[0]] + 'O' + data[row][rock[0]+1:]
    return data

def rool_east(data) :
    rocks = get_rocks(data)
    rocks = [rocks[i-1] for i in range(len(rocks),0, -1)]
    while len(rocks) > 0 :
        rock = rocks.pop(0)
        col = rock[0]
        while col < len(data[0]) - 1 and data[rock[1]][col + 1] == '.':
            col += 1

        if col + 1 == len(data[0]) :
            data[rock[1]] = data[rock[1]][:rock[0]] + '.' + data[rock[1]][rock[0]+1:]
            data[rock[1]] = data[rock[1]][:col] + 'O'
        else :
            data[rock[1]] = data[rock[1]][:rock[0]] + '.' + data[rock[1]][rock[0]+1:]
            data[rock[1]] = data[rock[1]][:col] + 'O' + data[rock[1]][col+1:]
    return data

old_datas = []
for cycle in range(1, 1000000000) :
    old_datas.append(copy.deepcopy(data))

    rool_north(data)
    # print(f"Data au cycle {cycle} après Nort: ")
    # print('\n'.join(data))
    # print()
    rool_west(data)
    # print(f"Data au cycle {cycle} après West: ")
    # print('\n'.join(data))
    # print()
    rool_south(data)
    # print(f"Data au cycle {cycle} après South: ")
    # print('\n'.join(data))
    # print()
    rool_east(data)
    # print(f"Data au cycle {cycle} après East: ")
    # print('\n'.join(data))
    # print()

    # if cycle in [1, 2, 3, 4] :
    #     print(f"Data au cycle {cycle} : ")
    #     print('\n'.join(data))
    #     print()

    # if cycle > 4 :
    #     break
    trouve = False
    for index, old_data in enumerate(old_datas) :
        eg = [data[x][y] == old_data[x][y] for x in range(len(data)) for y in range(len(data[0]))]
        if all(eg) :
            trouve = True
            break
    if trouve :
        break

cycle_fin = (1000000000 - index) % (cycle - index)

n_data = old_datas[index + cycle_fin]

score = [len(n_data) - row for row in range(len(n_data)) for col in range(len(n_data[0])) if n_data[row][col] == 'O']
print(sum(score))

