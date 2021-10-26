# Practice set up:
from typing import Sized


knapsack1=10
knapsack2=11
# size = [2, 4, 3, 5]      # should return true for practice set
# size = [2, 4, 6]        # should return false for practice set
size = [5, 7, 8, 2]


def knap(aKnap, bKnap):
    global size
    if aKnap < 0 or bKnap < 0:
        return False
    elif aKnap == 0 and bKnap == 0:
        return True
    for i in size:
        if (knap(aKnap-i, bKnap) or knap(aKnap, bKnap-i)):
            return True

    return False

print("knap(10, 11): " + str(knap(10, 11)))
print("knap(23, 14): " + str(knap(23, 14)))
print("knap(30, 22): " + str(knap(30, 22)))
