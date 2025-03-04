N = int(input())
A = list(map(int, input().split()))

cnt = 0
while True:
    if any( a % 2 == 1 for a in A):
        break
    A = [a / 2 for a in A]
    cnt += 1

print(cnt)
