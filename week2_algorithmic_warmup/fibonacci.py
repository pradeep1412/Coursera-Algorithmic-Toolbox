# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fibs(gnvl):
    n1, n2 = 0, 1
    if gnvl <= 1:
        print(gnvl)
    for _ in range(gnvl - 1):
        nth = n1 + n2
        n1, n2 = n2, nth
    print(nth)


n = int(input())
# print(calc_fib(n))
calc_fibs(n)
