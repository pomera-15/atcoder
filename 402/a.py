S = input()
# A = list(map(int, input().split()))

res = ""
for s in S:
    if s.isupper():
        res += s

print(res)