
# 余りを切り上げる
# 例）17 人を 3 人ずつグループに分けて、余ったところは 1 つのグループとしたときに何グループできるか
# a が b で割り切れるとき: a/b
# a が b で割り切れないとき: a/b + 1
def amari_kiriage(a, b):
    return int((a + b - 1) / b)
