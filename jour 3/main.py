# Exercice 1
data = open("jour 3/input.txt", "r").read().split("\n")
data = [[char for char in line] for line in data]

score = 0
for index_ligne, ligne in enumerate(data) :
    chiffre_en_cours = False
    chiffre_valide = False
    chiffre = ''
    for index_col, char in enumerate(ligne) :
        if char.isdigit() :
            if chiffre_en_cours :
                chiffre += char
            else :
                chiffre = char
            chiffre_en_cours = True
            for e in [(-1,-1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)] :
                new_ligne = index_ligne + e[0]
                new_col = index_col + e[1]
                if new_ligne > 0 and new_ligne < len(data) and new_col > 0 and new_col < len(data[0]) :
                    if not data[new_ligne][new_col].isdigit() and data[new_ligne][new_col] != '.' :
                        chiffre_valide = True
        else :
            if chiffre_en_cours and chiffre_valide :
                score += int(chiffre)
            chiffre_en_cours = False
            chiffre_valide = False
    # Cas où un chiffre termine la ligne :
    if chiffre_en_cours and chiffre_valide :
        score += int(chiffre)

print(score)


# Exercice 2
data = open("jour 3/input.txt", "r").read().split("\n")
data = [[char for char in line] for line in data]

gears = {}
for index_ligne, ligne in enumerate(data) :
    chiffre_en_cours = False
    chiffre_gear = False
    chiffre = ''
    for index_col, char in enumerate(ligne) :
        if char.isdigit() :
            if chiffre_en_cours :
                chiffre += char
            else :
                chiffre = char
            chiffre_en_cours = True
            for e in [(-1,-1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)] :
                new_ligne = index_ligne + e[0]
                new_col = index_col + e[1]
                if new_ligne > 0 and new_ligne < len(data) and new_col > 0 and new_col < len(data[0]) :
                    if  data[new_ligne][new_col] == '*' :
                        chiffre_gear = True
                        gear_en_cours = (new_ligne, new_col)
        else :
            if chiffre_en_cours and chiffre_gear :
                if gear_en_cours in gears.keys() :
                    gears[gear_en_cours].append(int(chiffre))
                else :
                    gears[gear_en_cours] = [int(chiffre)]
            chiffre_en_cours = False
            chiffre_gear = False
    # Cas où un chiffre termine la ligne :
    if chiffre_en_cours and chiffre_gear :
        if gear_en_cours in gears.keys() :
            gears[gear_en_cours].append(int(chiffre))
        else :
            gears[gear_en_cours] = [int(chiffre)]

print(sum([k[0]*k[1] for k in gears.values() if len(k) == 2]))