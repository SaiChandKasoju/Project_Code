import random
import csv


def csvToList():
    with open('data.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        li = list(csv_reader)
        list_of_words=[]
        for i in li:
            list_of_words.extend(i)
        word=random.choices(list_of_words)
        return word[0]

def correctGuess():
    

def startGame(word):
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
    




if __name__=="__main__":
    word=csvToList()
    play=input("Please enter 'y' to start : ")
    if play=='y':


