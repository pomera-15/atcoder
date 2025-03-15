from collections import defaultdict

N = int(input())

D = []
for _ in range(N):
    D.append(int(input()))

# -- バケット法 --

# bucketを用意する
buckets = defaultdict(int)

# bucketに値を入れる
for d in D:
    buckets[d] += 1

# bucketsに値が入っている数が答えになる
print(len(buckets))
