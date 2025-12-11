from collections import deque

# Exercice 1
data = open("2025/jour 11/input.txt", "r").read().split("\n")
data = [el.split(": ") for el in data]

machines = {ma1 : ma2.split(" ") for ma1,ma2 in data}

res = 0

list_machine = deque()
list_machine.append(('svr', False, False))

while len(list_machine) > 0 :
    machine, dac, fft = list_machine.popleft()
    # print(f"machine : {machine}, dac : {dac}, fft : {fft}")
    if machine == 'out' :
        if dac and fft :
            res += 1
    else :
        for m in machines[machine] :
            if machine == 'dac' :
                list_machine.append((m, True, fft))
            elif machine == 'fft' :
                list_machine.append((m, dac, True))
            else :
                list_machine.append((m, dac, fft))
                

print(res)