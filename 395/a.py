N = int(input())
A_list = list(map(int, input().split()))

ans = "Yes"
for i in range(N-1):
    if A_list[i] >= A_list[i+1]:
        ans = "No"
        break

print(ans)