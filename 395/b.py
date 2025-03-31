N = int(input())

# 矩形領域をつくる
S = []
for x in range(N):
    S.append([])
    for y in range(N):
        S[x].append("*")

# ターゲットをつくる
for i in range(1, N+1):
    j = N + 1 - i
    if i <= j:
        if i % 2 == 1:
            # 黒 で左上(i, i)、右下(j, j)矩形領域を塗りつぶす
            for ii in range(i-1, j):
                for jj in range(i-1, j):
                    S[ii][jj] = "#"
        else:
            # 白 で左上(i, i)、右下(j, j)矩形領域を塗りつぶす
            for ii in range(i-1, j):
                for jj in range(i-1, j):
                    S[ii][jj] = "."

for i in range(N):
    print("".join(S[i]))