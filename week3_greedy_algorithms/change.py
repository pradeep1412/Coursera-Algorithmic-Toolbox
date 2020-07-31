# Uses python3
import sys
import time


def get_change(m):
    # write your code here
    c = m // 10
    r = m % 10
    c1 = r // 5
    r1 = r % 5
    m = c + r1 + c1
    return m


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
    # print(time.process_time())
