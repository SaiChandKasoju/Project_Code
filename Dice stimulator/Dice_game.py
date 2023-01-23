import random

def dice(inp):
    inp="y"
    while inp=="y":
        num = random.randint(1,6)
        if inp=="y":
            if num == 1:
                print("Dice".center(7, " "))
                print("." * 7)
                print("|"+" " *5 + "|")
                print("|"+"o".center(5," ") + "|")
                print("|"+" " *5 + "|")
                print("'" * 7)
            if num == 2:
                print("Dice".center(7, " "))
                print("." * 7)
                print("|"+" " *5 + "|")
                print("| o o |")
                print("|"+" " *5 + "|")
                print("'" * 7)
            if num == 3:
                print("Dice".center(7, " "))
                print("." * 7)
                print("|"+"o".center(5," ") + "|")
                print("|"+"o".center(5," ") + "|")
                print("|"+"o".center(5," ") + "|")
                print("'" * 7)
            if num == 4:
                print("Dice".center(7, " "))
                print("." * 7)
                print("| o o |")
                print("|"+" " *5 + "|")
                print("| o o |")
                print("'" * 7)
            if num == 5:
                print("Dice".center(7, " "))
                print("." * 7)
                print("| o o |")
                print("|"+"o".center(5," ") + "|")
                print("| o o |")
                print("'" * 7)
            if num == 6:
                print("Dice".center(7, " "))
                print("." * 7)
                print("| o o |")
                print("| o o |")
                print("| o o |")
                print("'" * 7)
        inp=input("Enter 'y' to role the dice or 'n' to exit : ")
    else:
        print("Stimulation ended".center(45, "-"))


if __name__=="__main__":
    game=input("Hello! Enter 'y' for Dice Stimulator : " )
    dice(game)