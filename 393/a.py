# 高橋くん 1 2
# 青木くん 1 3
s1, s2 = map(str, input().split())

if s1 == "sick" and s2 == "sick":
    print(1)
elif s1 == "fine" and s2 == "sick":
    print(3)
elif s1 == "sick" and s2 == "fine":
    print(2)
elif s1 =="fine" and s2 == "fine":
    print(4)
