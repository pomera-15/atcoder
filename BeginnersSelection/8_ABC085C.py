N, Y = input().split()
N, Y = int(N), int(Y)

ans_x = -1
ans_y = -1
ans_z = -1
for x in range(N + 1):
    for y in range(N + 1 - x):
        z = N - x - y
        if 10000*x + 5000*y + 1000*z == Y:
            ans_x = x
            ans_y = y
            ans_z = z

print(ans_x, ans_y, ans_z)