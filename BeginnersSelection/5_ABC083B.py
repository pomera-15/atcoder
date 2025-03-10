def sum_each_digit(n: int):
    """
    nの各桁の和を求める
    """
    sum = 0
    while n > 0:
        sum += n % 10
        n = int(n / 10)
    return sum


N, A, B = map(int, input().split())

res = 0
for n in range(1,N+1):
    # 格桁の和を求める
    sum = sum_each_digit(n)
    # 和がA以上B以下かどうか
    if A <= sum and sum <= B:
        res += n

print(res)