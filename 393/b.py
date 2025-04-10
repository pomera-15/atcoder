S = input()

N = len(S)
res = 0
for i in range(N):
    if S[i] == "A":
        for j in range(i, N):
            if S[j] == "B":
                for k in range(j, N):
                    if S[k] == "C":
                        if j - i == k - j:
                            res += 1

print(res)