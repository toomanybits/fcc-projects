def arithmetic_arranger(problems, sol=None):
    if len(problems)>5:
        quit()
    else:
        noeq = len(problems)
    
    upeq = list()
    opeq = list()
    boteq = list()
    space = list()
    n=0
    
    for problem in problems:
        #to make argument accessible
        up, operator, down = problem.split()
        #to find the longest operand
        if len(up)>len(down):
            n = len(up)
        else:
            n = len(down) 
        
        up = int(up)
        down = int(down)
        
        upeq.append(up)
        opeq.append(operator)
        boteq.append(down)
        space.append(n)
    
    #making list of formated problems
    str1 = [f"{upeq[i] :>{space[i]+2}}" for i in range(noeq)]
    str2 = [f"{opeq[j]} {boteq[j] :>{space[j]}}" for j in range(noeq)]

    #for printing dashes
    str3 = ["_"*(space[k]+2) for k in range(noeq)]

    #printing solution of the problem
    str4 = list()
    if sol==True:
        for l in range(noeq):
            if opeq[l]=="+":
                ans = upeq[l] + boteq[l]
            else:
                ans = upeq[l] - boteq[l]
            str4.append(f"{ans :>{space[l]+2}}")

    if str4!=None:
        arranged_problems = "    ".join(str1) + "\n" + "    ".join(str2) + "\n" + "    ".join(str3) + "\n" + "    ".join(str4)
    else:
        arranged_problems = "    ".join(str1) + "\n" + "    ".join(str2) + "\n" + "    ".join(str3)
    return arranged_problems

if __name__ == "__main__":
    #arithmetic_arranger(["3801 - 2", "938 + 84"], True)
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
