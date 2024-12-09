# Exercice 1
data = open("2024/jour 9/exemple_input.txt", "r").read().split("\n")[0]

en_cours = "file"
id = 0
final = []
for n in data :
    if en_cours == "file" :
        final += [id]*int(n)
        id += 1
        en_cours = "free"
    elif en_cours == "free" :
        final += ['.']*int(n)
        en_cours = "file"

def get_last_index(array) :
    for i in range(len(array) - 1, -1, -1) :
        if array[i] != '.' :
            return i

for i in range(len(final)) :
    if final[i] == '.' :
        last_index = get_last_index(final)
        if last_index < i :
            break
        else :
            final[i] = final[last_index]
            final[last_index] = '.'

score = 0

for index, val in enumerate(final) :
    if val == '.' :
        break
    else :
        score += index*val

print(score)

# Exercice 2
data = open("2024/jour 9/input.txt", "r").read().split("\n")[0]

en_cours = "file"
id = 0
final = []
ids = []
for n in data :
    if en_cours == "file" :
        final += [id]*int(n)
        ids.append(n)
        id += 1
        en_cours = "free"
    elif en_cours == "free" :
        final += ['.']*int(n)
        en_cours = "file"

for val in range(len(ids) - 1, -1, -1) :
    taille = int(ids[val])
    en_cours = False
    t = 0
    trouve = False
    for i in range(len(final)) :
        if final[i] == val and not en_cours:
            break
        elif final[i] == '.' :
            if not en_cours :
                start_i = i
            t += 1
            en_cours = True
        elif en_cours and taille <= t :
            trouve = True
            break
        else :
            t = 0
            en_cours = False
    if trouve :
        final = ['.' if x == val else x for x in final]
        for i in range(start_i, start_i + taille) :
            final[i] = val

# print(final)

# 00992111777.44.333....5555.6666.....8888..

score = 0

for index, val in enumerate(final) :
    if val != '.' :
        score += index*val

print(score)