N = int(input())

# 初期値
t, x, y = 0, 0, 0

ans = "Yes"
for _ in range(N):
    t_new, x_new, y_new = map(int, input().split())

    # 差分を計算
    dt = t_new - t
    dx = abs(x_new - x)
    dy = abs(y_new - y)

    # マンハッタン距離が時間以内で、偶奇が一致するかチェック
    if dx + dy > dt or (dx + dy) % 2 != dt % 2:
        ans = "No"
        break

    # 現在地を更新
    t, x, y = t_new, x_new, y_new

print(ans)