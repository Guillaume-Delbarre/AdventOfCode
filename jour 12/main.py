# Exercice 1
data = open("jour 12/input.txt", "r").read().split("\n")
data = [line.split() for line in data]

# print(data)

def compte(input) :
    hash_en_cours = False
    n = 0
    ret = ''
    for lettre in input :
        if lettre == '#' :
            hash_en_cours = True
            n += 1
        elif lettre == '.' :
            if hash_en_cours :
                ret += str(n) + ','
                n = 0
                hash_en_cours = False
    if hash_en_cours :
        ret += str(n) + ','
    return ret[:-1]

def partial_compte(input) :
    hash_en_cours = False
    n = 0
    ret = ''
    for lettre in input :
        if lettre == '#' :
            hash_en_cours = True
            n += 1
        elif lettre == '.' :
            if hash_en_cours :
                ret += str(n) + ','
                n = 0
                hash_en_cours = False
        elif lettre == '?' :
            if len(ret) > 1 :
                return ret[:-1]
            else :
                return ret
    if len(ret) > 1 :
        return ret[:-1]
    else :
        return ret

def get_possibility(input) :
    if '?' not in input :
        return [input]
    else :
        ret = []
        for index, lettre in enumerate(input) :
            if lettre == '?' :
                ret += get_possibility(input[:index] + '.' + input[index + 1:])
                ret += get_possibility(input[:index] + '#' + input[index + 1:])
        return ret
    
def get_true_possibility(input_str, res) :
    if '?' not in input_str :
        return [input_str]
    else :
        ret = []
        for index, lettre in enumerate(input_str) :
            if lettre == '?' :
                if res.startswith(partial_compte(input_str[:index] + '.' + input_str[index + 1:])) :
                    ret += get_true_possibility(input_str[:index] + '.' + input_str[index + 1:], res)
                if res.startswith(partial_compte(input_str[:index] + '#' + input_str[index + 1:])) :
                    ret += get_true_possibility(input_str[:index] + '#' + input_str[index + 1:], res)
                break
        return ret

score = 0
for line in data :
    score += len([1 for l in get_true_possibility(line[0], line[1]) if compte(l) == line[1]])

print(score)

# Exercice 2
data = open("jour 12/input.txt", "r").read().split("\n")
data = [line.split() for line in data]


for index, line in enumerate(data) :
    data[index][0] = "?".join([data[index][0] for _ in range(5)])
    data[index][1] = ",".join([data[index][1] for _ in range(5)])

score = 0
for line in data :
    score += len([1 for l in get_true_possibility(line[0], line[1]) if compte(l) == line[1]])

print(score)