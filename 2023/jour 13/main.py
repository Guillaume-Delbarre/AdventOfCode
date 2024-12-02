# Exercice 1
data = open("2023/jour 13/input.txt", "r").read().split("\n\n")
data = [block.split("\n") for block in data]

# print(data)

res = []
for block in data :
    # Récupération des paire verticales
    for i in range(1, len(block[0])) :
        col1 = [block[l][i - 1] for l in range(len(block))]
        col2 = [block[l][i] for l in range(len(block))]

        eg = [col1[index] == col2[index] for index in range(len(block))]
        if all(eg) :
            sep = 1
            valid = True
            while i - sep > 0 and i + sep < len(block[0]) :
                col1 = [block[l][i - 1 - sep] for l in range(len(block))]
                col2 = [block[l][i + sep] for l in range(len(block))]
                sep += 1
                if not all([col1[index] == col2[index] for index in range(len(block))]) :
                    valid = False
                    break
            if valid :
                res.append(i)

    # Récupération des paire horizontales
    for i in range(1, len(block)) :
        col1 = [block[i - 1][l] for l in range(len(block[0]))]
        col2 = [block[i][l] for l in range(len(block[0]))]

        eg = [col1[index] == col2[index] for index in range(len(block[0]))]
        if all(eg) :
            sep = 1
            valid = True
            while i - sep > 0 and i + sep < len(block) :
                col1 = [block[i - 1 - sep][l] for l in range(len(block[0]))]
                col2 = [block[i + sep][l] for l in range(len(block[0]))]
                sep += 1
                if not all([col1[index] == col2[index] for index in range(len(block[0]))]) :
                    valid = False
                    break
            if valid :
                res.append(100 * i)

print(sum(res))


# Exercice 2
data = open("2023/jour 13/input.txt", "r").read().split("\n\n")
data = [block.split("\n") for block in data]

# print(data)

res = []
for block in data :
    # Récupération des paire verticales
    for i in range(1, len(block[0])) :
        col1 = [block[l][i - 1] for l in range(len(block))]
        col2 = [block[l][i] for l in range(len(block))]

        eg = [0 if col1[index] == col2[index] else 1 for index in range(len(block))]
        if sum(eg) in [0, 1] :
            sep = 1
            valid = True
            diff = sum(eg)
            while i - sep > 0 and i + sep < len(block[0]) :
                col1 = [block[l][i - 1 - sep] for l in range(len(block))]
                col2 = [block[l][i + sep] for l in range(len(block))]
                sep += 1
                diff += sum([0 if col1[index] == col2[index] else 1 for index in range(len(block))])
                if diff > 1 :
                    valid = False
                    break
            if valid and diff == 1:
                res.append(i)

    # Récupération des paire horizontales
    for i in range(1, len(block)) :
        col1 = [block[i - 1][l] for l in range(len(block[0]))]
        col2 = [block[i][l] for l in range(len(block[0]))]

        eg = [0 if col1[index] == col2[index] else 1 for index in range(len(block[0]))]
        if sum(eg) in [0, 1] :
            sep = 1
            valid = True
            diff = sum(eg)
            while i - sep > 0 and i + sep < len(block) :
                col1 = [block[i - 1 - sep][l] for l in range(len(block[0]))]
                col2 = [block[i + sep][l] for l in range(len(block[0]))]
                sep += 1
                diff += sum([0 if col1[index] == col2[index] else 1 for index in range(len(block[0]))])
                if diff > 1 :
                    valid = False
                    break
            if valid and diff == 1 :
                res.append(100 * i)

print(sum(res))