N = int(input())
P = list(map(int, input().split()))

# ランクを入れるリストを用意する
ranks = [ 0 for _ in range(N)]

r = 1
up = 0  # 同ランクのものがあった場合に個数分ランクを落とすため用意
for _ in range(N):
    max_p = max(P)
    if max_p == -1:
        # すべてランクづけできたのでbreak
        break
    for i, p in enumerate(P):
        if p == max_p:
            ranks[i] = r
            P[i] = -1
            up += 1
    r += up
    up = 0

for r in ranks:
    print(r)