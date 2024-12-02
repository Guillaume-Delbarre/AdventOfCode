# Exercice 1
data = open("2023/jour 18/exemple_input.txt", "r").read().split('\n')
data = [line.split() for line in data]

# print(data)

points = [(0, 0)]
actuel = (0, 0)

for line in data :
    dir, dist, col = line
    
    if dir == 'U' :
        coord_dir = (0, -1)
    elif dir == 'D' :
        coord_dir = (0, 1)
    elif dir == 'R' :
        coord_dir = (1, 0)
    elif dir == 'L' :
        coord_dir = (-1, 0)

    for i in range(1, int(dist) + 1) :
        points.append((actuel[0] + i*coord_dir[0], actuel[1] + i*coord_dir[1]))
    
    actuel = (actuel[0] + int(dist)*coord_dir[0], actuel[1] + int(dist)*coord_dir[1])

# print(points)
max_x = max(points, key=lambda x : x[0])
min_x = min(points, key=lambda x : x[0])
min_y = min(points, key=lambda x : x[1])
max_y = max(points, key=lambda x : x[1])

ext = []

from collections import deque
to_see = deque()

def analyse_points(x, y) :
    if min_x[0] <= x <= max_x[0] and min_y[1] <= y <= max_y[1] :
        if (x, y) not in points and (x, y) not in ext:
            ext.append((x, y))
            to_see.append((x, y + 1))
            to_see.append((x, y - 1))
            to_see.append((x + 1, y))
            to_see.append((x - 1, y))


# Ajout des nouveaux points à l'interieur
for x in range(min_x[0], max_x[0]+1) :
    for y in [min_y[1], max_y[1]] :
        to_see.append((x, y))

for y in range(min_y[1], max_y[1]+1) :
    for x in [min_x[0], max_x[0]] :
        to_see.append((x, y))

while to_see :
    x, y = to_see.pop()
    analyse_points(x, y)


print((max_x[0] - min_x[0] + 1)*(max_y[1] - min_y[1] + 1) - len(ext))


# Exercice 2
data = open("2023/jour 18/input.txt", "r").read().split('\n')
data = [line.split() for line in data]

# print(data)

points = [(0, 0)]
actuel = (0, 0)

for line in data :
    _, _, col = line
    col = col[2:-1]
    dir = col[-1]
    dist = int(col[:-1], 16)
    
    if dir == '3' :
        coord_dir = (0, -1)
    elif dir == '1' :
        coord_dir = (0, 1)
    elif dir == '0' :
        coord_dir = (1, 0)
    elif dir == '2' :
        coord_dir = (-1, 0)

    for i in range(1, int(dist) + 1) :
        points.append((actuel[0] + i*coord_dir[0], actuel[1] + i*coord_dir[1]))
    
    actuel = (actuel[0] + int(dist)*coord_dir[0], actuel[1] + int(dist)*coord_dir[1])


# Calcul d'une aire à partir des sommets
s = [points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1] for i in range(len(points)-1)]
s.append(points[len(points)-1][0]*points[0][1] - points[0][0]*points[len(points)-1][1])
a = 0.5 * abs(sum(s))

print(int(a))
print(int(0.5*len(points)))
print(int(a) + int(0.5*len(points)))
print(int(a) + int(0.5*len(points)) + 1)
