a, b, c = map(int, input().split())

if a+b==c or b+c==a or c+a==b or a==b==c:
    print("Yes")
else:
    print("No")
