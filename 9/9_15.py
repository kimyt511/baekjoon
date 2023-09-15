# 1036 36진수
import sys

N = int(sys.stdin.readline())
word_arr = []
for _ in range(N):
    word_arr.append(sys.stdin.readline()[:-1])
K = int(sys.stdin.readline())
delta_arr = [0] * 36


def tenToThirtySix(num):
    if num < 10:
        return str(num)
    else:
        return chr(55 + num)


def thirtySixToTen(charc):
    if ord(charc) in range(48, 58):
        return int(charc)
    else:
        return ord(charc) - 55


for i in range(36):
    charcter = tenToThirtySix(i)
    for word in word_arr:
        for j in range(len(word)):
            if word[j] == charcter:
                delta_arr[i] += (35 - i) * (36 ** (len(word) - j - 1))

changing_char = []
for _ in range(K):
    idx = delta_arr.index(max(delta_arr))
    delta_arr[idx] = -1
    changing_char.append(tenToThirtySix(idx))
new_word_arr = []
for word in word_arr:
    arr = list(word)
    for i in range(len(arr)):
        if arr[i] in changing_char:
            arr[i] = "Z"
    new_word_arr.append("".join(arr))


def addWord(word1, word2):
    arr1 = list(reversed(list(word1)))
    arr2 = list(reversed(list(word2)))
    arr = []
    up = False
    for i in range(max(len(arr1), len(arr2))):
        if (i in range(len(arr1))) & (i in range(len(arr2))):
            num = thirtySixToTen(arr1[i]) + thirtySixToTen(arr2[i])
        elif i in range(len(arr1)):
            num = thirtySixToTen(arr1[i])
        else:
            num = thirtySixToTen(arr2[i])
        if up:
            num += 1
            up = False
        if num > 35:
            num -= 36
            up = True
        arr.append(tenToThirtySix(num))
    if up:
        arr.append("1")
    return "".join(reversed(arr))


sum = ""
for word in new_word_arr:
    sum = addWord(sum, word)

print(sum)
