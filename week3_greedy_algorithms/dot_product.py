import time
nth = int(input())
profit = list(map(int,input().split()))
average = list(map(int,input().split()))
profit.sort()
average.sort()
ans = sum([profit[i]*average[i] for i in range(nth)])
print(ans)
#print(time.process_time())