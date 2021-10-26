'''My interpretation of this one is throwing me for a loop
    Q - diagonally up or down and to the right? or is left allowed too?
    Q - when does the game end? when other side is reached? A 0 is reached?
    Q - can a square be hit more than once?
    Q - Is the monetary value different form square to square?'''
import numpy as np
m = 5
n = 5
values = np.zeros(m, n)

def grabbyWrapper():
    big = 0
    for i in range(m):
        cur = grabby(0, i)
        if big < cur:
            big = cur
    return big


def grabby(x, y):
    global m
    global n

    if y > m or y < 0:
        return 0
    if x > n:
        return 0
    return max(grabby(x+1, y+1), grabby(x+1, y-1)) + values[x][y]