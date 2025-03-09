# 整数かどうかを判定する(1で割ったときの余りが0かどうか)
def is_integer(n: int):
    if n % 1 == 0:
        return True
    else:
        return False

# N次元空間における2点間のユークリッド距離を求める関数
import math
def distance(p1:list, p2:list):    
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(p1, p2)))


N ,D = map(int, input().split())
X = []
for _ in range(N):
    X.append(list(map(int, input().split())))

res = 0
for i, xi in enumerate(X):
    for xj in X[i+1:]:
        if is_integer(distance(xi, xj)):
            res += 1

print(res)