def to_base_k(n:int, k:int):
    """
    nをk進数に変換する
    """
    res = ""
    while n > 0:
        res = str(n % k) + res
        n = n // k
    return int(res)


N, K = map(int, input().split())
res = len(str(to_base_k(N,K)))
print(res)