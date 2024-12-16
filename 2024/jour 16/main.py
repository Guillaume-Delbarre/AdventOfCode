import heapq
import copy
# Exercice 1
data = open("2024/jour 16/input.txt", "r").read().split("\n")
data = [list(d) for d in data]

# Start pos :
for y in range(len(data)) :
    for x in range(len(data[y])) :
        if data[y][x] == 'S' :
            break
    else :
        continue
    break

direction = (1, 0)
p_deplacement = 1
p_rotation = 1000

seen = set()

h = []
heapq.heappush(h, (0, (x, y), direction))

while True :
    val, pos, dir = heapq.heappop(h)
    x, y = pos
    if data[y][x] == 'E' : break
    if (pos, dir) in seen :
        continue
    else :
        seen.add((pos, dir))
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
        if data[y+dy][x+dx] != '#' :
            if dir[0] == dx and dir[1] == dy :
                heapq.heappush(h, (val + p_deplacement, (x+dx, y+dy), dir))
            else :
                heapq.heappush(h, (val + p_deplacement + p_rotation, (x+dx, y+dy), (dx, dy)))

print(val, pos, dir)


# Exercice 2
data = open("2024/jour 16/exemple_input.txt", "r").read().split("\n")
data = [list(d) for d in data]

# Start pos :
for y in range(len(data)) :
    for x in range(len(data[y])) :
        if data[y][x] == 'S' :
            break
    else :
        continue
    break

direction = (1, 0)
p_deplacement = 1
p_rotation = 1000

seen = set()

h = []
heapq.heappush(h, (0, (x, y), direction, [(x, y)]))

final = []
trouve = False
min_val = -1
while len(h) > 0 :
    val, pos, dir, chemin = heapq.heappop(h)
    x, y = pos
    if trouve and val > min_val :
        continue
    if data[y][x] == 'E' : 
        heapq.heappush(final, (val, pos, dir, chemin))
        trouve = True
        min_val = val
        continue
    if (pos, dir) in seen :
        continue
    else :
        seen.add((pos, dir))
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
        if data[y+dy][x+dx] != '#' :
            if dir[0] == dx and dir[1] == dy :
                n_chemin = copy.deepcopy(chemin)
                n_chemin.append((x+dx, y+dy))
                heapq.heappush(h, (val + p_deplacement, (x+dx, y+dy), dir, n_chemin))
            else :
                n_chemin = copy.deepcopy(chemin)
                n_chemin.append((x+dx, y+dy))
                heapq.heappush(h, (val + p_deplacement + p_rotation, (x+dx, y+dy), (dx, dy), n_chemin))

che = set()
while len(final) > 0 :
    val, pos, _, chemin = heapq.heappop(final)
    if (2, 11) in chemin :
        print(val, min_val, pos, chemin)
    if data[pos[1]][pos[0]] == 'E' and val == min_val :
        for el in chemin :
            che.add(el)

print(len(che))

for y in range(len(data)) :
    li = []
    for x in range(len(data[0])) :
        if (x, y) in che :
            li.append('O')
        else :
            li.append(data[y][x])
    print("".join(li))
