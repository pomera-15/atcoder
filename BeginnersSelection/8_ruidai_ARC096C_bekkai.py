a, b, c, x, y = map(int, input().split())

min = 10**100
for ab in range(max(x, y)+1):
    sum = c * 2 * ab
    if x - ab > 0:
        sum += a * (x - ab)
    if y - ab > 0:
        sum += b * (y - ab)
    if sum < min:
        min = sum

print(min)