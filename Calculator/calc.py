from calculator import *
while True:
    try:
        x=int(input('- '))
        operation=input('- ') #+,-,/,//,%,*,**
        y=int(input('- '))
        if operation=='+':
            print(add(x,y))
        elif operation=='-':
            print(sub(x,y))
        elif operation=='/':
            print(div(x,y))
        elif operation=='//':
            print(div_without_float(x,y))
        elif operation=='%':
            print(remainder(x,y))
        elif operation=='*':
            print(multiply(x,y))
        elif operation=='**':
            print(power(x,y))
    except:
        print('Something went wrong! Please try again.')
        break