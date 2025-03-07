N = int(input())

ans = 0
max = 0
for n in range(1, N+1):

    cnt = 0
    i = n
    while i % 2 == 0:
        cnt += 1
        i = i / 2

    if max <= cnt:
        max = cnt
        ans = n

print(ans)
