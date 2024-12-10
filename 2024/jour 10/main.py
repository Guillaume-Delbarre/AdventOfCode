# Exercice 1
data = open("2024/jour 10/input.txt", "r").read().split("\n")
data = [list(map(int, list(d))) for d in data]

# Trouver les départs
dep = []
for row in range(len(data)) :
    for col in range(len(data[0])) :
        if data[row][col] == 0 :
            dep.append((row, col))

def get_pos_access(r, c, val, array) :
    ret = []
    if val == 9 : return [(r, c)]
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
        if r + dr >= 0 and r + dr < len(array) and c + dc >= 0 and c + dc < len(array[0]) :
            n_val = array[r+dr][c+dc]
            if n_val == val + 1 :
                ret += get_pos_access(r+dr, c+dc, n_val, array)
    return ret

# Calcul du score
score = 0
for row_dep, col_dep in dep :
    score += len(set(get_pos_access(row_dep, col_dep, 0, data)))

print(score)


# Exercice 2
data = open("2024/jour 10/input.txt", "r").read().split("\n")
data = [list(map(int, list(d))) for d in data]

# Trouver les départs
dep = []
for row in range(len(data)) :
    for col in range(len(data[0])) :
        if data[row][col] == 0 :
            dep.append((row, col))

def get_pos_access(r, c, val, array) :
    ret = []
    if val == 9 : return [(r, c)]
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
        if r + dr >= 0 and r + dr < len(array) and c + dc >= 0 and c + dc < len(array[0]) :
            n_val = array[r+dr][c+dc]
            if n_val == val + 1 :
                ret += get_pos_access(r+dr, c+dc, n_val, array)
    return ret

# Calcul du score
score = 0
for row_dep, col_dep in dep :
    score += len(get_pos_access(row_dep, col_dep, 0, data))

print(score)