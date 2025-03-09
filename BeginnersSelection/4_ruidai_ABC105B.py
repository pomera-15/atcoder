N = int(input())

res = "No"
for x in range(0, N+1):
    for y in range(0, N+1):
        if 4*x + 7*y == N:
            res = "Yes"
            break
    
print(res)