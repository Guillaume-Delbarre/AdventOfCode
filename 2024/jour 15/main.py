# Exercice 1
data = open("2024/jour 15/input.txt", "r").read().split("\n\n")

tiles = [list(d) for d in data[0].split("\n")]
mouvements = []
for m in data[1].split("\n") :
    mouvements += list(m)

# Récupération des coordonnées initiales
for y in range(len(tiles)) :
    for x in range(len(tiles[y])) :
        if tiles[y][x] == '@' :
            rx, ry = x, y
            break
    else :
        continue
    break

for m in mouvements :
    match m :
        case '<' :
            dx, dy = -1, 0
        case '>' :
            dx, dy = 1, 0
        case '^' :
            dx, dy = 0, -1
        case 'v' :
            dx, dy = 0, 1
    
    if tiles[y + dy][x + dx] == '.' :
        tiles[y][x] = '.'
        tiles[y + dy][x + dx] = '@'
        y += dy
        x += dx
    elif tiles[y + dy][x + dx] == 'O' :
        i = 1
        while tiles[y + dy*i][x + dx*i] == 'O' :
            i += 1
        if tiles[y + dy*i][x + dx*i] == '.' :
            tiles[y + dy][x + dx] = '@'
            tiles[y + dy*i][x + dx*i] = 'O'
            tiles[y][x] = '.'
            y += dy
            x += dx

score = 0
for y in range(len(tiles)) :
    for x in range(len(tiles[y])) :
        if tiles[y][x] == 'O' :
            score += 100*y + x

print(score)


# Exercice 2
data = open("2024/jour 15/exemple_input.txt", "r").read().split("\n\n")

tiles = []
for d in data[0].split("\n") :
    line = []
    for el in d :
        if el == '#' :
            line += ['#', '#']
        elif el == 'O' :
            line += ['[', ']']
        elif el == '.' :
            line += ['.', '.']
        elif el == '@' :
            line += ['@', '.']
    tiles.append(line)

mouvements = []
for m in data[1].split("\n") :
    mouvements += list(m)

# Récupération des coordonnées initiales
for y in range(len(tiles)) :
    for x in range(len(tiles[y])) :
        if tiles[y][x] == '@' :
            rx, ry = x, y
            break
    else :
        continue
    break

for m in mouvements :
    match m :
        case '<' :
            dx, dy = -1, 0
        case '>' :
            dx, dy = 1, 0
        case '^' :
            dx, dy = 0, -1
        case 'v' :
            dx, dy = 0, 1
    
    if tiles[y + dy][x + dx] == '.' :
        tiles[y][x] = '.'
        tiles[y + dy][x + dx] = '@'
        y += dy
        x += dx
    elif tiles[y + dy][x + dx] in ('[', ']') :
        if tiles[y + dy][x + dx] == '[' :
            to_look = [(y + dy, x + dx), (y + dy, x + dx + 1)]
        else :
            to_look = [(y + dy, x + dx), (y + dy, x + dx - 1)]
        i = 1
        while True :
            for tile in 

        while tiles[y + dy*i][x + dx*i] == 'O' :
            i += 1
        if tiles[y + dy*i][x + dx*i] == '.' :
            tiles[y + dy][x + dx] = '@'
            tiles[y + dy*i][x + dx*i] = 'O'
            tiles[y][x] = '.'
            y += dy
            x += dx

score = 0
for y in range(len(tiles)) :
    for x in range(len(tiles[y])) :
        if tiles[y][x] == 'O' :
            score += 100*y + x

print(score)