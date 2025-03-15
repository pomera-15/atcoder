N = int(input())
A = list(map(int, input().split()))

# bucketを用意する
from collections import defaultdict
left = defaultdict(int)
right = defaultdict(int)

# bucketに初期値を入れる
for a in A[:1]:
    left[a] += 1
for a in A[1:]:
    right[a] += 1

max_left = len(left)
max_right = len(right)

max = max_left + max_right
for i in range(1, N - 1):

    # rightからleftに移動する数字がleftにすでに存在しなければmax_leftが1増加する
    if left[A[i]] == 0:
        max_left += 1
    # rightからleftに移動する数字がrightに1つだけ存在する場合は異動によりmax_rightが1減少する
    if right[A[i]] == 1:
        max_right -= 1

    if max < max_left + max_right:
        max = max_left + max_right

    # left, rightの境界が一つずれるためbucketを更新する
    left[A[i]] += 1
    right[A[i]] -= 1

print(max)