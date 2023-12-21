# Exercice 1
data = open("jour 21/input.txt", "r").read().split('\n')

for index, line in enumerate(data) :
    if 'S' in line :
        coord_s = (line.index('S'), index)

print(coord_s)

cases = {0 : [coord_s]}
for step in range(64) :
    cases[step + 1] = []
    for case_x, case_y in cases[step] :
        for dir_x, dir_y in [(0, 1), (0, -1), (-1, 0), (1, 0)] :
            if 0 <= case_x + dir_x < len(data[0]) and 0 <= case_y + dir_y < len(data) :
                if data[case_y + dir_y][case_x + dir_x] in '.S' and (case_x + dir_x, case_y + dir_y) not in cases[step + 1] :
                    cases[step + 1].append((case_x + dir_x, case_y + dir_y))

print(len(cases[64]))