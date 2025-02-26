N, A, B = input().split()
N, A, B = int(N), int(A), int(B)

ans = 0
for i in range(1,N+1):
    i_digit_list = list(map(int, list(str(i))))
    i_digit_sum = sum(i_digit_list)
    if A <= i_digit_sum and i_digit_sum <= B:
        ans += i

print(ans)