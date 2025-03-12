N, K = map(int, input().split())
L = list(map(int, input().split()))

L.sort(reverse=True)
sum = 0
for i in range(K):
    sum += L[i]

print(sum)