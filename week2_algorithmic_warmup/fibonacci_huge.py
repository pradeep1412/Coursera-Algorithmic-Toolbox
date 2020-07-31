# Uses python3
import sys
import time


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return i + 1


def fibonacci_huge1(n, m):
    n = n % pisanoPeriod(m)

    previous, current = 0, 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n - 1):
        previous, current = current % m, (previous + current) % m

    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge1(n, m))

