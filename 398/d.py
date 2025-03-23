def w2newW(W, S):
    """
    wを受け取って1s後のwを返す
    wには常に[0,0]を追加する
    """
    # [0,0]がない場合は追加する
    if not([0, 0] in W):
        W.append([0,0])

    # 1s経過して煙が移動する
    newW = []
    for w in W:
        if S == "N":
            newW.append([w[0]-1, w[1]])
        elif S == "W":
            newW.append([w[0], w[1]-1])
        elif S == "S":
            newW.append([w[0]+1, w[1]])
        elif S == "E":
            newW.append([w[0], w[1]+1])

    return newW


N, R, C = map(int, input().split())
S = str(input())

# 高橋くんの立ち位置
takahashi = [R, C]

# もともと煙がある場所
W = [[0, 0]]

res = ""
for s in S:
    # 1s経過して煙が移動する
    newW = w2newW(W, s)
    print(W, newW)

    # この時点での高橋くんの位置に煙があるかどうかをチェックする
    if takahashi in newW:
        res += "1"
    else:
        res += "0"
    # 置き換える
    W = newW

print(res)