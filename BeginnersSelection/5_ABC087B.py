
A = int(input()) # 500
B = int(input()) # 100
C = int(input()) # 50
X = int(input())

ans = 0
for i in range(0, A+1):
    for j in range(0, B+1):
        for k in range(0, C+1):
            if (500 * i + 100 * j + 50 * k) == X:
                ans += 1

print(ans)
