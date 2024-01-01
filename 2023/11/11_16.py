import sys

X, G = list(map(int,sys.stdin.readline().split()))
if X == G:
    print(0)
    exit()
def sum_(n):
    val = 0
    for c in str(n):
        val += int(c)
    return val

def prod(n):
    val = 1
    for c in str(n):
        val *= int(c)
    return val

def prod3(n):
    if len(str(n)) < 3:
        return prod(n)
    arr = sorted(list(str(n)), reverse=True)
    val = 1
    for i in range(3):
        val *= int(arr[i])
    return val

def smallest(n):
    val = 10
    for c in str(n):
        if int(c) < val:
            val = int(c)
    return val

def first(n):
    return int(str(n)[0])

def dot(a,b):
    return 5*prod3(a) + first(a)*sum_(b) + smallest(b)

ans = -1
correct_num_arr = [X]
count_dic = {X:0}
dp = {}
correct_num_len = 1

while ans == -1:
    possible = False
    for i in range(correct_num_len):
        for j in range(correct_num_len):
            if (correct_num_arr[i], correct_num_arr[j]) not in dp:
                dp[(correct_num_arr[i], correct_num_arr[j])] = 1
                val = dot(correct_num_arr[i], correct_num_arr[j])
                count = count_dic[correct_num_arr[i]] + count_dic[correct_num_arr[j]] + 1
                if val == G:
                    ans = count
                if val not in count_dic:
                    correct_num_arr.append(val)
                    count_dic[val] = count
                    correct_num_len += 1
                    possible = True
    if possible == False:
        break

print(ans)