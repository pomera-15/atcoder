N = int(input())
S = str(input())
T = str(input())

res = 0
for s, t in zip(S, T):
    if s != t:
        res += 1

print(res)