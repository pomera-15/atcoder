N, M = map(int, input().split())

L = []
for _ in range(M):
    L.append(list(map(int, input().split())))

# N個の都市のバケツを用意する
cities = {i: 0 for i in range(1, N+1)}

for a, b in L:
    cities[a] += 1
    cities[b] += 1

for c in cities.values():
    print(c)