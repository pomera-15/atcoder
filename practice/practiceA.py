# ex)
# input
# 1
# 2 3
# test
#
# output 
# 6 test

a = input()
b, c = input().split(" ")
s = input()

print(f"{int(a)+int(b)+int(c)} {s}")
