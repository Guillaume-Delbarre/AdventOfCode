# Exercice 1
data = open("2025/jour 9/input.txt", "r").read().split("\n")

corners = [[int(cor.split(",")[0]), int(cor.split(",")[1])] for cor in data]

max_area = 0

for i in range(len(corners)) :
    for j in range(i+1, len(corners)) :
        area = (1+abs(corners[i][0] - corners[j][0])) * (1+abs(corners[i][1] - corners[j][1]))
        if area > max_area :
            max_area = area

print(max_area)