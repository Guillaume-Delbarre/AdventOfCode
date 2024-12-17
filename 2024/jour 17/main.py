# Exercice 1
register, program = open("2024/jour 17/input.txt", "r").read().split("\n\n")
register = [int(d[12:]) for d in register.split('\n')]
register = {'A' : register[0], 'B' : register[1], 'C' : register[2]}
program = [int(p) for p in program[9:].split(',')]

def get_combo_operand(operand) :
    if operand in (0, 1, 2, 3) :
        return operand
    elif operand == 4 :
        return register['A']
    elif operand == 5 :
        return register['B']
    elif operand == 6 :
        return register['C']
    print(f"[Error] operand {operand} is not supported")
    return None

def process(opcode, operand, register) :
    global i
    if opcode == 0 : #adv
        denom = pow(2, get_combo_operand(operand))
        num = register['A']
        register['A'] = int(num/denom)
        i += 2
    elif opcode == 1 : #bxl
        val1 = register['B']
        val2 = operand
        register['B'] = val1 ^ val2
        i += 2
    elif opcode == 2 : #bst
        val = get_combo_operand(operand)
        register['B'] = val % 8
        i += 2
    elif opcode == 3 : #jnz
        if register['A'] == 0 :
            i += 2
        else :
            i = operand
    elif opcode == 4 : #bxc
        register['B'] = register['B'] ^ register['C']
        i += 2
    elif opcode == 5 : #out
        val = get_combo_operand(operand)
        i += 2
        return val % 8
    elif opcode == 6 : #bdv
        denom = pow(2, get_combo_operand(operand))
        num = register['A']
        register['B'] = int(num/denom)
        i += 2
    elif opcode == 6 : #cdv
        denom = pow(2, get_combo_operand(operand))
        num = register['A']
        register['C'] = int(num/denom)
        i += 2
    return None



i = 0
res = []
while i < len(program)-1 :
    code = program[i]
    rand = program[i+1]
    # print(f"On est avec i:{i} on a opcode:{code} et oprand:{rand}")
    # print(f"On a comme registre : {register}")
    val = process(code, rand, register)
    if val != None :
        res.append(str(val))

print(f"Etat final : register={register}")

print(",".join(res))