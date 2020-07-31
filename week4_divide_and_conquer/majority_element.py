import time
from collections import Counter, OrderedDict


class OrderedictCounter(Counter, OrderedDict):
    pass;


n = int(input())
a = list(map(int, input().split()))
dic = OrderedictCounter(a)
count = 0
for i in dic.values():
    if i > n // 2:
        count += 1
print(count)

