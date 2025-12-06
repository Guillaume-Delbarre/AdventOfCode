# Exercice 1
data = open("2025/jour 6/exemple_input.txt", "r").read().split("\n")

numbers = [[int(number) for number in line.split(" ") if number != "" and number != " "] for line in data[:-1]]
operators = [ope for ope in data[-1] if ope != "" and ope != " "]

res = 0
for i_problem in range(len(operators)) :
    if operators[i_problem] == "+" :
        for nb_input in range(len(numbers)) :
            res += numbers[nb_input][i_problem]
    elif operators[i_problem] == "*" :
        temp = 1
        for nb_input in range(len(numbers)) :
            temp *= numbers[nb_input][i_problem]
        res += temp
    else :
        input(f"Erreur avec l'operateur {operators[i_problem]}")

print(res)


# Exercice 2
data = open("2025/jour 6/input.txt", "r").read().split("\n")

res = 0
current = []
for i in range(len(data[-1])-1, -1, -1) :
    number_list = [number for line in data[:-1] for number in line[i] if number != " "]
    number_list.reverse()
    number = sum([int(val)*pow(10,index) for index, val in enumerate(number_list)])
    current.append(number)

    if data[-1][i] in ("+", "*") :
        if data[-1][i] == "+" :
            # input(f"On fait la somme de {current}, on rajoute {sum(current)}")
            res+=sum(current)
        elif data[-1][i] == "*" :
            temp = 1
            for n in current :
                if n!=0 :
                    temp *= n
            # input(f"On fait le produit de {current}, on rajoute {temp}")
            res += temp
        current=[]
        i+=1

print(res)