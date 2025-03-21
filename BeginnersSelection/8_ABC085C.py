# N枚のお札の合計金額がY円
N, Y = map(int, input().split())

ans_x = -1  # 10000
ans_y = -1  # 5000
ans_z = -1  # 1000
for x in range(0, N + 1):
    for y in range(0, N + 1 - x):
        z = N - x - y
        if 10000*x + 5000*y + 1000*z == Y:
            ans_x = x
            ans_y = y
            ans_z = z

print(ans_x, ans_y, ans_z)