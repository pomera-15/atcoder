N, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

res = 0
for a in A:
    # xからaを出せるなら満足する子供は+1
    if x - a >= 0:
        res += 1
    x -= a

# もしresが1以上で最後にxが余っていたら最後の子は満足していない
if res >= 1 and x > 0:
    res -= 1

print(res)