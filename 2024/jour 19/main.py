from functools import cache
# Exercice 1
towels, goals = open("2024/jour 19/input.txt", "r").read().split("\n\n")
towels = towels.split(', ')
goals = goals.split('\n')

@cache
def possible_towel(goal, towels=towels) :
    if goal == '' : return True
    for towel in towels :
        if len(goal) >= len(towel) and goal[:len(towel)] == towel :
            if possible_towel(goal[len(towel):]) : return True
    return False

score = 0
for goal in goals :
    if possible_towel(goal) :
        score += 1

print(score)


# Exercice 2
towels, goals = open("2024/jour 19/input.txt", "r").read().split("\n\n")
towels = towels.split(', ')
goals = goals.split('\n')

@cache
def nb_possible_towel(goal, towels=towels) :
    if goal == '' : return 1
    val = 0
    for towel in towels :
        if len(goal) >= len(towel) and goal[:len(towel)] == towel :
            val += nb_possible_towel(goal[len(towel):])
    return val

score = 0
for goal in goals :
    score += nb_possible_towel(goal)

print(score)