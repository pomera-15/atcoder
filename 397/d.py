import math

def sol(a, b, c):
    """
    ax^2 + bx + c = 0の正の整数の解を二分探索で求める（解がない場合は -1 を返す）
    """
    l, r = 0, 600000001
    
    while r - l > 1:
        mid = (l + r) // 2
        if a * mid * mid + b * mid + c <= 0:
            l = mid
        else:
            r = mid
    
    return l if a * l * l + b * l + c == 0 else -1


N = int(input())

# 以下のようにd, kを置く
# d = x - y
# k = y

# dはNの3乗根以下になる。
max_d = int(math.pow(N, 1 / 3))

for d in range(1, max_d+1):
    # (3d)k^2 + (3d^2)k + (d^3-N) = 0 をkの2次方程式として解の公式を用いる
    k = sol(3*d, 3*d**2, d**3-N)
        
    if k > 0:
        x = d + k
        y = k
        print(f"{x} {y}")
        exit()

print(-1)

