N, M = map(int, input().split())

X = 0
for i in range(0, M+1):
    X += N**i

if X > 10**9:
    print("inf")
else:
    print(X)

