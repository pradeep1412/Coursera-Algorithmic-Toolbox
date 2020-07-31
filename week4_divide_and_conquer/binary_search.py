import time
import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif x > a[mid]:
            left = mid + 1
        elif x < a[mid]:
            right = mid - 1
    return -1


if __name__ == '__main__':
    seq = list(map(int, input().split()))
    data = list(map(int, input().split()))
    n = seq[0]
    a = seq[1:]
    for x in data[1:]:
        print(binary_search(a, x), end=' ')
