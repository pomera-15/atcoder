n, k = map(int, input().split())

a = [1 for _ in range(n + 1)]

# s = a[n-k]+...+a[n-1] として累積和を持つ
s = k
for i in range(k, n + 1):
    a[i] = s
    # a[i+1]の値を求める( a[i+1] = a[i] + s - a[i-k] )
    s += a[i]
    s -= a[i-k]
    s %= 10**9

# print(a[-1]%10**9) # ここだと遅い
print(a[-1])