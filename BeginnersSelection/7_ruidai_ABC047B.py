W, H, N = map(int, input().split())
P = []
for _ in range(N):
    P.append(list(map(int, input().split())))

S = []
for x in range(W):
    S.append([])
    for y in range(H):
        S[x].append(True)

# 面積を刈り取っていく
for [px, py, a] in P:
    if a == 1:
        # x:1~px、y:1~H をFalseに置き換える
        for x in range(px):
            for y in range(H):
                S[x][y] = False
    elif a == 2:
        # x:px~W、y:1~H をFalseに置き換える
        for x in range(px,W):
            for y in range(H):
                S[x][y] = False    
    elif a == 3:
        # x:1~W、y:1~py をFalseに置き換える
        for x in range(W):
            for y in range(py):
                S[x][y] = False
    elif a == 4:
        # x:1~W、y:py~H をFalseに置き換える
        for x in range(W):
            for y in range(py,H):
                S[x][y] = False

# Trueを数える
res = 0
for x in range(W):
    for y in range(H):
        if S[x][y] == True:
            res += 1

print(res)