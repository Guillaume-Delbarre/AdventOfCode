# Exercice 1
data = open("2025/jour 1/input.txt", "r").read().split("\n")
#print(data)

pos = 50
nb0 = 0

for line in data :
    direction = line[0]
    distance = int(line[1:])
    if direction == "L" :
        pos = (pos - distance) % 100
    elif direction == "R" :
        pos = (pos + distance) % 100
    else :
        print(f"ERREUR : dans la ligne : {line}")
        break

    if pos == 0 :
        nb0 += 1

print(nb0)


# Exercice 2
data = open("2025/jour 1/input.txt", "r").read().split("\n")
#print(data)

pos = 50
nb0 = 0

for line in data :
    direction = line[0]
    distance = int(line[1:])
    if direction == "L" :
        distance = distance*-1

    while abs(distance) > 0 :
        if abs(distance) >= 100 :
            nb0 += 1
            distance = distance + 100 if direction == "L" else distance - 100
        else :
            new_pos = (pos + distance) % 100
            if ((pos + distance) <= 0 or (pos + distance) >= 100) and pos != 0:
                nb0 += 1
            # input(f"line : {line}, pos : {pos}, new_pos : {new_pos}, nb0 : {nb0}, distance : {distance}")
            pos = new_pos
            break
    

    
#    print(new_pos // 100, f"new_pos : {new_pos}")
#    nb0 += abs(new_pos // 100)
#    
#    if pos == 0 and new_pos < 0 :
#        nb0 -= 1
#    pos = new_pos % 100
#
#    if new_pos == 0 :
#        nb0 += 1
#    input(f"line : {line}, pos : {pos}, nb0 : {nb0}")

print(nb0)