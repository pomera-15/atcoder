N = int(input())
A_list = list(map(int, (input().split())))

A_list.sort(reverse=True)

Alice_sum = 0
Bob_sum = 0
for i, a in enumerate(A_list, 1):
    if i % 2 != 0:
        Alice_sum += a
    else:
        Bob_sum += a

print(Alice_sum - Bob_sum)