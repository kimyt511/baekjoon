import sys

N, M = list(map(int, sys.stdin.readline().split()))
material = {}
for i in range(N):
    name, cost = sys.stdin.readline().split()
    material[name] = int(cost)
recipes = {}
for i in range(M):
    name, rec = sys.stdin.readline().split("=")
    material_arr = []
    for m in rec.split("+"):
        material_name = ""
        material_cost = ""
        for c in m:
            if c.isdigit():
                material_cost = material_cost + c
            elif c.isalnum():
                material_name = material_name + c
        if material_name == name:
            material_arr.append(-1)
        else:
            material_arr.append((material_name, int(material_cost)))
    if material_arr.count(-1) == 0:
        if name not in recipes:
            recipes[name] = []
        recipes[name].append(material_arr)

dp = {}


def getCost(name, node):
    if (name not in recipes) & (name not in material):
        return -1
    if name in dp:
        return dp[name]
    cost = 1000000002
    if name in material:
        cost = min(cost, material[name])
    if name in recipes:
        for recipe in recipes[name]:
            material_cost_arr = []
            for i in recipe:
                if i[0] not in node:
                    _node = [i for i in node]
                    _node.append(name)
                    material_cost = getCost(i[0], _node)
                    if material_cost * i[1] > 1000000000:
                        material_cost_arr.append(1000000001)
                    elif material_cost != -1:
                        material_cost_arr.append(material_cost * i[1])
                    else:
                        material_cost_arr.append(-1)
                elif i[0] in material:
                    material_cost_arr.append(material[i[0]] * i[1])
                else:
                    material_cost_arr.append(-1)
            if material_cost_arr.count(-1) != 0:
                if cost == 1000000002:
                    cost = -1
            else:
                cost = min(cost, sum(material_cost_arr))
    dp[name] = cost
    return cost


print(getCost("LOVE", []))
