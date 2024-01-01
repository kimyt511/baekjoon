times = int(input())


class Node:
    def __init__(self, coor, next=None):
        self.coor = coor
        self.next = next

    def add_data(self, node):
        while self.next != None:
            self = self.next
        self.next = node


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def organicCabbage():
    _, _, cabbage_num = input().split()
    cabbage_list = []
    for _ in range(int(cabbage_num)):
        x, y = input().split()
        coor = Coordinate(int(x), int(y))
        parent_node = None
        for node in cabbage_list:
            if checkNode(node, coor) == True:
                if parent_node == None:
                    parent_node = node
                else:
                    parent_node.add_data(node)
                    cabbage_list.remove(node)
        if parent_node == None:
            cabbage_list.append(Node(coor))
        else:
            parent_node = None

    return len(cabbage_list)


def checkNode(node, coor):
    while node != None:
        if isNeighbor(node.coor, coor):
            node.add_data(Node(coor))
            return True
        elif node.next != None:
            node = node.next
        else:
            node = None
    return False


def isNeighbor(coor1, coor2):
    if (coor1.x == coor2.x) & (abs(coor1.y - coor2.y) == 1):
        return True
    elif (coor1.y == coor2.y) & (abs(coor1.x - coor2.x) == 1):
        return True
    else:
        return False


for _ in range(times):
    print(organicCabbage())
