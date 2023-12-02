# Exercice 1

data = open("jour 2/input.txt", "r").read().split("\n")
data = [line.split(":") for line in data]
data = list(map(lambda x : [x[0], x[1].split(";")], data))
data = [[game, [coul.split(",") for coul in action]] for game, action in data]
data = [[game, [[pioche.strip() for pioche in partie] for partie in action]] for game, action in data]

#print(data)
#print(data[0])

possibility = {"red": 12, "green": 13, "blue": 14}
score = 0
for game, action in data :
    valide = True
    for pioche in action :
        for couleur in pioche :
            c = couleur.split()
            if int(c[0]) > possibility[c[1]] :
                valide = False
                break
    if valide :
        score += int(game.split()[1])

print(score)



# Exercice 2
import math
data = open("jour 2/input.txt", "r").read().split("\n")
data = [line.split(":") for line in data]
data = list(map(lambda x : [x[0], x[1].split(";")], data))
data = [[game, [coul.split(",") for coul in action]] for game, action in data]
data = [[game, [[pioche.strip() for pioche in partie] for partie in action]] for game, action in data]

#print(data)
#print(data[0])

score = 0
for game, action in data :
    # red / green / blue
    min = {"red": 0, "green": 0, "blue": 0}
    for pioche in action :
        for couleur in pioche :
            c = couleur.split()
            if int(c[0]) > min[c[1]] :
                min[c[1]] = int(c[0])
    score += math.prod(list(min.values()))

print(score)