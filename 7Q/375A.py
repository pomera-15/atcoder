N = int(input())
S = input()

res = 0
for s1, s2, s3 in zip(S[0:-2], S[1:-1], S[2:]):
    if s1 == "#" and s2 == "." and s3 == "#":
        res += 1 

print(res)