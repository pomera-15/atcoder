s = str(input())

ans = ""
for i, c in enumerate(s, 1):
    if i % 2 == 1:
        ans += c

print(ans)