N = int(input())
A = list(map(int, input().split()))

b = ""
cnt = 1
for a in A:

    # 連続しているか判定
    if a == b:
        cnt += 1
    else:
        cnt = 1

    # 3回連続している場合はYes
    if cnt >= 3:
        print("Yes")
        exit()

    b = a

print("No")
