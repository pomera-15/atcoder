n, d = map(int, input().split())
S = input()

newS = []
for i in range(n-1, -1, -1):
    if S[i] == "@" and d > 0:
        newS.insert(0, ".")
        d -= 1
    else:
        newS.insert(0, S[i])

print("".join(newS))
