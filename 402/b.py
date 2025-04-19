Q = int(input())

machi = []
res = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if len(q) == 2:
        machi.append(q)
    else:
        res.append(machi.pop(0)[1])

for r in res:
    print(r)