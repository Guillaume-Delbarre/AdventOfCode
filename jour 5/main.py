# Exercice 1
data = open("jour 5/exemple_input.txt", "r").read().split("\n\n")

seeds = list(map(int, data[0].split()[1:]))

data = [group.split("\n") for group in data[1:]]
# print(data)


for relation in data :
    moved = [False] * len(seeds)
    for group in relation[1:] :
        start1, start2, length = group.split()
        for index, seed in enumerate(seeds) :
            if seed in range(int(start2), int(start2) + int(length)) and not moved[index]:
                seeds[index] = int(start1) + seed - int(start2)
                moved[index] = True

print(min(seeds))



# Exercice 2
import copy
data = open("jour 5/input.txt", "r").read().split("\n\n")

seeds_range = list(map(int, data[0].split()[1:]))
seeds = [(seeds_range[2*i], seeds_range[2*i] + seeds_range[2*i+1]) for i in range(int(len(seeds_range) / 2))]

print(seeds)
# seeds.remove((79, 93))

data = [group.split("\n") for group in data[1:]]


for relation in data :
    new_seeds = []
    for group in relation[1:] :
        start_nouveau, start_ancien, length = list(map(int,group.split()))
        end_nouveau = start_nouveau + length
        end_ancien = start_ancien + length
        # print("nouvelle boucle avec : ", seeds)

        current_seed = []
        while len(seeds) > 0 :
        # for index, seed in enumerate(seeds) :
            start_seed, end_seed = seeds[0]

            # print(f"seeds {seeds[0]}    /   nouveau {(start_nouveau, end_nouveau)}  /   ancien {(start_ancien, end_ancien)}")
            # print(seeds)
            # print()

            if start_ancien <= start_seed and end_ancien >= start_seed:
                if end_ancien < end_seed :
                    # Cas 1
                    # print("Cas 1")
                    new_seeds.append((start_nouveau + (start_seed - start_ancien), end_nouveau))
                    current_seed.append((end_ancien, end_seed))
                    seeds.remove(seeds[0])
                else :
                    # Cas 2
                    # print("Cas 2")
                    new_seeds.append((start_nouveau + start_seed - start_ancien, end_nouveau - (end_ancien - end_seed)))
                    seeds.remove(seeds[0])

            elif start_ancien <= end_seed and start_ancien >= start_seed:
                if end_ancien <= end_seed :
                    # Cas 3
                    # print("Cas 3")
                    current_seed.append((start_seed, start_ancien))
                    new_seeds.append((start_nouveau, end_nouveau))
                    current_seed.append((end_ancien, end_seed))
                    seeds.remove(seeds[0])
                else :
                    # Cas 4
                    # print("Cas 4")
                    current_seed.append((start_seed, start_ancien))
                    new_seeds.append((start_nouveau, start_nouveau + end_seed - start_ancien))
                    seeds.remove(seeds[0])

            else :
                # Cas où les seeds ne sont pas impactées
                current_seed.append(seeds[0])
                seeds.remove(seeds[0])

        seeds = copy.deepcopy(current_seed)
    
    seeds += copy.deepcopy(new_seeds)

seeds = [s for s, t in seeds]
print(min(seeds))