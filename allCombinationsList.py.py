#! python3
# allCombinationsList.py - gets all possible combinations of list.

from itertools import permutations

stuff = [1,2,3]
i = len(stuff)
combinations = []
while i != 0:
    perm = permutations(stuff, i)
    for r in list(perm): 
        combinations.append(r)
        print(r)
    i = i - 1
