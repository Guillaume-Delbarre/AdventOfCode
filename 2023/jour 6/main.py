# Exercice 1
data = open("2023/jour 6/exemple_input.txt", "r").read().split("\n")
data = [line.split() for line in data]

# print(data)

score = 1
for race in range(1, len(data[0])) :
    distances_made = []
    count = 0
    for second_hold in range(int(data[0][race]) + 1) :
        distances_made.append(second_hold * (int(data[0][race]) - second_hold))
    for distance in distances_made :
        if distance > int(data[1][race]) :
            count += 1
    score *= count

print(score)


# Exercice 2
data = open("2023/jour 6/input.txt", "r").read().split("\n")
data = [line.split() for line in data]

time = int("".join(data[0][1:]))
distance = int("".join(data[1][1:]))

print(time, distance)

count = 0
for second_hold in range(time + 1) :
    distance_made = second_hold * (time - second_hold)
    if distance_made > distance :
        count += 1
print(count)