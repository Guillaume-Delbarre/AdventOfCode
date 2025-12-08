import math
import heapq

# Exercice 1
data = open("2025/jour 8/exemple_input.txt", "r").read().split("\n")

boxes = [[int(coord) for coord in box.split(",")] for box in data]
nb_distance = 10

def distance(box1, box2) -> int :
    return math.sqrt(pow(box1[0]-box2[0], 2) + pow(box1[1]-box2[1], 2) + pow(box1[2]-box2[2], 2))

def get_n_min_distances(boxes=boxes, nb=nb_distance) :
    heap = []
    for i in range(len(boxes)) :
        for j in range(i+1, len(boxes)) :
            dist = -1 * distance(boxes[i], boxes[j])
            # print(f"Distance entre {i} : {boxes[i]} et {j} : {boxes[j]}  = {dist}")
            if len(heap) < nb :
                heapq.heappush(heap, (dist, i, j))
            else :
                if dist > heap[0][0] :
                    heapq.heapreplace(heap, (dist, i, j))
            # input(f"Nouveau heap : {heap}")
    return heap

min_dist = get_n_min_distances()

res = [[i] for i in range(len(boxes))]

for (link, box1, box2) in min_dist :
    index_1 = 0
    index_2 = 0
    for i, group in enumerate(res) :
        if box1 in group :
            index_1 = i
        if box2 in group :
            index_2 = i
    if index_1 != index_2 :
        n_res = [r for j,r in enumerate(res) if j != index_1 and j != index_2]
        n_res.append(res[index_1]+res[index_2])
    res = n_res

lis = sorted([len(r) for r in res], reverse=True)
print(lis[0] * lis[1] * lis[2])


# Exercice 1
data = open("2025/jour 8/input.txt", "r").read().split("\n")

boxes = [[int(coord) for coord in box.split(",")] for box in data]

def get_distances(boxes=boxes) :
    links = []
    for i in range(len(boxes)) :
        for j in range(i+1, len(boxes)) :
            dist = distance(boxes[i], boxes[j])
            links.append((dist, i, j))

    sorted_lst = sorted(links, key=lambda t: t[0])
    return sorted_lst

links = get_distances()
box_linked = set()
i=0
while len(box_linked) != len(boxes) :
    box_linked.add(links[i][1])
    box_linked.add(links[i][2])
    i+=1

print(links[i-1])
print(boxes[links[i-1][1]][0] * boxes[links[i-1][2]][0])