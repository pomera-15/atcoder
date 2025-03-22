A = list(map(int, input().split()))

# 0 - 13のバケツを用意する
B = [0 for i in range(0, 14)]

# 整数ごとの個数を求める
for a in A:
    B[a] += 1

# フラグ
f1 = 0
f2 = 0

# 3以上があるかどうか
for i, b in enumerate(B):
    if b >= 3:
        # 3以上とした整数は個数を0にしておく
        B[i] = 0
        f1 = 1
        break

# 2以上があるかどうか
for i, b in enumerate(B):
    if b >= 2:
        # 2以上とした整数は個数を0にしておく
        B[i] = 0
        f2 = 1
        break

# フルハウスの条件を満たすかどうか
if f1 and f2:
    print("Yes")
else:
    print("No")
