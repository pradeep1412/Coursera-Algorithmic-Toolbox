import time
n = int(input())
a = list(map(int,input().split()))
print(" ".join([str(i) for i in sorted(a)]))
