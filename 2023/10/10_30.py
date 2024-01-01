# 1287 할 수 있다
import sys

mathical_string = sys.stdin.readline()[:-1]
mathical_arr = []
num = ""
for c in mathical_string:
    if c.isdecimal():
        num += c
    else:
        if len(num) != 0:
            mathical_arr.append(int(num))
            num = ""
        mathical_arr.append(c)
if len(num) != 0:
    mathical_arr.append(int(num))
    num = ""
# 주어진 식을 숫자와 기호로 parsing


def Error():  # 잘못된 식이 들어왔을 때 ROCK을 출력하고 프로그램 종료
    print("ROCK")
    exit()


parenthesis = 0  # 괄호가 적절히 사용된 식인지 사전에 점검
for i in mathical_arr:
    if i == "(":
        parenthesis += 1
    elif i == ")":
        parenthesis -= 1
        if parenthesis < 0:
            Error()


def Expr(expr):  # +와 -로 이루어진 식에 대한 계산
    if len(expr) == 0:
        Error()
    stack = []
    arr = []
    for i in expr:
        if i not in ["+", "-"]:
            stack.append(i)
        else:
            arr.append(Value(stack))
            arr.append(i)
            stack = []
    arr.append(Value(stack))
    curr = 0
    calculate = ""
    Flag = False
    for i in arr:
        if i in ["+", "-"]:
            if Flag == False:
                Error()
            calculate = i
            Flag = False
        else:
            if Flag == True:
                Error()
            if calculate == "":
                curr = i
            elif calculate == "+":
                curr = curr + i
                calculate = ""
            elif calculate == "-":
                curr = curr - i
                calculate = ""
            Flag = True
    if calculate != "":
        Error()
    return curr


def Value(value):  # *와 /로 이루어진 식에 대한 계산
    if len(value) == 0:
        Error()
    curr = 0
    calculate = ""
    Flag = False
    for i in value:
        if i in ["*", "/"]:
            if Flag == False:
                Error()
            calculate = i
            Flag = False
        else:
            if Flag == True:
                Error()
            if calculate == "":
                curr = i
            elif calculate == "*":
                curr = curr * i
                calculate = ""
            elif calculate == "/":
                if i == 0:
                    Error()
                curr = curr // i
                calculate = ""
            Flag = True
    if calculate != "":
        Error()
    return curr


def Parenthesis(parent):  # 주어진 식에서 괄호를 하나씩 계산하는 함수
    if len(parent) == 0:
        Error()
    arr = []
    stack = []
    Flag = False
    count = 0
    for i in parent:
        if Flag == False:
            if i != "(":
                arr.append(i)
            else:
                Flag = True
                count += 1
        else:
            if (i != "(") & (i != ")"):
                stack.append(i)
            elif i == "(":
                stack.append(i)
                count += 1
            elif i == ")":
                count -= 1
                if count == 0:
                    Flag = False
                    arr.append(Parenthesis(stack))
                    stack = []
                else:
                    stack.append(i)
    return Expr(arr)


print(Parenthesis(mathical_arr))
