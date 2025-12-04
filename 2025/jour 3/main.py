# Exercice 1
data = open("2025/jour 3/input.txt", "r").read().split("\n")

res=0
nb_turn = 12

def get_max(bank, nb_turn=nb_turn) -> int:
    if len(bank) == nb_turn :
        return int("".join([str(b) for b in bank]))
    elif len(bank) < nb_turn :
        return 0
    else :
        premier = bank[0]
        bank_reste = get_max(bank[1:])
        batteries = [int(b) for b in str(bank_reste)]

        if premier >= batteries[0] :
            min_val = min(batteries)
            batteries.remove(min_val)
            return int(str(premier) + "".join([str(b) for b in batteries]))
        else :
            return int("".join([str(b) for b in batteries]))



for bank in data :
    print([int(battery) for battery in bank])
    val_bank = get_max([int(battery) for battery in bank])
    res += val_bank
    print(f"Ajout de {val_bank}")

print(res)