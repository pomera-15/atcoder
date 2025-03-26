a, b, c, x, y = map(int, input().split())

sum = 0
while x > 0 or y > 0:
    # AとBどちらも必要な場合
    # A+Bを買う場合と2Cを買う場合で安い方を採用する
    if x > 0 and y > 0:
        if a + b >= c * 2:
            x -= 1
            y -= 1
            sum += c * 2
        else:
            x -= 1
            y -= 1
            sum += a + b
    # Aだけが必要な場合
    # Aを買う場合と2Cを買う場合で安い方を採用する
    elif x > 0 and y <= 0:
        if a > c * 2:
            x -= 1
            sum += c * 2
        else:
            x -= 1
            sum += a
    # Bだけが必要な場合
    # Bを買う場合と2Cを買う場合で安い方を採用する
    elif x <= 0 and y > 0:
        if b > c * 2:
            y -= 1
            sum += c * 2
        else:
            y -= 1
            sum += b

print(sum)