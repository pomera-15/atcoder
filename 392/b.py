N, M = map(int, input().split())
A = list(map(int, input().split()))

res = set()
for i in range(1, N+1):
    if i not in A:
        res.add(i)

if len(res) != 0:
    print(len(res))
    print(*res)
else:
    print(0)