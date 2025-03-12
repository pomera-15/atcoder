N, L = map(int, input().split())

S = []
for i in range(N):
    S.append(input())

ans = "".join(sorted(S))

print(ans)