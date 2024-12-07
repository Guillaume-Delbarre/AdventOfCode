# Exercice 1
data = open("2024/jour 7/input.txt", "r").read().split("\n")
data = [[int(sli.split(": ")[0]), list(map(int, sli.split(": ")[1].split(" ")))] for sli in data]
#print(data)

# Cette fonction ne fonctionne pas parce qu'on peut faire 0*Nombre pour commencer ce qui peut retourner un faux positif
def calc_sol(res, prem, reste, eq) :
    # print(f"On regarde res:{res}, prem:{prem} et reste:{reste}, eq:{eq}")
    if len(reste) == 0 :
        if prem == res :
            print("C'est Valide")
            print(eq)
            return True
    else :
        if calc_sol(res, prem * reste[0], reste[1:], eq+["*"]) :
            # print(f"Solution res:{res}, prem:{prem} et reste:{reste}, eq:{eq}")
            print(f"* {reste[0]}")
            return True
        if calc_sol(res, prem + reste[0], reste[1:], eq+["+"]) :
            print(f"+ {reste[0]}")
            return True
        return False
    
def can_obtain(res, reste) :
    if len(reste) == 1 :
        return reste[0] == res
    if can_obtain(res, [reste[0] * reste[1]]+reste[2:]) : 
        return True
    if can_obtain(res, [reste[0] + reste[1]]+reste[2:]) : 
        return True
    return False

score = 0
for res, val in data :
    if can_obtain(res, val) :
        score += res

print(score)


# Exercice 1
data = open("2024/jour 7/input.txt", "r").read().split("\n")
data = [[int(sli.split(": ")[0]), list(map(int, sli.split(": ")[1].split(" ")))] for sli in data]
#print(data)

def can_obtain(res, reste) :
    if len(reste) == 1 :
        return reste[0] == res
    if can_obtain(res, [reste[0] * reste[1]]+reste[2:]) : 
        return True
    if can_obtain(res, [reste[0] + reste[1]]+reste[2:]) : 
        return True
    if can_obtain(res, [int(str(reste[0]) + str(reste[1]))]+reste[2:]) :
        return True
    return False

score = 0
for res, val in data :
    if can_obtain(res, val) :
        score += res

print(score)