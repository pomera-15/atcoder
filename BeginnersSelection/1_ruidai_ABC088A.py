N = int(input())
A = int(input())

# 500円玉で払えない金額を求める
num = N % 500

# num が手持ちの1円玉で払えるかどうか
if num <= A:
    print("Yes")
else:
    print("No")
    