N = int(input())

if N % 2 ==0:
    s = "=="
else:
    s = "="

for _ in range(int((N-1)/2)):
    s = "-" + s + "-"

print(s)
