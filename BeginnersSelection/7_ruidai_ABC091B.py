N = int(input())
S = []
for _ in range(N):
    S.append(str(input()))

M = int(input())
T = []
for _ in range(M):
    T.append(str(input()))

# Sの文字列を言ったときの点数を算出する
points = {i: 0 for i in set(S)}

# 加点
for k, v in points.items():
    for s in S:
        if k == s:
            points[k] += 1

# 減点
for k, v in points.items():
    for t in T:
        if k == t:
            points[k] -= 1

# 最大値が答えになる
res = max(points.values())
if res < 0:
    res = 0

print(res)