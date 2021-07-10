import random
import re

from random_word import RandomWords

r = RandomWords()
word = r.get_random_word()
listword = list(word)

displayedword = "-"*len(listword)
displayedlist = re.findall("-", displayedword)
print(displayedword)
ultguess = False
fails = []
guesses = []
totalhints = 3


def hint() -> None:
    """Description of function"""
    global totalhints
    x = random.randint(1, len(listword))
    if displayedlist[x] == "-":
        print("this worked")
        displayedlist[x] = listword[x]
        for y in range(len(listword)):
            if displayedlist[x] == listword[y]:
                displayedlist[y] = listword[y]
    totalhints -= 1


def guessresult(guess: str) -> str:
    """Guess the result. I don't know :cry:"""
    global totalhints
    global ultguess
    global word
    global guesses
    if guess == "hint" and totalhints != 0:
        hint()
        print("You have used a hint! you have %s left" % totalhints)

    if len(guess) == 1:
        if guess not in guesses:

            for x in range(len(listword)):
                if listword[x] == guess:
                    displayedlist[x] = guess
            if len(re.findall(guess, word)) == 0:
                fails.append(guess)
        guesses.append(guess)

    if len(guess) == len(word):
        if guess == word:
            ultguess = True
        else:
            fails.append(guess)
            guesses.append(guess)


def hangman() -> None:
    """He got hanged"""
    global ultguess
    global word
    while len(fails) < 7:
        guessresult(guess=input("guess something \n"))
        if ultguess is True:
            print("win")
            break
        print("fails:"+"".join(fails))
        print("guesses:"+"".join(guesses))
        print("".join(displayedlist))
    else:
        print("lose")
        print("The word was %s!" % (word))
    return


hangman()
