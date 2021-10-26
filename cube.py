# n X m X p (board dimensions, integers)
import numpy as np


n = 10
m = 10
p = 10
# moves = [M]
    # M = tuple (dx, dy, dz)
# moves = [(1, 0, 0), (0, 2, 0), (0, 0, 3)]
moves = [(3, 0, 0), (0, 3, 0), (0, 0, 3)]

# visited = set(())
visited = []


def traverse(loc):    # not sure if more inputs will be needed
    # I believe all these globals will be needed?
    global n
    global m
    global p
    global moves
    global visited

    if loc[0] > n or loc[1] > m or loc[2] > p:
        return
    elif loc in visited:
        return
    else:
        visited.append(loc)
        for move in moves:
            traverse((loc[0] + move[0], loc[1] + move[1], loc[2] + move[2]))
        return visited


def traverseDP(x, y, z):
    global sol
    global moves
    global visited

    sol = np.zeros(m+1, n+1, p+1)
    for i in range(m+1):
        for j in range(n+1):
            for k in range(p+1):
                sol[i, j, k] = False
    
    sol[x, y, z] = True






temp = traverse((1, 1, 1))
for i in temp:
    print(i)
