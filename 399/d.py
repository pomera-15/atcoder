T = int(input())
res = []
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    # カップルごとの位置を取得する
    position = [[] for _ in range(N + 1)]
    for i in range(N*2):
        position[A[i]].append(i)
    # print(f"positon:{position}")
    # positon:[[], [0, 4], [1, 5], [2, 3]]

    answer_pair = set()
    for i in range(N*2 - 1):
        a = A[i]
        b = A[i+1]
        # 隣り合っていたら中断
        if position[a][0] + 1 == position[a][1]:
            continue
        if position[b][0] + 1 == position[b][1]:
            continue
        # ...ab...ab... or ...ab...ba...かどうか
        v = [position[a][0], position[a][1], position[b][0], position[b][1]]
        v.sort()
        if v[0] + 1 == v[1] and v[2] + 1 == v[3]:
            answer_pair.add(tuple(sorted((a, b))))

    res.append(len(answer_pair))

for r in res:
    print(r)