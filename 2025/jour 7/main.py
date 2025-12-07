# Exercice 1
data = open("2025/jour 7/input.txt", "r").read().split("\n")

largeur = len(data[0])
position = [data[0].find("S")]
split = 0

for line in data[1:] :
    # input(f"Nouvelle ligne : {line}\nLes positions sont {position}")
    split_done = []
    new_positions = []
    for pos in position :
        # print(f"Analyse de la position {pos} pour la ligne : {line}")
        if line[pos] == "^" :
            # print(f"split")
            if pos not in split_done :
                # print(f"Nouveau split")
                split_done.append(pos)
                split += 1

            if pos - 1 >= 0 and pos - 1 not in new_positions :
                new_positions.append(pos-1)
            if pos + 1 < largeur and pos + 1 not in new_positions :
                new_positions.append(pos+1)
        else :
            new_positions.append(pos)
    position = new_positions
            
print(split)



# Exercice 2
data = open("2025/jour 7/input.txt", "r").read().split("\n")

largeur = len(data[0])
position = [data[0].find("S")]
paths = 0
dict_nb_path = {}

def get_nb_path(position, hauteur) -> int :
    # input(f"get_nb_path avec position = {position} et hauteur = {hauteur}")
    # print(f"Vision du dictionnaire : {dict_nb_path}")
    # print(dict_nb_path.keys())
    if (position, hauteur) in dict_nb_path :
        return dict_nb_path[(position, hauteur)]
    else :
        # print("On est dans le else")
        new_val = 0
        if position - 1 >= 0 :
            # print(f"position - 1 : {position - 1}")
            trouve = False
            for i in range(hauteur+1, len(data)) :
                if trouve : break
                if data[i][position - 1] == "^" :
                    new_val += get_nb_path(position - 1, i)
                    trouve = True
            if not trouve : new_val+=1
        if position + 1 < largeur :
            # print(f"position + 1 : {position + 1}")
            trouve = False
            for i in range(hauteur+1, len(data)) :
                if trouve : break
                if data[i][position + 1] == "^" :
                    new_val += get_nb_path(position + 1, i)
                    trouve = True
            if not trouve : new_val+=1
        # print(f"On a trouve {new_val} chemins")
        dict_nb_path[(position, hauteur)] = new_val
        return new_val


print(get_nb_path(position[0], 2))