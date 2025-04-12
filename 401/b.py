N = int(input())
S = []
for _ in range(N):
    S.append(input())

status = "out"
res = 0
for s in S:
    if s == "login":
        status = "in"
    if s == "logout":
        status = "out"
    if s == "private" and status == "out":
        res += 1

print(res)