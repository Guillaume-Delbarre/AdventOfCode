# Exercice 1
data = open("2024/jour 1/input.txt", "r").read().split("\n")
#print(data)

gauche = []
droite = []

for ligne in data :
    g, d = ligne.split("   ")
    gauche.append(g)
    droite.append(d)

gauche.sort()
droite.sort()

somme = 0
for i in range(len(data)) :
    somme += abs(int(gauche[i]) - int(droite[i]))

print(somme)


# Exercice 2
data = open("2024/jour 1/input.txt", "r").read().split("\n")

gauche = []
droite = []

for ligne in data :
    g, d = ligne.split("   ")
    gauche.append(g)
    droite.append(d)

d = {}

for el in droite :
    if el in d.keys() :
        d[el] += 1
    else :
        d[el] = 1

somme = 0

for el in gauche :
    if el in d.keys() :
        somme += int(el) * d[el]

print(somme)