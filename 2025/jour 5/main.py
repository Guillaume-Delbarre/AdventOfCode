# Exercice 1
data = open("2025/jour 5/input.txt", "r").read().split("\n\n")

ranges = [[int(ran.split("-")[0]), int(ran.split("-")[1])] for ran in data[0].split('\n')]
ranges = sorted(ranges, key=lambda x: x[0])
ingredient = [int(i) for i in data[1].split('\n')]

res = 0

for i in ingredient :
    # input(f"nouveau ingredient : {i}")
    for ra in ranges :
        # print(f"etude de {ra} pour {i}")
        if ra[0] > i :
            # print(f"ko pour {i} dans {ra}")
            break
        else :
            if ra[1] >= i :
                res += 1
                # print(f"ok pour {i} dans {ra}")
                break

print(res)


# Exercice 2
data = open("2025/jour 5/input.txt", "r").read().split("\n\n")

ranges = [[int(ran.split("-")[0]), int(ran.split("-")[1])] for ran in data[0].split('\n')]
ranges = sorted(ranges, key=lambda x: x[0])

ingredient = [int(i) for i in data[1].split('\n')]

new_ranges = [ranges[0]]
for i in range(1, len(ranges)) :
    last = new_ranges[-1]
    if ranges[i][0] <= last[1] :
        if last[1] < ranges[i][1] :
            new_ranges[-1][1] = ranges[i][1]
    else :
        new_ranges.append(ranges[i])

res = 0
for r in new_ranges :
    res += r[1] - r[0] + 1

print(res)