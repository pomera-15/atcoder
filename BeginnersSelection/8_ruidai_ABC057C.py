import math
N = int(input())

min_k = 11
for a in range(1, int(math.sqrt(N))+1):
    if N % a == 0:
        b = N // a
        k = max([len(str(a)), len(str(b))])
        if min_k > k:
            min_k = k

print(min_k)

