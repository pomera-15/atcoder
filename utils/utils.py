def amari_kiriage(a, b):
    """
    余りを切り上げる
    例）17 人を 3 人ずつグループに分けて、余ったところは 1 つのグループとしたときに何グループできるか
    a が b で割り切れるとき: a/b
    a が b で割り切れないとき: a/b + 1
    """
    return int((a + b - 1) / b)


def is_integer(n: int):
    """
    整数かどうかを判定する(1で割ったときの余りが0かどうか)
    """
    if n % 1 == 0:
        return True
    else:
        return False


import math
def distance(p1:list, p2:list):
    """
    N次元空間における2点間のユークリッド距離を求める
    """
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(p1, p2)))


def is_triangle(a: float, b: float, c: float) -> bool:
    """
    三辺の長さ a, b, c が与えられたとき、それらが三角形を形成できるか判定する。
    """
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)


def is_all_unique(*args) -> bool:
    """
    引数がすべて異なる値である場合に True を返す。
    """
    return len(args) == len(set(args))


def sum_each_digit(n: int):
    """
    nの各桁の和を求める
    """
    sum = 0
    while n > 0:
        sum += n % 10
        n = int(n / 10)
    return sum


def is_kaibun(s: str):
    """
    回文かどうかを判定する
    """
    s = list(s)
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True


def to_base_k(n:int, k:int):
    """
    nをk進数に変換する
    """
    res = ""
    while n > 0:
        res = str(n % k) + res
        n = n // k
    return int(res)