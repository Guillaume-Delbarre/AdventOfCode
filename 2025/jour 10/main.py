import ast
from collections import deque

# Exercice 1
data = open("2025/jour 10/input.txt", "r").read().split("\n")

def add_actions(actions:deque, buttons:list, etat:list, nb:int) -> deque :
    for button in buttons :
        actions.append((button, etat, nb))
    return actions

def press_button(button:list, etat: list) -> list :
    new_etat = [ind for ind in etat]
    for indicator in button :
        new_etat[indicator] = not new_etat[indicator]
    return new_etat

def is_equal(etat, cible) -> bool :
    if len(etat) != len(cible) : return False
    for i in range(len(etat)) :
        if etat[i] != cible[i] :
            return False
    return True


res = 0
for machine in data :
    parts = machine.split(" ")
    goal = [g == "#" for g in parts[0][1:-1]]
    joltage = parts[-1]
    buttons = [[bu] if type(bu) == int else bu for bu in [ast.literal_eval(b) for b in parts[1:-1]]]

    etat_start = [False]*len(goal)

    etats_seen = []

    found = False
    actions = add_actions(deque(), buttons, etat_start, 1)
    while not found :
        action, etat, nb = actions.popleft()
        #input(f"Nouvelle boucle avec action : {action}, nb : {nb}, etat : {etat}")
        new_etat = press_button(action, etat)
        if new_etat not in etats_seen :
            if is_equal(new_etat, goal) :
                print(f"OK pour la machine {machine} en {nb} operations")
                res += nb
                found = True
            else :
                actions = add_actions(actions, buttons, new_etat, nb + 1)
                etats_seen.append(new_etat)
print(res)