while True:
    s = input()
    if s == ".":
        break
    stack = []
    flag = True
    for i in list(s):
        if i == "(" or i == "[":
            stack.append(i)
        if i == ")" or i == "]":
            if len(stack) != 0:
                if (i == ")" and stack.pop() != "(") or (i == "]" and stack.pop() != "["):
                    flag = False
            else:
                flag = False
    if len(stack) > 0:
        flag = False
    print("yes" if flag else "no")
