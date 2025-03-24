N, R, C = map(int, input().split())
S = str(input())

# 焚き火の初期位置
r, c = 0, 0

# 煙の初期位置
W = set()
W.add((0, 0))

res = ""
for s in S:

    print(W)

    # 1s経過して焚き火、高橋くんが移動する
    if s == "N":
        r += 1
    elif s == "W":
        c += 1
    elif s == "S":
        r -= 1
    elif s == "E":
        c -= 1

    # 煙が焚き火の位置に追加される
    W.add((r, c))

    # この時点での高橋くんの位置(焚き火から見た相対位置[r+R,c+C])に煙があるかどうかをチェックする
    if (r+R,c+C) in W:
        res += "1"
    else:
        res += "0"

print(res)