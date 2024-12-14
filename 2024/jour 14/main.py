import re
# Exercice 1
data = open("2024/jour 14/input.txt", "r").read().split("\n")

# top-left, top-right, bottom-left, bottom-right
score = [[0, 0], [0, 0]]
taille = (11, 7)
taille = (101, 103)
nb_mouvement = 100
for robot in data :
    robot_p, robot_v = robot.split(" ")
    re_p = re.search(r"p=(-{0,1}\d+),(-{0,1}\d+)", robot_p)
    re_v = re.search(r"v=(-{0,1}\d+),(-{0,1}\d+)", robot_v)
    px, py = list(map(int, re_p.groups()))
    vx, vy = list(map(int, re_v.groups()))

    px = px + nb_mouvement*vx
    py = py + nb_mouvement*vy

    px = px % taille[0]
    py = py % taille[1]

    if py < taille[1] // 2 :
        pos0 = 1
    elif py > taille[1] // 2:
        pos0 = 0
    else :
        continue

    if px < taille[0] // 2 :
        pos1 = 0
    elif px > taille[0] // 2:
        pos1 = 1
    else :
        continue

    score[pos0][pos1] += 1

print(score[0][1] * score[0][0] * score[1][1] * score[1][0])