# Uses python3
import sys
import time


def get_fibonacci_last_digit_naive1(n):
    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    print(current)


if __name__ == '__main__':
    n = int(input())
    if n <= 1:
        print(n)
        quit()
    get_fibonacci_last_digit_naive1(n)
    #print(time.process_time())
