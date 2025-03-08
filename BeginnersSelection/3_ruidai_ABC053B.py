s = str(input())

ans = -1
left = 10000000000
right = -1
for i, c in enumerate(s):
    if c == "A":
        if i < left:
            left = i
    if c == "Z":
        if i > right:
            right = i

print(right - left + 1)