def is_kaibun(s: str):
    """
    回文かどうかを判定する
    """
    s = list(s)
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True


A, B = map(int, input().split())

res = 0
for n in range(A, B+1):
    if is_kaibun(str(n)):
        res += 1

print(res)
