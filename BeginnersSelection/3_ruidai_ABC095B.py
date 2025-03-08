N, X = map(int, input().split())

min_m = 10000000000     # 必要g数が最小のm
cnt = 0                 # 作成したドーナッツの合計数
sum = 0                 # 作成したドーナッツの合計量

# 作れるドーナッツの各種類を一つずつ作る
# そのさいに一番必要g数が小さいドーナッツを調べる
for _ in range(N):
    m = int(input())
    sum += m
    cnt += 1
    if min_m > m:
        min_m = m

# 一番必要g数が小さいドーナッツをできるだけ作る
while sum <= X:
    sum += min_m
    if sum <= X:
        cnt += 1

print(cnt)
