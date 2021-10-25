# Practice set up:
knapsack1=10
knapsack2=11
size = [2, 4, 3, 5]      # should return true for practice set
# size = [2, 4, 6]        # should return false for practice set


def knap(aKnap, bKnap):
    global size
    if aKnap < 0 or bKnap < 0:
        return False
    elif aKnap == 0 and bKnap == 0:
        return True
    for i in size:
        if (knap(aKnap-size[i], bKnap) or knap(aKnap, bKnap-size[i])):
            return True

    return False

print(knap(10, 11))
