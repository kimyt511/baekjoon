import sys

x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))


def addarr(arr1, arr2):
    arr = [0] * len(arr1)
    for i in range(len(arr1)):
        arr[i] = arr1[i] + arr2[i]
    return arr


def mularr(arr, num):
    new_arr = [0] * len(arr)
    for i in range(len(arr)):
        new_arr[i] = arr[i] * num
    return new_arr


def tileType(x, y):
    return (x / 5 + y / 5) % 2


def checkCorner(x, y):
    return (x % 5 == 0) & (y % 5 == 0)


def countTile(a, b, c, d):
    horizontal = tileType((a // 5) * 5, (b // 5) * 5)
    arr = [0] * 6
    if (a >= c) | (b >= d):
        return arr
    if horizontal:
        arr[d - b] = c - a
    else:
        arr[c - a] = d - b
    return arr


def countEdge(a, b, c, d):
    vertical_edge = (d - b) < 5
    tilenum = int((c - a) / 5) if vertical_edge else int((d - b) / 5)
    first_arr = (
        countTile(a, b, (a // 5) * 5 + 5, d)
        if vertical_edge
        else countTile(a, b, c, (b // 5) * 5 + 5)
    )
    second_arr = (
        countTile((a // 5) * 5 + 5, b, (a // 5) * 5 + 10, d)
        if vertical_edge
        else countTile(a, (b // 5) * 5 + 5, c, (b // 5) * 5 + 10)
    )
    if tilenum % 2 == 0:
        return addarr(mularr(first_arr, tilenum / 2), mularr(second_arr, tilenum / 2))
    else:
        return addarr(
            addarr(mularr(first_arr, tilenum // 2), mularr(second_arr, tilenum // 2)),
            first_arr,
        )


def tiles(x1, y1, x2, y2):
    size = [0] * 6
    center_x1 = x1 if x1 % 5 == 0 else x1 // 5 * 5 + 5
    center_y1 = y1 if y1 % 5 == 0 else y1 // 5 * 5 + 5
    center_x2 = x2 if x2 % 5 == 0 else x2 // 5 * 5
    center_y2 = y2 if y2 % 5 == 0 else y2 // 5 * 5
    if center_x1 > x2:
        center_x1 = x2
    if center_y1 > y2:
        center_y1 = y2
    if center_x2 < x1:
        center_x2 = x1
    if center_y2 < y1:
        center_y2 = y1
    dic = {}
    corner1 = countTile(x1, y1, center_x1, center_y1)
    dic[(x1, y1, center_x1, center_y1)] = 1
    corner2 = (
        countTile(x1, center_y2, center_x1, y2)
        if (x1, center_y2, center_x1, y2) not in dic
        else [0] * 6
    )
    dic[(x1, center_y2, center_x1, y2)] = 1
    corner3 = (
        countTile(center_x2, y1, x2, center_y1)
        if (center_x2, y1, x2, center_y1) not in dic
        else [0] * 6
    )
    dic[(center_x2, y1, x2, center_y1)] = 1
    corner4 = (
        countTile(center_x2, center_y2, x2, y2)
        if (center_x2, center_y2, x2, y2) not in dic
        else [0] * 6
    )
    dic[(center_x2, center_y2, x2, y2)] = 1
    edge1 = (
        countEdge(center_x1, y1, center_x2, center_y1)
        if (center_x1, y1, center_x2, center_y1) not in dic
        else [0] * 6
    )
    dic[(center_x1, y1, center_x2, center_y1)] = 1
    edge2 = (
        countEdge(center_x1, center_y2, center_x2, y2)
        if (center_x1, center_y2, center_x2, y2) not in dic
        else [0] * 6
    )
    dic[(center_x1, center_y2, center_x2, y2)] = 1
    edge3 = (
        countEdge(x1, center_y1, center_x1, center_y2)
        if (x1, center_y1, center_x1, center_y2) not in dic
        else [0] * 6
    )
    dic[(x1, center_y1, center_x1, center_y2)] = 1
    edge4 = (
        countEdge(center_x2, center_y1, x2, center_y2)
        if (center_x2, center_y1, x2, center_y2) not in dic
        else [0] * 6
    )
    dic[(center_x2, center_y1, x2, center_y2)] = 1
    center = (
        int(((center_x2 - center_x1) / 5) * ((center_y2 - center_y1) / 5) * 5)
        if checkCorner(center_x1, center_y1) & checkCorner(center_x2, center_y2)
        else 0
    )
    size = addarr(size, corner1)
    size = addarr(size, corner2)
    size = addarr(size, corner3)
    size = addarr(size, corner4)
    size = addarr(size, edge1)
    size = addarr(size, edge2)
    size = addarr(size, edge3)
    size = addarr(size, edge4)
    sum = center + size[5] + size[4] + size[3]
    size[1] = size[1] - size[4]
    size[2] = size[2] - size[3]
    if size[2] < 0:
        size[1] = size[1] + 2 * size[2]
    else:
        sum = sum + (size[2] // 2)
        size[1] = size[1] - (size[2] // 2)
        size[2] = size[2] % 2
    if size[2] == 1:
        sum = sum + 1
        size[1] = size[1] - 3
    if size[1] > 0:
        sum = sum + (size[1] // 5)
        size[1] = size[1] % 5
        if size[1] > 0:
            sum = sum + 1

    print(int(sum))


tiles(x1, y1, x2, y2)
