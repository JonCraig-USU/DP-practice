import numpy as np

# Practice set up
knapsack1=10
knapsack2=11
size = [2, 4, 3, 5]      # should return true for practice set
# size = [2, 4, 6]        # should return false for practice set
# size = [5, 7, 8, 2]


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


def knapDP(aKnap, bKnap):
    global size

    sols = np.zeros(shape=(aKnap+1, bKnap+1))


    for i in range(aKnap+1):
        for j in range(bKnap+1):
            sols[i, j] = False
    sols[0, 0] = True

    for x in range(1, aKnap+1):
        for y in range(1, bKnap+1):
            for s in size:
                if x-s>0 and sols[x-s, y]:
                    sols[x, y] = True
                if y-s>0 and sols[x, y-s]:
                        sols[x, y] = True
    print(sols)
    return sols[aKnap, bKnap]

# print("knap(10, 11): " + str(knap(10, 11)))
# print("knapDP(10, 11): " + str(knapDP(10, 11)))
# print("=======================================")
# print("knap(23, 14): " + str(knap(23, 14)))
# print("knapDP(23, 14): " + str(knapDP(23, 14)))
# print("=======================================")
# print("knap(30, 22): " + str(knap(30, 22)))
# print("knapDP(30, 22): " + str(knapDP(30, 22)))
# print("=======================================")
# print("knap(15, 22): " + str(knap(15, 22)))
# print("knapDP(15, 22): " + str(knapDP(15, 22)))

print(knapDP(11, 15))
