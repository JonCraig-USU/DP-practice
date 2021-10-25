# n X m X p (board dimensions, integers)
n = 10
m = 10
p = 10
# moves = [M]
    # M = tuple (dx, dy, dz)
moves = [(1, 0, 0), (0, 2, 0), (0, 0, 3)]

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
        return
