nth = int(input())
if nth <= 1:
    print(nth)
    print(nth)
    quit()
w = nth
maxprize = []
for i in range(1,nth):
    if w > 2*i:
        maxprize.append(i)
        w -= i
    else:
        maxprize.append(w)
        break
print(len(maxprize))
print(' '.join([str(i) for i in maxprize]))