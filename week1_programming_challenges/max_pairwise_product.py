# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
def by_sorting(numbers,n):
    ln = list(sorted(numbers))
    return ln[n-1]*ln[n-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    #print(max_pairwise_product(input_numbers))
    print(by_sorting(input_numbers,input_n))
    #a = max_pairwise_product(input_numbers)
    #d = by_sorting(input_numbers,input_n)
    #if a == d:
    #    print('ok')
    #else:
    #    print('worng:incorrect answer',a,d)
