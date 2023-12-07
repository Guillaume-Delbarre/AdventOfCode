from functools import cmp_to_key

# Exercice 1
data = open("jour 7/exemple_input.txt", "r").read().split("\n")
data = [line.split() for line in data]

# print(data)

order = {'A' : 13,
         'K' : 12,
         'Q' : 11,
         'J' : 10,
         'T' : 9,
         '9' : 8,
         '8' : 7,
         '7' : 6,
         '6' : 5,
         '5' : 4,
         '4' : 3,
         '3' : 2,
         '2' : 1}

def compare(tot1, tot2) :
    main1 = tot1[0]
    main2 = tot2[0]
    s1 = list(set(main1))
    s2 = list(set(main2))
    if len(s1) > len(s2) :
        # print(f"La main {tot2} et plus forte que {tot1}")
        return -1
    elif len(s1) < len(s2) :
        # print(f"La main {tot1} et plus forte que {tot2}")
        return 1
    else :
        if len(s1) == 2 : # Différentier Four of a kind et Full house
            foak1 = main1.count(s1[0]) == 4 or main1.count(s1[1]) == 4
            foak2 = main2.count(s2[0]) == 4 or main2.count(s2[1]) == 4
            if foak1 and not foak2 :
                # print(f"La main {tot1} et plus forte que {tot2}")
                return 1
            elif not foak1 and foak2 :
                # print(f"La main {tot2} et plus forte que {tot1}")
                return -1
        if len(s1) == 3 : # Différentier Three of a kind et Two pair
            foak1 = main1.count(s1[0]) == 3 or main1.count(s1[1]) == 3 or main1.count(s1[2]) == 3
            foak2 = main2.count(s2[0]) == 3 or main2.count(s2[1]) == 3 or main2.count(s2[2]) == 3
            if foak1 and not foak2 :
                # print(f"La main {tot1} et plus forte que {tot2}")
                return 1
            elif not foak1 and foak2 :
                # print(f"La main {tot2} et plus forte que {tot1}")
                return -1
        # Différentier sur la hauteur
        n_main1 = [order[carte] for carte in main1]
        n_main2 = [order[carte] for carte in main2]
        for c1, c2 in zip(n_main1, n_main2) :
            if c1 != c2 :
                if c1 > c2 :
                    # print(f"La main {tot1} et plus forte que {tot2}")
                    return 1
                elif c1 < c2 :
                    # print(f"La main {tot2} et plus forte que {tot1}")
                    return -1
        print(f"Erreur de comparaison avec les mains {main1} et {main2}")
        return 0

data_sort = sorted(data, key=cmp_to_key(compare))

score = 0
for index, main in enumerate(data_sort, 1) :
    score += index*int(main[1])

print(score)


# Exercice 2
data = open("jour 7/input.txt", "r").read().split("\n")
data = [line.split() for line in data]

order = {'A' : 13,
         'K' : 12,
         'Q' : 11,
         'J' : 0,
         'T' : 9,
         '9' : 8,
         '8' : 7,
         '7' : 6,
         '6' : 5,
         '5' : 4,
         '4' : 3,
         '3' : 2,
         '2' : 1}

# data = [['J345A', '2'], ['2345A', '1']]

def compare2(tot1, tot2) :
    main1 = tot1[0]
    main2 = tot2[0]

    max_main1 = sorted(main1.replace("J", ""), key = lambda carte : main1.count(carte), reverse=True)
    max_main2 = sorted(main2.replace("J", ""), key = lambda carte : main2.count(carte), reverse=True)

    if main1 == "JJJJJ" :
        new_main1 = "22222"
    else :
        new_main1 = main1.replace("J", max_main1[0])

    if main2 == "JJJJJ" :
        new_main2 = "22222"
    else :
        new_main2 = main2.replace("J", max_main2[0])
    
    s1 = list(set(new_main1))
    s2 = list(set(new_main2))

    if len(s1) > len(s2) :
        #print(f"La main {new_main2} et plus forte que {new_main1}")
        return -1
    elif len(s1) < len(s2) :
        #print(f"La main {new_main1} et plus forte que {new_main2}")
        return 1
    else :
        if len(s1) == 2 : # Différentier Four of a kind et Full house
            foak1 = new_main1.count(s1[0]) == 4 or new_main1.count(s1[1]) == 4
            foak2 = new_main2.count(s2[0]) == 4 or new_main2.count(s2[1]) == 4
            if foak1 and not foak2 :
                #print(f"La main {new_main1} et plus forte que {new_main2}")
                return 1
            elif not foak1 and foak2 :
                #print(f"La main {new_main2} et plus forte que {new_main1}")
                return -1
        if len(s1) == 3 : # Différentier Three of a kind et Two pair
            foak1 = new_main1.count(s1[0]) == 3 or new_main1.count(s1[1]) == 3 or new_main1.count(s1[2]) == 3
            foak2 = new_main2.count(s2[0]) == 3 or new_main2.count(s2[1]) == 3 or new_main2.count(s2[2]) == 3
            if foak1 and not foak2 :
                #print(f"La main {new_main1} et plus forte que {new_main2}")
                return 1
            elif not foak1 and foak2 :
                #print(f"La main {new_main2} et plus forte que {new_main1}")
                return -1
        # Différentier sur la hauteur
        n_main1 = [order[carte] for carte in main1]
        n_main2 = [order[carte] for carte in main2]
        for c1, c2 in zip(n_main1, n_main2) :
            if c1 != c2 :
                if c1 > c2 :
                    #print(f"La main {new_main1} et plus forte que {new_main2}")
                    return 1
                elif c1 < c2 :
                    #print(f"La main {new_main2} et plus forte que {new_main1}")
                    return -1
        print(f"Erreur de comparaison avec les mains {main1} et {main2}")
        return 0
    

data_sort = sorted(data, key=cmp_to_key(compare2))

score = 0
for index, main in enumerate(data_sort, 1) :
    score += index*int(main[1])
    # print(index, main)

print(score)