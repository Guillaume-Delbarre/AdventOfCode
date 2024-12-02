# Exercice 1
from collections import deque
data = open("2023/jour 20/input.txt", "r").read().split('\n')

modules = {}
conjunction = set()

for module in data :
    name, output = module.split(' -> ')
    if name != 'broadcaster' :
        if name[0] == '&' :
            modules[name[1:]] = [name[0], output.split(', '), {}]
            conjunction.add(name[1:])
        elif name[0] == '%' :
            modules[name[1:]] = [name[0], output.split(', '), False]
    else :
        modules['broadcaster'] = ['broadcaster', output.split(', ')]

for name, output in modules.items() :
    for n in output[1] :
        if n in conjunction :
            modules[n][2][name] = False

stack = deque()

def all_flip_flop_off(di) :
    for name, _ in di.items() :
        if di[name][0] == '%' :
            if di[name][2] :
                return False
    return True

send = [0, 0]

for p in range(1000) :
    stack.append(('broadcaster', False, ''))
    send[1] += 1

    while stack :
        name, pulse, origin = stack.popleft()

        if name not in list(modules.keys()) :
            # if not stack and not all_flip_flop_off(modules):
            #     print(f"module : {modules}")
            #     stack.append(('broadcaster', False, ''))
            #     send[1] += 1
            continue

        if modules[name][0] == 'broadcaster' :
            for module in modules[name][1] :
                stack.append((module, pulse, name))
                send[0 if pulse else 1] += 1
        elif modules[name][0] == '&' :
            modules[name][2][origin] = pulse
            output = all(list(modules[name][2].values()))
            for module in modules[name][1] :
                stack.append((module, not output, name))
                send[0 if not output else 1] += 1
        elif modules[name][0] == '%' and not pulse :
            modules[name][2] = not modules[name][2]
            for module in modules[name][1] :
                stack.append((module, modules[name][2], name))
                send[0 if modules[name][2] else 1] += 1

print(send[0] * send[1])


# Exercice 2
data = open("2023/jour 20/input.txt", "r").read().split('\n')

modules = {}
conjunction = set()

for module in data :
    name, output = module.split(' -> ')
    if name != 'broadcaster' :
        if name[0] == '&' :
            modules[name[1:]] = [name[0], output.split(', '), {}]
            conjunction.add(name[1:])
        elif name[0] == '%' :
            modules[name[1:]] = [name[0], output.split(', '), False]
    else :
        modules['broadcaster'] = ['broadcaster', output.split(', ')]

for name, output in modules.items() :
    for n in output[1] :
        if n in conjunction :
            modules[n][2][name] = False

stack = deque()

def all_flip_flop_off(di) :
    for name, _ in di.items() :
        if di[name][0] == '%' :
            if di[name][2] :
                return False
    return True

nb_rx = 0
while nb_rx != 1 :
    stack.append(('broadcaster', False, ''))
    send[1] += 1

    nb_rx = 0

    while stack :
        name, pulse, origin = stack.popleft()

        if name not in list(modules.keys()) :
            if name == 'rx' :
                nb_rx += 1
            continue

        if modules[name][0] == 'broadcaster' :
            for module in modules[name][1] :
                stack.append((module, pulse, name))
        elif modules[name][0] == '&' :
            modules[name][2][origin] = pulse
            output = all(list(modules[name][2].values()))
            for module in modules[name][1] :
                stack.append((module, not output, name))
        elif modules[name][0] == '%' and not pulse :
            modules[name][2] = not modules[name][2]
            for module in modules[name][1] :
                stack.append((module, modules[name][2], name))

print(p)
