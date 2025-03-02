s = str(input())

# 入力が空文字の場合は考えない
if s == "":
    print("NO")
    exit()

# 回答
yes_or_no = "YES"

"""
sの先頭から
dreameraser,dreamerase,
dreamer,dream
eraser,erase
のどれかに一致するかを判定し、一致する場合は該当の部分を削除する。
一致しない場合は"NO"として終了。

sがなくなるまで繰り返し、"NO"にならない場合は全て
dream,dreamer,erase,eraser
で構成されるということのため"Yes"を返す
"""
while s != "":

    if s[:10] == "dreamerase":
        if s[10:11] == "r":
            # dreameraser
            s = s[11:]
        else:
            # dreamerase
            s = s[10:]

    elif s[:5] == "dream":
        if s[5:7] == "er":
            # dreamer
            s = s[7:]
        else:
            # dream
            s = s[5:]

    elif s[:5] == "erase":
        if s[5:6] == "r":
            # eraser
            s = s[6:]
        else:
            # erase
            s = s[5:]
    else:
        # NG
        yes_or_no = "NO"
        break

print(yes_or_no)
