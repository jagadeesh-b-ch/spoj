for i in range(int(input())):
    exp = input()
    ops = []
    rpnExp = ""
    for char in exp:
        if char == "(":
            continue
        elif char == ")":
            rpnExp = rpnExp + ops.pop()
        elif char == "+" or char == "-" or char == "*" or char == "/" or char == "^":
            ops.append(char)
        else:
            rpnExp = rpnExp + char
    print(rpnExp)
