# Exercice 1
data = open("jour 9/input.txt", "r").read().split("\n")
data = [line.split() for line in data]

score = 0
for ligne in data :
    ligne = [[int(c) for c in ligne]]
    while not all([i == 0 for i in ligne[-1]]) :
        ligne.append([])
        for index in range(1, len(ligne[-2])) :
            ligne[-1].append(ligne[-2][index] - ligne[-2][index - 1])

    ligne[-1].append(0)
    for hauteur in range(len(ligne)-2, -1, -1) :
        ligne[hauteur].append(ligne[hauteur][-1] + ligne[hauteur + 1][-1])

    score += ligne[0][-1]

print(score)


# Exercice 2
data = open("jour 9/input.txt", "r").read().split("\n")
data = [line.split() for line in data]

score = 0
for ligne in data :
    ligne = [[int(c) for c in ligne]]
    while not all([i == 0 for i in ligne[-1]]) :
        ligne.append([])
        for index in range(1, len(ligne[-2])) :
            ligne[-1].append(ligne[-2][index] - ligne[-2][index - 1])

    ligne[-1].append(0)
    for hauteur in range(len(ligne)-2, -1, -1) :
        ligne[hauteur].append(ligne[hauteur][0] - ligne[hauteur + 1][-1])

    score += ligne[0][-1]

print(score)