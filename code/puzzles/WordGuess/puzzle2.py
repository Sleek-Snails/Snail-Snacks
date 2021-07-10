import random

from rich.prompt import Prompt

word = "pycharm"
scram = list(word)
random.shuffle(scram)
newword = ""
for x in scram:
    newword += x
wrong = True
while wrong is True:
    ques = Prompt.ask(f"Unscramble {newword}")
    if ques == word:
        wrong = False
    if not ques == word:
        print("Incorrect!")
