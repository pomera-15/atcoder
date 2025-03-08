N = int(input())
A = list(map(int, input().split()))

A_MAX = 0
A_MIN = 10000000000

for a in A:
    if a > A_MAX:
        A_MAX = a
    if a < A_MIN:
        A_MIN = a

print(A_MAX - A_MIN)
