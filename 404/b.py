
def diff_num(S,T):
    cnt = 0
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][j] == "." and T[i][j] == "#":
                cnt += 1
            if S[i][j] == "#" and T[i][j] == ".":
                cnt += 1
    return cnt

def migi90(S):
    N = len(S)
    T = []
    for i in range(N):
        T.append(["."] * N)
    for i in range(N):
        for j in range(N):
            T[j][N - 1 - i] = S[i][j]
    return T

def check(N, S, T):

    # 差分が2以下のときは回転させずに差分が答えになる
    # if diff_num(S, T) <= 2:
    #     return diff_num(S, T)

    # どの方向が一番一致するかを調べる
    # そのままの一致数
    res0 = diff_num(S, T)
    # 90度回転
    res90 = 1 + diff_num(migi90(S), T)
    # 180度回転
    res180 = 2 + diff_num(migi90(migi90(S)), T)
    # 270度回転
    res270 = 3 + diff_num(migi90(migi90(migi90(S))), T)

    return min(res0, res90, res180, res270)


N = int(input())
S = []
for i in range(N):
    S.append(list(input()))
T = []
for i in range(N):
    T.append(list(input()))

print(check(N, S, T))