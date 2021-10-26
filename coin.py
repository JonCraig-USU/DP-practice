coins = []

def grab(left, right):
    if right == left:
        return coins[right]
    # elif right - left < 3:
    #     return max(coins[left] + grab(), right)

    elif coins[right] - coins[right - 1] >= coins[left] - coins[left + 1]:
        return max(coins[left] + grab(left+1, right), coins[right] + grab[left, right-1])
