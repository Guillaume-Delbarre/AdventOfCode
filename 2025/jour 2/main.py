# Exercice 1
data = open("2025/jour 2/exemple_input.txt", "r").read().replace("\n", "").split(",")
# print(data)

ranges = [(int(da.split("-")[0]), int(da.split("-")[1])) for da in data]

res=0

for (debut, fin) in ranges :
    # input(f"debut : {debut}, fin : {fin}, res:{res}")
    for i in range(debut, fin+1) :
        val = str(i)
        if len(val) % 2 == 0 :
            moit = int(len(val)/2)
            if val[:moit] == val[moit:] :
                res += i
                # print(f"ajout de {i}")

print(res)


# Exercice 2
data = open("2025/jour 2/input.txt", "r").read().replace("\n", "").split(",")

ranges = [(int(da.split("-")[0]), int(da.split("-")[1])) for da in data]

res=0

def is_repeating(number, size) -> bool :
    # print(f"is repeating {number}, {size}")
    val = str(number)
    if len(val) % size != 0 :
        return False
    else :
        schema = val[:size]
        # print(f"1 : {1}, len(val)//size : {len(val)//size}")
        # print(f"valeurs de la boucle : {[r for r in range(1, len(val)//size)]}")
        for i in range(1, len(val)//size) :
            # print(f"schema : {schema}, val : {val}, i:{i}, i*size : {i*size}, val[i*size:(i+1)*size] : {val[i*size:(i+1)*size]}")
            if schema != val[i*size:(i+1)*size] :
                # print(f"pas ok pour {number} avec {schema} != {val[i*size:(i+1)*size]}")
                # print(f"size : {size}, i : {i}")
                return False
        # print(f"ok pour {number} avec {schema}")
        return True

    
def is_valid(number) -> bool :
    # print(f"is valid pour {number}")
    val = str(number)
    # print(range(1, len(val)//2+1))
    for size in range(1, len(val)//2+1) :
        if is_repeating(number, size) :
            return True
    return False


for (debut, fin) in ranges :
    # input(f"debut : {debut}, fin : {fin}, res:{res}")
    for i in range(debut, fin+1) :
        if is_valid(i) :
            # print(f"valid pour {i}")
            res += i

print(res)
