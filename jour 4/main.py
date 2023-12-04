# Exercice 1
data = open("jour 4/input.txt", "r").read().split("\n")
data = [line.split(": ")[1].split(" | ") for line in data]
data = [[list.split() for list in line] for line in data]

# print(data)

score = 0
for num_card, (gagnant, joue) in enumerate(data) :
    r = [1 for n in joue if n in gagnant]
    if len(r) > 0 :
        score += pow(2, len(r)-1)

print(score)



# Exercice 2
data = open("jour 4/input.txt", "r").read().split("\n")
data = [line.split(": ")[1].split(" | ") for line in data]
data = [[list.split() for list in line] for line in data]

# print(data)

copies = [1] * len(data)
for num_card, (gagnant, joue) in enumerate(data) :
    r = [copies[num_card] for n in joue if n in gagnant]
    for index, val in enumerate(r) :
        copies[num_card + index + 1] += val

print(sum(copies))