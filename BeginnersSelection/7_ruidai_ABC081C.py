N, K = map(int, input().split())
A = list(map(int, input().split()))

# バケツnumを用意する
num = [0 for _ in range(max(A))]
for a in A:
    num[a - 1] += 1

# 降順にソートして先頭からK個まで確定、それ以降は置き換えると考える
# 置き換える整数の個数の合計が答えになる
num.sort(reverse=True)
print(sum(num[K:]))
