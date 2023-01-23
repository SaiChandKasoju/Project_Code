import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def dic(inp):
    inp=inp.lower()
    if inp in data:
        print(inp.title())
        print(data[inp])
    elif inp.title() in data:
        print(inp.title())
        print(data[inp.title()])
    elif inp.upper() in data:
        print(inp.title())
        print(data[inp.upper()])
    elif len(get_close_matches(inp , data.keys())) > 0 :
        print("did you mean %s" %get_close_matches(inp, data.keys())[0])
        decide = input("Enter 'y' if yes or 'n' if not : ")
        if decide == "y":
            return print(data[get_close_matches(inp , data.keys())[0]])
        elif decide == "n":
            return print("Please check your input and try again.")
        else:
            return print("You have entered wrong input please enter just y or n")
    else:
        print("Please check your input and try again.")

if __name__=="__main__":
    inp=input("Enter the word : ")
    dic(inp)