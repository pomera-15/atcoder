N = int(input())
A = list(map(int, input().split())) 

# set(A)でバケットを作成
setA = set(A)
buckets = {a: 0 for a in setA}

# N人でそれぞれ何個整数を持っているか
for a in A:
    buckets[a] += 1

# Valueが1かつ最大のKeyを求める
max_k = 0
for k, v in buckets.items():
    if v ==1 and k > max_k:
        max_k = k

# max_kを所持する人の番号(res)を求める
res = -1
for i, a in enumerate(A, 1):
    if a == max_k:
        res = i

print(res)