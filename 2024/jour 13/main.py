import re
from math import isclose
# Exercice 1
data = open("2024/jour 13/input.txt", "r").read().split("\n\n")


# Récupération des infos :
machines=[]
for machine in data :
    a, b, p = machine.split("\n")
    val_a = re.search(r".*X\+(\d+).*Y\+(\d+)", a)
    val_b = re.search(r".*X\+(\d+).*Y\+(\d+)", b)
    val_p = re.search(r".*X=(\d+).*Y=(\d+)", p)
    machines.append([val_a.groups(), val_b.groups(), val_p.groups()])

score = 0
for a, b, p in machines :
    for nb_a in range(101) :
        nb_b = (int(p[1]) - int(a[1]) * nb_a) / int(b[1])
        val_trouve = int(a[0]) * nb_a + int(b[0]) * nb_b
        real = int(p[0])
        if val_trouve == real :
            score += int(nb_b) + 3*nb_a
            break
print(score)


# Exercice 1
data = open("2024/jour 13/input.txt", "r").read().split("\n\n")

# Récupération des infos :
machines=[]
for machine in data :
    a, b, p = machine.split("\n")
    val_a = re.search(r".*X\+(\d+).*Y\+(\d+)", a)
    val_b = re.search(r".*X\+(\d+).*Y\+(\d+)", b)
    val_p = re.search(r".*X=(\d+).*Y=(\d+)", p)
    machines.append([val_a.groups(), val_b.groups(), val_p.groups()])

score = 0
for a, b, p in machines :
    num = int(p[0])+10000000000000 - (int(b[0])*(int(p[1])+10000000000000)) / int(b[1])
    denom = int(a[0]) - (int(b[0])*int(a[1]))/int(b[1])
    tot = num/denom
    n_b = (int(p[1])+10000000000000 - (int(a[1])*tot))/int(b[1])
    # print(f"on a tot={tot} et b={n_b}")
    if tot-float(int(tot))<1e-5 and n_b-float(int(n_b))<1e-5:
        print(f"cela fonctionne avec a={tot}")
        score += int(n_b) + 3*int(tot)
print(score)


# 155949902316829
# 53567505831494