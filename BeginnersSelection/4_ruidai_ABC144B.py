N = int(input())

res = "No"
for x in range(1,10):
    for y in range(1,10):
        if x*y == N:
            res = "Yes"
            break

print(res)