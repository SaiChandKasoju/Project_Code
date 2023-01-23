def arithmetic_arranger(problems):
    x=[]
    y=[]
    if 'True' in problems:
        a=problems[1]
        problems=problems[0]
    for i in problems:
        if '+' in i:
            x.append(i.split("+"))
            y.append("+")
        elif '-' in i:
            x.append(i.split("-"))
            y.append("-")
    

      
    

    return x, y
    #return arranged_problems


out=arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print(out)
