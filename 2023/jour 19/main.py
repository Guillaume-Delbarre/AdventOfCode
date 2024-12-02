# Exercice 1
data = open("2023/jour 19/input.txt", "r").read().split('\n\n')

workflows = data[0].split('\n')
workflows = [line.split('{') for line in workflows]
workflows = {name : [s for s in k[:-1].split(',')] for name, k in workflows }



ratings = data[1].split('\n')
ratings = [[ra for ra in line[1:-1].split(',')] for line in ratings]
ratings = [[l.split('=') for l in line] for line in ratings]

# print(ratings)
# print(workflows)


score = 0
pos = {'x':0, 'm':1, 'a':2, 's':3}

for r in ratings :
    current = 'in'
    while current not in 'AR' :
        for w in workflows[current] :
            if w[0] in 'xmas' and w[1] in '<>':
                name = w[0]
                sign = w[1]
                val, des = w[2:].split(':')
                if (sign == '<' and int(r[pos[name]][1]) < int(val)) or (sign == '>' and int(r[pos[name]][1]) > int(val)) :
                    current = des
                    break
            else :
                current = w
    if current == 'A' :
        score += sum([int(x[1]) for x in r])

print(score)


# Exercice 2
from collections import deque
import copy
import math
data = open("2023/jour 19/input.txt", "r").read().split('\n\n')

workflows = data[0].split('\n')
workflows = [line.split('{') for line in workflows]
workflows = {name : [s for s in k[:-1].split(',')] for name, k in workflows}

vals = deque()
vals.append(['in', {"x" : [1, 4000], "m" : [1, 4000], "a" : [1, 4000], "s" : [1, 4000]}])

score = 0
while vals :
    current, values = vals.pop()

    if current in 'RA' :
        if current == 'A' :
            score += math.prod([x[1] - x[0] + 1 for x in values.values()])
            # print(f"On rajoute les données de {current, values}")
        continue

    for w in workflows[current] :
        if w[0] in 'xmas' and w[1] in '<>':
            name = w[0]
            sign = w[1]
            val, des = w[2:].split(':')
            # print(f"\nworkfllow = {w}")
            if int(val) in range(values[name][0], values[name][1] + 1) :
                d1 = copy.deepcopy(values)
                d2 = copy.deepcopy(values)
                # print(f"On gère {values}")
                if sign == "<" :
                    d1[name] = [d1[name][0], int(val)-1]
                    values[name] = [int(val), values[name][1]]
                    vals.append([des, d1])
                    # vals.append([current, d2])
                    # print(f"envoi de {[des, d1]} et on garde {values}")
                elif sign == ">" :
                    values[name] = [values[name][0], int(val)]
                    d2[name] = [int(val)+1, d2[name][1]]
                    # vals.append([current, d1])
                    # print(f"envoi de {[des, d2]} et on garde {values}")
                    vals.append([des, d2])
        else :
            vals.append([w, values])

print(score)