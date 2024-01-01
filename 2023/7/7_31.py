num, E, W, N, S = input().split(" ")
E = int(E) / 100
W = int(W) / 100
N = int(N) / 100
S = int(S) / 100
stack = []


def move(route, v, node, curr):
    currX, currY = curr
    node = node.copy()
    if v == "E":
        currX = currX + 1
    elif v == "W":
        currX = currX - 1
    elif v == "N":
        currY = currY - 1
    else:
        currY = currY + 1

    if (currX, currY) not in node:
        if len(route) + 1 == int(num):
            stack.append(route + v)
        else:
            node[(currX, currY)] = 1
            move(route + v, "E", node, (currX, currY))
            move(route + v, "W", node, (currX, currY))
            move(route + v, "N", node, (currX, currY))
            move(route + v, "S", node, (currX, currY))


move("", "E", {(0, 0): 1}, (0, 0))
move("", "W", {(0, 0): 1}, (0, 0))
move("", "N", {(0, 0): 1}, (0, 0))
move("", "S", {(0, 0): 1}, (0, 0))

sum = 0
for route in stack:
    p = 1
    for v in route:
        if v == "E":
            p = p * E
        elif v == "W":
            p = p * W
        elif v == "N":
            p = p * N
        else:
            p = p * S
    sum = sum + p

print(sum)
