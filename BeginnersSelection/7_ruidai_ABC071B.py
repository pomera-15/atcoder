s = str(input())
alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }

# 1 - 26のバケツを用意する
buckets = {i: False for i in range(1, 27)}

# sに現れるアルファベットをバケツに入れる
for c in s:
    buckets[alphabet[c]] = True

# sに現れていないアルファベットで辞書順で最も小さいものを探す
for key, value in alphabet.items():
    if buckets[value] == False:
        print(key)
        exit()

# 全て使っていたときはNoneを出力する
print("None")
