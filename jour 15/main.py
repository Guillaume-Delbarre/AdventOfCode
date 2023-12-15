# Exercice 1
data = open("jour 15/input.txt", "r").read().split(",")

# print(data)

score = 0
for mot in data :
    current_value = 0
    for lettre in mot :
        ascii = ord(lettre)
        current_value += ascii
        current_value *= 17
        current_value = current_value % 256
    score += current_value

print(score)


# Exercice 2
data = open("jour 15/input.txt", "r").read().split(",")

boites = {}

def get_ascii(mot) :
    current_value = 0
    for lettre in mot :
        ascii = ord(lettre)
        current_value += ascii
        current_value *= 17
        current_value = current_value % 256
    return current_value

for mot in data :
    val = None
    if "=" in mot :
        n_mot, val = mot.split('=')
    elif "-" in mot :
        n_mot = mot[:-1]
    ascii = get_ascii(n_mot)
    if ascii not in boites and val is not None:
        boites[ascii] = [[n_mot, val]]
    elif val is not None :
        index = [index for index in range(len(boites[ascii])) if boites[ascii][index][0] == n_mot]
        if len(index) > 0 :
            boites[ascii][index[0]] = [n_mot, val]
        else : 
            boites[ascii].append([n_mot, val])
    elif ascii in boites :
        index = [b for b in boites[ascii] if b[0] == n_mot]
        if len(index) > 0 :
            boites[ascii].remove(index[0])

score = 0
for box in boites.keys() :
    for index, focal in enumerate(boites[box]) :
        score += (box + 1) * (index + 1) * int(focal[1])

print(score)