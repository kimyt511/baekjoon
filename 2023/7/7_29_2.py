from queue import Queue


def goldenMinsooNum(n):
    if n == 1:
        return 2
    elif n == 2:
        return 6
    elif n == 3:
        return 14
    elif n == 4:
        return 30
    elif n == 5:
        return 62
    elif n == 6:
        return 126
    else:
        return 0


goldenMinsoo = [
    4,
    7,
    44,
    47,
    74,
    77,
    444,
    447,
    474,
    477,
    744,
    747,
    774,
    777,
    4444,
    4447,
    4474,
    4477,
    4744,
    4747,
    4774,
    4777,
    7444,
    7447,
    7474,
    7477,
    7744,
    7747,
    7774,
    7777,
    44444,
    44447,
    44474,
    44477,
    44744,
    44747,
    44774,
    44777,
    47444,
    47447,
    47474,
    47477,
    47744,
    47747,
    47774,
    47777,
    74444,
    74447,
    74474,
    74477,
    74744,
    74747,
    74774,
    74777,
    77444,
    77447,
    77474,
    77477,
    77744,
    77747,
    77774,
    77777,
    444444,
    444447,
    444474,
    444477,
    444744,
    444747,
    444774,
    444777,
    447444,
    447447,
    447474,
    447477,
    447744,
    447747,
    447774,
    447777,
    474444,
    474447,
    474474,
    474477,
    474744,
    474747,
    474774,
    474777,
    477444,
    477447,
    477474,
    477477,
    477744,
    477747,
    477774,
    477777,
    744444,
    744447,
    744474,
    744477,
    744744,
    744747,
    744774,
    744777,
    747444,
    747447,
    747474,
    747477,
    747744,
    747747,
    747774,
    747777,
    774444,
    774447,
    774474,
    774477,
    774744,
    774747,
    774774,
    774777,
    777444,
    777447,
    777474,
    777477,
    777744,
    777747,
    777774,
    777777,
]


# num = int(input())
def gms(num):
    que = Queue()
    que.put((0, num))
    dict = [0] * num
    reach = [-1] * (num + 1)
    flag = True
    while (not que.empty()) & flag:
        minimum, left = que.get()
        for i in range(goldenMinsooNum(len(str(left)))):
            minsoo_num = goldenMinsoo[i]
            if minsoo_num < minimum:
                continue
            elif left == minsoo_num:
                reach[left - minsoo_num] = left
                flag = False
            elif left > minsoo_num:
                if dict[left - minsoo_num] == 0:
                    dict[left - minsoo_num] = 1
                    reach[left - minsoo_num] = left
                    que.put(
                        (
                            minsoo_num,
                            left - minsoo_num,
                        )
                    )
    if reach[0] == -1:
        print(-1)
    else:
        stack = []
        num = 0
        while reach[num] != -1:
            stack.append(reach[num] - num)
            num = reach[num]
        print(" ".join(list(map(str, (list(reversed(stack)))))))


for i in range(20000):
    gms(i)
