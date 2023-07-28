def arithmetic_arranger(problems, sol=None):
    #check whether arguments are more than five or not
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        noeq = len(problems)

    upeq = list()
    opeq = list()
    boteq = list()
    space = list()
    n = 0

    for problem in problems:
        # to make argument accessible
        up, operator, down = problem.split()
        # to find the longest operand
        if len(up) > len(down):
            n = len(up)
        else:
            n = len(down)

        upeq.append(up)
        opeq.append(operator)
        boteq.append(down)
        space.append(n)

    # check operator are onli "+" or "-"
    if "*" in opeq or "/" in opeq:
        return "Error: Operator must be '+' or '-'."

    # check the digits
    for i in range(len(space)):
        if not (upeq[i].isdigit() and boteq[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # check if digit more than 4
    for i in range(len(space)):
        if space[i] > 4:
            return "Error: Numbers cannot be more than four digits."

    # making list of formated problems
    str1 = [f"{upeq[i] :>{space[i]+2}}" for i in range(noeq)]
    str2 = [f"{opeq[j]} {boteq[j] :>{space[j]}}" for j in range(noeq)]

    # for printing dashes
    str3 = ["-" * (space[k] + 2) for k in range(noeq)]

    # printing solution of the problem
    str4 = list()
    if sol == True:
        for l in range(noeq):
            if opeq[l] == "+":
                ans = int(upeq[l]) + int(boteq[l])
            else:
                ans = int(upeq[l]) - int(boteq[l])
            str4.append(f"{ans :>{space[l]+2}}")

    if str4 != []:
        arranged_problems = (
            "    ".join(str1)
            + "\n"
            + "    ".join(str2)
            + "\n"
            + "    ".join(str3)
            + "\n"
            + "    ".join(str4)
        )
    else:
        arranged_problems = (
            "    ".join(str1)
            + "\n"
            + "    ".join(str2) 
            + "\n"
            + "    ".join(str3)
        )
    return arranged_problems

