# 再帰のメモ化では間に合わない

import sys
sys.setrecursionlimit(10**6)

def A(n,k, memo={}):
    if n in memo.keys():
        return memo[n]
    if n < k:
        return 1

    sum = k
    for i in range(1, k + 1):
        sum += sum + i
    memo[n] = sum
    return sum

N, K = map(int, input().split())
memo = {}
print(A(N, K, memo) % 10**9)