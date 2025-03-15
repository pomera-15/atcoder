S = str(input())

# 末尾がiの場合はoを挿入するためres=1とする
if S[-1] == "i":
    res = 1
else:
    res = 0

#t: 次に現れるべき文字
t = "i"

for i, s in enumerate(S, 1):

    if s == t:
        if t == "i":
            t = "o"
        else:
            t = "i"
    else:
        res += 1

print(res)