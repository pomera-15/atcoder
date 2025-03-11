def sum_each_digit(n: int):
    """
    nの各桁の和を求める
    """
    sum = 0
    while n > 0:
        sum += n % 10
        n = int(n / 10)
    return sum

N = int(input())

min = 1000000
for i in range(1, N):
    A = i
    B = N - i
    a = sum_each_digit(A)
    b = sum_each_digit(B)
    if a + b < min:
        min = a + b

print(min)
