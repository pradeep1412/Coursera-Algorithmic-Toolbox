# Uses python3
import sys
import time

m = int(input())


def get_change(m):
    # write your code here
    if m == 0:
        return 0
    best = -1
    coinarray = [1, 3, 4]
    for coin in coinarray:
        if coin <= m:
            nexttry = get_change(m - coin)
        if best < 0 or best > nexttry + 1:
            best = nexttry + 1
    return best


print(get_change(m))
#print(time.process_time())
