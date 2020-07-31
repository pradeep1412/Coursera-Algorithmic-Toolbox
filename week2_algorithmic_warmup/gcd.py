# Uses python3
import sys



def gcd_naive1(a, b):

    if a < b:
        temp = a
        a = b
        b = temp
    while b != 0:
        temp = a % b
        a = b
        b = temp
    if a == 0 and b == 0:
        a = 1
    return a


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_naive1(a, b))
