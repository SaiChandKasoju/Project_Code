
inter=['[ a  b  c ]', '[ d  e  f ]', '[ g  h  i ]']
options='a, b, c, d, e, f, g, h, i'
print("Hello there! Welcome to Tic-Tac-Toe")
print()

def player(name, key):
    inp=input(name.title()+ " Please choose an option - ")
    for j in range(len(inter)):
        if inp in inter[j] and options:
            s=inter[j]
            s=s.replace(inp, key)
            inter[j]=s
    return print("\n".join(inter))
def computer():


inter=['[ a  b  c ]', '[ d  e  f ]', '[ g  h  i ]']
options='a, b, c, d, e, f, g, h, i'
print("Hello there! Welcome to Tic-Tac-Toe")
print()
play=input("Enter '1' to play with Computer or '2' to play 2-player game : ")

pl1=input('Enter Player1 Name : ')
pl2=input('Enter Player2 Name : ')
print("Observe the interface below.")
print("\n".join(inter))
print("Now choose your option from %s" % options)
win=0
i=0
crit1='O O O' 
crit2='X X X'
while win==0:
    if (i%2)==0 and win==0:
        
        for j in range(len(inter)):
            if inp in inter[j]:
                s=inter[j]
                s=s.replace(inp, 'O')
                inter[j]=s
    elif (i%2)!=0 and win==0:
        inp=input(pl2.title()+ " Please choose an Option - ")
        for j in range(len(inter)):
            if inp in inter[j]:
                s=inter[j]
                s=s.replace(inp, 'X')
                inter[j]=s
    print("\n".join(inter))
    print()
    i+=1
    ho1=inter[0][2]+" "+inter[0][5]+" "+inter[0][8]
    ho2=inter[1][2]+" "+inter[1][5]+" "+inter[1][8]
    ho3=inter[2][2]+" "+inter[2][5]+" "+inter[2][8]
    di1=inter[0][2]+" "+inter[1][5]+" "+inter[2][8]
    di2=inter[0][8]+" "+inter[1][5]+" "+inter[2][2]
    ve1=inter[0][2]+" "+inter[1][2]+" "+inter[2][2]
    ve2=inter[0][5]+" "+inter[1][5]+" "+inter[2][5]
    ve3=inter[0][8]+" "+inter[1][8]+" "+inter[2][8]
    if ho1==crit1 or ho1==crit2 or ho2==crit1 or ho2==crit2 or ho3==crit1 or ho3==crit2 or di1==crit1 or di1==crit2 or  di2==crit1 or di2==crit2 or ve1==crit1 or ve1==crit2 or ve2==crit1 or ve2==crit2 or ve3==crit1 or ve3==crit2 :
        if ho1==crit1 or ho2==crit1 or ho3==crit1 or di1==crit1 or di2==crit1 or ve1==crit1 or ve2==crit1 or ve3==crit1 :
            print()
            print("Hurrah! %s has won." %pl1)
            print("Better luck next time %s." %pl2)
            print()
        if ho1==crit2 or ho2==crit2 or ho3==crit2 or di1==crit2 or di2==crit2 or ve1==crit2 or ve2==crit2 or ve3==crit2 :
            print()
            print("Hurrah! %s has won." %pl2)
            print("Better luck next time %s." %pl1)
            print()
        print("Do you want to play again")
        play=input("Enter 'y' if yes or Press any key to end the game : ")
        if play!='y':
            print()
            print("Game End".center(30, "-"))
            break
        else:
            inter=['[ a  b  c ]', '[ d  e  f ]', '[ g  h  i ]']
