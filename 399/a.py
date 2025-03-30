N = int(input())
S = str(input())
T = str(input())

diff_cnt = len(list(filter(lambda x: x[0] != x[1], zip(S, T))))
print(diff_cnt)
