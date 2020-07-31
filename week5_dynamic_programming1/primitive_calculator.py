import sys
import time
n = int(input())
sequence = []
while n >= 1:
    sequence.append(n)
    t = n%3
    to = n%2
    if t:
        n = n // 3
    elif n % 2 <= n % 3:
        n = n // 2
    else:
        n = n - 1
print(len(sequence)-1)
print(" ".join([str(i) for i in sequence][::-1]))
#print(time.process_time())
