# Exercice 1
from collections import deque
data = open("jour 23/exemple_input.txt", "r").read().split('\n')

print(data)

start = (data[0].index('.'), 0)

chemins = deque()

print(start)


