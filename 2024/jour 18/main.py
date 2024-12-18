import heapq
import copy
# Exercice 1
data = open("2024/jour 18/input.txt", "r").read().split("\n")
data = [list(map(int, d.split(','))) for d in data]

taille = 71
nb_tombe = 1024
area = [['.' for _ in range(taille)] for _ in range(taille)]
for b_x, b_y in data[:nb_tombe] :
    area[b_y][b_x] = '#'

h = [(0, (0, 0))]
trouve = False
seen = set()
while not trouve :
    score, pos = heapq.heappop(h)
    x, y = pos
    # print(f"On traite {score, pos} et il reste {len(h)} element dans h")
    if pos in seen :
        continue
    else :
        seen.add(pos)
    if x == taille-1 and y == taille-1 :
        trouve = True
        break
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] :
        if x+dx >= 0 and x+dx < taille and y+dy >= 0 and y+dy < taille :
            if area[y+dy][x+dx] == '.' :
                heapq.heappush(h, (score+1, (x+dx, y+dy)))

print(score)

# Exercice 2
data = open("2024/jour 18/input.txt", "r").read().split("\n")
data = [list(map(int, d.split(','))) for d in data]

taille = 71
nb_tombe_min = 1024
nb_tombe_max = len(data)

while nb_tombe_min != nb_tombe_max :
    nb_tombe = nb_tombe_min +  int((nb_tombe_max - nb_tombe_min)/2)
    print(f"Nouveau test avec max:{nb_tombe_max} min:{nb_tombe_min} et nb:{nb_tombe}")
    area = [['.' for _ in range(taille)] for _ in range(taille)]
    for b_x, b_y in data[:nb_tombe] :
        area[b_y][b_x] = '#'

    h = [(0, (0, 0), [[0, 0]])]
    trouve = False
    seen = set()
    while not trouve and len(h) > 0:
        score, pos, che = heapq.heappop(h)
        x, y = pos
        # print(f"On traite {score, pos} et il reste {len(h)} element dans h")
        if pos in seen :
            continue
        else :
            seen.add(pos)
        if x == taille-1 and y == taille-1 :
            trouve = True
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] :
            if x+dx >= 0 and x+dx < taille and y+dy >= 0 and y+dy < taille :
                if area[y+dy][x+dx] == '.' :
                    c_che = copy.deepcopy(che)
                    c_che.append([x+dx, y+dy])
                    heapq.heappush(h, (score+1, (x+dx, y+dy), c_che))
    
    # Si on est bloqué -> Le max devient le courant
    if len(h) == 0 and not trouve:
        # print(f"Problème avec {nb_tombe} et {data[nb_tombe-1]}")
        nb_tombe_max = nb_tombe
    else :
        nb_tombe_min = nb_tombe
    nb_tombe += 1

# Exercice pas 100% fonctionnel car quand la différence est de 1 on peut boucler
    # -> Mais si on connait les deux valeurs sur lesquelles on boucle on peut savoir quelle ligne de l'input est la bonne et donc donner la réponse sur AOC