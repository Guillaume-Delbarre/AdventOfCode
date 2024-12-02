from heapq import heappush, heappop
# Exercice 1
data = open("2023/jour 17/input.txt", "r").read().split('\n')
data = [[int(l) for l in line] for line in data]

points = [(0, 0, 0, 0, 0, 0)] # Current score / x / y / dir x / dir y / distance in that direction
seen = set()

trouve = False

while not trouve :
    score, x, y, dir_x, dir_y, dist = heappop(points)

    if (x, y) == (len(data[0])-1, len(data) - 1) :
        trouve = True
        break
    
    if (x, y, dir_x, dir_y, dist) not in seen : # On y est déjà allé on a déjà exploré les possibilitées
        seen.add((x, y, dir_x, dir_y, dist))

        for new_dir in [(0, 1), (0, -1), (1, 0), (-1, 0)] :
            if new_dir != (dir_x * -1, dir_y * -1) : # On ne fait pas demi-tour
                new_x = x + new_dir[0]
                new_y = y + new_dir[1]
                if new_x >= 0 and new_x < len(data[0]) and new_y >= 0 and new_y < len(data) : # On est bien dans la grille
                    if (dir_x, dir_y) == new_dir and dist < 3 : # On va dans la même direction mais pas plus de 3 fois
                        heappush(points, (score + data[new_y][new_x], new_x, new_y, new_dir[0], new_dir[1], dist + 1))
                    elif (dir_x, dir_y) != new_dir :
                        heappush(points, (score + data[new_y][new_x], new_x, new_y, new_dir[0], new_dir[1], 1))

print(score)