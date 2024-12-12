# Exercice 1
data = open("2024/jour 12/input.txt", "r").read().split("\n")
data = [list(d) for d in data]

done = [[False for _ in range(len(data[0]))] for _ in range(len(data))]

def get_aire_perim(val, r_start, c_start) :
    if data[r_start][c_start] != val : return 0, 0
    if done[r_start][c_start] : return 0, 0
    done[r_start][c_start] = True
    a, p = 1, 0
    for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
        r = r_start + dr
        c = c_start + dc
        if r >= 0 and r < len(data) and c >= 0 and c < len(data[0]) :
            if data[r][c] != val :
                p += 1
            elif not done[r][c] and data[r][c] == val :
                n_a, n_p = get_aire_perim(val, r, c)
                a += n_a
                p += n_p
        else : 
            p += 1
    return (a, p)

score = 0
for r in range(len(data)) :
    for c in range(len(data[0])) :
        a, p = get_aire_perim(data[r][c], r, c)
        score += a*p
print(score)

# Exercice 2
data = open("2024/jour 12/input.txt", "r").read().split("\n")
data = [list(d) for d in data]

done = [[False for _ in range(len(data[0]))] for _ in range(len(data))]

def get_aire_perim(val, r_start, c_start) :
    if data[r_start][c_start] != val : return 0, 0
    if done[r_start][c_start] : return 0, 0
    done[r_start][c_start] = True
    a, p = 1, []
    for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
        r = r_start + dr
        c = c_start + dc
        if r >= 0 and r < len(data) and c >= 0 and c < len(data[0]) :
            if data[r][c] != val :
                p.append((r_start, c_start, dr, dc))
            elif not done[r][c] and data[r][c] == val :
                n_a, n_p = get_aire_perim(val, r, c)
                a += n_a
                p += n_p
        else : 
            p.append((r_start, c_start, dr, dc))
    return (a, p)

score = 0
for r in range(len(data)) :
    for c in range(len(data[0])) :
        a, p = get_aire_perim(data[r][c], r, c)
        if a != 0 :
            p_sco = 4
            sup = sorted([x for x in p if x[2] == -1])
            for ligne in range(1, len(sup)) :
                if sup[ligne - 1][0] != sup[ligne][0] :
                    p_sco+=1
                elif sup[ligne - 1][1]+1 != sup[ligne][1] :
                    p_sco+=1
            inf = sorted([x for x in p if x[2] == 1])
            for ligne in range(1, len(inf)) :
                if inf[ligne - 1][0] != inf[ligne][0] :
                    p_sco+=1
                elif inf[ligne - 1][1]+1 != inf[ligne][1] :
                    p_sco+=1
            droite = sorted([x for x in p if x[3] == 1], key = lambda x : (x[1], x[0]))
            for ligne in range(1, len(droite)) :
                if droite[ligne - 1][1] != droite[ligne][1] :
                    p_sco+=1
                elif droite[ligne - 1][0]+1 != droite[ligne][0] :
                    p_sco+=1
            gauche = sorted([x for x in p if x[3] == -1], key = lambda x : (x[1], x[0]))
            for ligne in range(1, len(gauche)) :
                if gauche[ligne - 1][1] != gauche[ligne][1] :
                    p_sco+=1
                elif gauche[ligne - 1][0]+1 != gauche[ligne][0] :
                    p_sco+=1
            score += a * p_sco
print(score)