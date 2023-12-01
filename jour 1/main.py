# Exercice 1
data = open("jour 1/input.txt", "r").read().split("\n")
#print(len(data))

somme = 0
for line in data :
    trouve = False
    for l in line :
        if l.isdigit() :
            if not trouve :
                premier = l
                trouve = True
            dernier = l
    somme += int(premier + dernier)

print(somme)


# Exercice 2
data = open("jour 1/input.txt", "r").read().split("\n")
#print(len(data))

chiffre = {"one": '1',
           "two": '2',
           "three": '3',
           "four": '4',
           "five": '5',
           "six": '6',
           "seven": '7',
           "eight": '8',
           "nine": '9'}

somme = 0
for line in data :
    trouve = False
    for index, l in enumerate(line) :
        if l.isdigit() :
            if not trouve :
                premier = l
                trouve = True
            dernier = l
        for substr in chiffre :
            if line[index:].startswith(substr) :
                if not trouve :
                    premier = chiffre[substr]
                    trouve = True
                dernier = chiffre[substr]
    somme += int(premier + dernier)

print(somme)