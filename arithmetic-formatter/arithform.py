def arithmetic_arranger(problem, sol=None):
    #to make argument accessible
    up, operator, down = problem.split()
    #to find the longest operand
    if len(up)>len(down):
        n = len(up)
    else:
        n = len(down) 
    
    up = int(up)
    down = int(down)
    
    #priting formated problem
    print(f"{up :>{n+2}}")
    print(f"{operator} {down :>{n}}")

    # for printing dashes
    [print("_", end="") for i in range(n+2)]
    print("")

    #printing solution of the problem
    if sol==True:
        if operator=="+":
            ans = up+down
        else:
            ans = up-down
        print(f"{ans :>{n+2}}")
#return arranged_problems

if __name__ == "__main__":
    arithmetic_arranger("3801 - 2", True)
    arithmetic_arranger("1 - 3801", True)
    arithmetic_arranger("32 + 69")
