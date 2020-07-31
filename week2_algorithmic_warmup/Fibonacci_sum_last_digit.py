import sys
import time


def fibonacci_huge1(n):
    n = n % 60
    previous, current = 0, 1
    sum = 1
    if n <= 1:
        return n

    for i in range(n - 1):
        previous, current = current, (previous + current)
        sum += current
    return sum % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_huge1(n))
