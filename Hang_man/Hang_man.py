#random. choices()
import random
import csv

def hang_man(word):
    res="_____"
    #word=word[0]
    word = word[0].lower()
    print(word)
    #print(word)
    appr=['Great!', 'Awsome!', 'Good job!']
    warn=['Play carefully.', 'Death getting near.', 'Be causious']
    x=10
    for i in range(1, 11):
        guess=input("Guess a letter : ")
        if guess in word:
            n=word.index(guess)
            if guess in res:
                y=res.split(guess)
                wo=word.split(guess,1)
                p=wo[1].index(guess)
                y[1]=y[1][:p]+guess+y[1][p+1:]
                res=guess.join(y)
                word=guess.join(wo)
            else:
                result=res[:n]+guess+res[n+1:]
                res=result
            print(res)
            print((random.choices(appr))[0])
            print("We have more %d chances to guess %d letters." %((10-i), (res.count("_"))))
            print("_"*25)
            print("   _|".center(25, " "))
            print()
            print(("\ O /"+" "*x).center(25, " "))
            print(("|"+" "*x).center(25, " "))
            print((" / \ "+" "*x).center(25, " "))
            print("'"*25)

        else:
            print(res)
            x=10-i
            if x>=1:
                print("Think! Only %d chances left." %(10-i))
                print((random.choices(warn))[0])
                print("_"*25)
                print("   _|".center(25, " "))
                print()
                print((" O "+" "*x).center(25, " "))
                print((" /|\ "+" "*x).center(25, " "))
                print((" / \ "+" "*x).center(25, " "))
                print("'"*25)
            '''''
            else:
                print("_"*25)
                print(" O_|".center(25, " "))
                print("/|\  ".center(27, " "))
                print((" / \ ").center(25, " "))
                print()
                print("'"*25)
                print("Try again and save Jack this time.")
                print()
                print("Good Bye".center(30, "-"))
            '''''
        if res == word:
            print("Hurrah! You saved Jack.")
            break
    else:
        print("_"*25)
        print(" O_|".center(25, " "))
        print("/|\  ".center(27, " "))
        print((" / \ ").center(25, " "))
        print()
        print("'"*25)
        print("Try again and save Jack this time.")
        print()
        print("Do you want to try again?")
        print()
        again=input("If yes enter 'y' or enter any key to exit from the game : ")
        print()
        if again=='y':
            word=random.choices(list_of_words)
            hang_man(word)
        else:
            print("You tried your level best. But Jack's no more.")
            print("Good Bye".center(30, "-"))



if __name__=="__main__":
    with open('data.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        li = list(csv_reader)
        list_of_words=[]
        for i in li:
            list_of_words.extend(i)
    word=random.choices(list_of_words)
    print()
    print("Thank god you are here.\nOur Jack is in grave danger. He is going to be hanged in front of everyone.")
    print()
    print("Mayor announced 'if anyone wants to save jack they must guess a 5 letter word I give'.")
    print("So to save him you must guess the 5 letters of a word in 10 attempts.")
    print("Do you want to save Jack?")
    print()
    play=input("Enter 'y' if yes : ")
    if play == "y":
        hang_man(word)
