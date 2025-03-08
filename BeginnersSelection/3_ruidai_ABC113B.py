N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

dmin = 10000000000
ans_h = -1
for i, h in enumerate(H, 1):
    t = T - h * 0.006
    d = abs(A - t)
    if d < dmin:
        dmin = d
        ans_h = i

print(ans_h)
        