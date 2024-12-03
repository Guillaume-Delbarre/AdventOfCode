import re

# Exercice 1
data = open("2024/jour 3/input.txt", "r").read()
#print(data)

muls = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", data)

score = 0
for mul in muls :
    n1, n2 = re.findall(r"\d+", mul)
    score += int(n1)*int(n2)

print(score)

# Exercice 2
data = open("2024/jour 3/input.txt", "r").read()
#print(data)

muls = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)", data)

score = 0
actual = "do"
for mul in muls :
    if mul == "do()" :
        actual = "do"
    elif mul == "don't()" :
        actual = "dont"
    else :
        if actual == "do" :
            n1, n2 = re.findall(r"\d+", mul)
            score += int(n1)*int(n2)

print(score)