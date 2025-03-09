import math

N ,D = map(int, input().split())
X = []
for _ in range(N):
    X.append(list(map(int, input().split())))

res = 0
for i, xi in enumerate(X):
    for xj in X[i+1:]:
 
        # xiとxjの距離を算出する
        d = 0
        for i in range(D):
            d += (xi[i] - xj[i])**2
        d = math.sqrt(d)
        
        # 整数かどうかを判定する(1で割ったときの余りが0かどうか)
        if d % 1 == 0:
            res += 1

print(res)