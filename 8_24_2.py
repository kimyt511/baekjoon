import sys

N, M = list(map(int, sys.stdin.readline().split()))
material = {}
for i in range(N):
    name, cost = sys.stdin.readline().split()
    material[name] = int(cost)
recipes = []

for i in range(M):
    recipes.append(sys.stdin.readline())


def strTorecipe(string):
    name, rec = string.split("=")
    if name not in material:
        material[name] = -1
    material_arr = []
    for m in rec.split("+"):
        material_name = ""
        material_cost = ""
        for c in m:
            if c.isdigit():
                material_cost = material_cost + c
            elif c.isalnum():
                material_name = material_name + c
        if material_name not in material:
            material[material_name] = -1
        material_arr.append((material_name, int(material_cost)))
    return (name, material_arr)


for _ in range(M):
    for recipe in recipes:
        name, rec = strTorecipe(recipe)
        rec = [material[i[0]] * i[1] if material[i[0]] != -1 else -1 for i in rec]
        if rec.count(-1) == 0:
            if material[name] == -1:
                material[name] = sum(rec)
            else:
                material[name] = min(material[name], sum(rec))
if "LOVE" not in material:
    print(-1)
elif material["LOVE"] > 1000000000:
    print(1000000001)
else:
    print(material["LOVE"])
