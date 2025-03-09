N = int(input())
L = list(map(int, input().split()))

res = 0
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            # 同じ長さの辺がある場合は条件を満たさない
            if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                continue
            else:
                # 三角形が成立する場合はres++
                if (L[i] + L[j] > L[k]) and (L[j] + L[k] > L[i]) and (L[k] + L[i] > L[j]):
                    res += 1

print(res)