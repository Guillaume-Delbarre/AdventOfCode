# Exercice 1
rg, data = open("2024/jour 5/input.txt", "r").read().split("\n\n")
rg=[r.split('|') for r in rg.split("\n")]
data=[d.split(',') for d in data.split("\n")]


score = 0
for update in data :
    valid = True
    for i_pre in range(len(update)) :
        for i_sec in range(i_pre + 1,len(update)) :
            if not valid or [update[i_sec], update[i_pre]] in rg:
                valid = False
                break
    if valid :
        score += int(update[int((len(update))/2)])

print(score)


# Exercice 1
rg, data = open("2024/jour 5/input.txt", "r").read().split("\n\n")
rg=[r.split('|') for r in rg.split("\n")]
data=[d.split(',') for d in data.split("\n")]


score = 0
for update in data :
    valid = True
    for i_pre in range(len(update)) :
        for i_sec in range(i_pre + 1,len(update)) :
            if not valid or [update[i_sec], update[i_pre]] in rg:
                valid = False
                break
    if not valid :
        while not valid :
            valid=True
            for i_pre in range(len(update)) :
                for i_sec in range(i_pre + 1,len(update)) :
                    if [update[i_sec], update[i_pre]] in rg:
                        valid = False
                        t = update[i_sec]
                        update[i_sec] = update[i_pre]
                        update[i_pre] = t
        score += int(update[int((len(update))/2)])

print(score)
