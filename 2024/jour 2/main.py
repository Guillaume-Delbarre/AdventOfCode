# Exercice 1
data = open("2024/jour 2/input.txt", "r").read().split("\n")
#print(data)

data = [list(map(int, d.split(" "))) for d in data]

score = 0

for level in data :
    diffs = [level[i+1] - level[i] for i in range(len(level) - 1)]
    if max(list(map(abs, diffs))) < 4 and min(list(map(abs, diffs))) >= 1 and ((min(diffs) < 0 and max(diffs) < 0) or (min(diffs) > 0 and max(diffs) > 0)):
        score += 1

print(score)


# Exercice 1
data = open("2024/jour 2/input.txt", "r").read().split("\n")

data = [list(map(int, d.split(" "))) for d in data]

score = 0

for level in data :
    diffs = [level[i+1] - level[i] for i in range(len(level) - 1)]
    if max(list(map(abs, diffs))) < 4 and min(list(map(abs, diffs))) >= 1 and ((min(diffs) < 0 and max(diffs) < 0) or (min(diffs) > 0 and max(diffs) > 0)):
        score += 1
    else :
        for i in range(len(level)) :
            new_level = level[:i] + level[i+1:]
            diffs = [new_level[i+1] - new_level[i] for i in range(len(new_level) - 1)]
            if max(list(map(abs, diffs))) < 4 and min(list(map(abs, diffs))) >= 1 and ((min(diffs) < 0 and max(diffs) < 0) or (min(diffs) > 0 and max(diffs) > 0)):
                score += 1
                break

print(score)