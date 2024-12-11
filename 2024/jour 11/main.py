# Exercice 1
data = open("2024/jour 11/input.txt", "r").read().split(" ")
data = list(map(int, data))

nb_blink = 25
for i in range(nb_blink):
    new_data = []
    for d in data :
        if d == 0 :
            new_data.append(1)
        elif len(str(d)) % 2 == 0 :
            n_taille = int(len(str(d))/2)
            new_data.append(int(str(d)[:n_taille]))
            new_data.append(int(str(d)[n_taille:]))
        else :
            new_data.append(d * 2024)
    data = new_data

print(len(data))


# Exercice 1
data = open("2024/jour 11/input.txt", "r").read().split(" ")
data = list(map(int, data))

def get_nb_dans_n(val, n) :
    if n == 0 : return 1
    if val == 0 :
        return get_global(1, n-1)
    elif len(str(val)) % 2 == 0 :
        n_taille = int(len(str(val))/2)
        return get_global(int(str(val)[:n_taille]), n-1) + get_global(int(str(val)[n_taille:]), n-1)
    else :
        return get_global(val * 2024, n-1)

memoire = {}
def get_global(val, n) :
    if (val, n) in memoire.keys() :
        return memoire[(val, n)]
    else :
        ret = get_nb_dans_n(val, n)
        memoire[(val, n)] = ret
        return ret

nb_blink = 75
score = 0
for d in data :
    score += get_global(d, nb_blink)

print(score)