n, d = map(int, input().split())
s = input()

cnum = s.count("@")
knum = s.count(".")

print(knum + d)