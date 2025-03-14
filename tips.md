# python tips
## range
```
range(start, stop[, step])
```
いつも忘れる。

## pythonでのAtcoder的入力の書き方
1行で1単語
```
# N
N = int(input())
```

1行で複数単語(固定の数)
```
# N, K
N, K = map(int, input().split())
```

1行で複数単語(任意の数)
```
# n1 n2 n3 n4 n5
N = list(map(int, input().split())) 
```

複数行で複数単語(個数は事前に指定される)
```
# N
# l1
# l2
# l3
# l4
# l5
L = []
for _ in range(N):
    L.append(int(input()))
```

# AGC012A: AtCoder Group Contest
> 3N個の整数から3個ずつのペアを作る。  
> このとき、ペアリングのスコアは各ペアにおける2番目に大きい数の総和とすると、総和はどのようにすれば最大化できるか。  

`12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1`  
で考えると、  
`12, 11, x`  
`10, 9, x`  
`8, 7, x`  
`6, 5, x`  
として、`11+9+7+5=32`だ最大となる。  
※ この考え方が思いつかなかった。  

