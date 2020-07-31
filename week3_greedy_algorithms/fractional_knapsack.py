import sys
import time

noitems, maxloot = map(int, input().split())
lst = []

if maxloot <= 0:
    print(0)
    quit()

for _ in range(noitems):
    value, weigth = map(int, input().split())
    if value <= 0:
        continue
    lst.append((value, weigth))
lst.sort(key=lambda x: x[0] / x[1], reverse=True)
total_value = 0
for value, weigth in lst:
    if maxloot <= 0:
        print('{:.4f}'.format(total_value))
        print(time.process_time())
        quit()
    amt = min(weigth, maxloot)
    total_value += amt * value / weigth
    maxloot -= amt
print('{:.4f}'.format(total_value))
print(time.process_time())
