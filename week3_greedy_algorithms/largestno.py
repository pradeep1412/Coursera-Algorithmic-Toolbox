# python3
n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)


def largestnumber(lst):
    answer = []

    while lst != []:
        max_digit = 0
        for digit in lst:
            if int(str(digit)+str(max_digit)) >= int(str(max_digit)+str(digit)):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer


print(''.join([str(i) for i in largestnumber(lst)]))
