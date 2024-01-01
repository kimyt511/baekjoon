words = [
    "caaaaa",
    "aaaaaaaaa",
    "a",
    "bbb",
    "bbbbbbbbb",
    "bbb",
    "cc",
    "cccccccccccc",
    "ccccccc",
    "ccccccc",
    "cc",
    "cccc",
    "c",
    "cccccccc",
    "c",
]

if len(words) == 1:
    print(True)
    exit()
arr = [0] * 26
for word in words:
    for c in word:
        arr[ord(c) - 97] += 1
max_val = max(arr)
print(arr)
print(all([(i == 0) | (i == max_val) for i in arr]) & (max_val % len(words) == 0))
