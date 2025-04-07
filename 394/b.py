N = int(input())
S = []
for _ in range(N):
    S.append(input())

min_s = S[0]
sorted_s = []
for i in range(0, N-1):
    for j in range(0, N-1-i):
        if len(S[j]) > len(S[j+1]):
            tmp = S[j]
            S[j] = S[j+1]
            S[j+1] = tmp
print("".join(S))