a = input().strip()
priority = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}
stack = []
result = []
try:
    if a.find("()") != -1:
        raise
    asd = ""
    for i in a:
        if i == "(":
            if asd != "":
                result.append(asd)
                asd = ""
            stack.append(i)
        elif i == ")":
            if asd != "":
                result.append(asd)
                asd = ""
            while stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
        elif i == "+" or i == "-" or i == "*" or i == "/":
            if asd != "":
                result.append(asd)
                asd = ""
            if not result:
                raise
            while stack:
                if priority[stack[-1]] >= priority[i]:
                    result.append(stack.pop())
                else:
                    break
            stack.append(i)
        else:
            asd += i
    if asd != "":
        result.append(asd)
    while stack:
        if stack[-1] == "(" or stack[-1] == ")":
            raise
        else:
            result.append(stack.pop())
    stack = []
    for i in result:
        if i == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
        else:
            stack.append(int(i))
    if len(stack) != 1:
        raise
    print(stack[0])
except:
    print("ROCK")
    exit()
