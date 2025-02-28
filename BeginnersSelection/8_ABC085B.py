N = int(input())

d = []
for i in range(N):
    d.append(int(input()))

d = list(set(d))
d.sort(reverse=True)

print(len(d))