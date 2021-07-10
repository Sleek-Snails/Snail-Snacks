import random

from rich.prompt import Prompt

words = ["pizza", "chicken", "cake"]
word = random.choice(words)
hint = ""
if word == "pizza":
    hint = "What is the most popular food among children in the US?"
if word == "chicken":
    hint = "What is the food that's white and stringy when cooked?"
if word == "cake":
    hint = "What is the most popular food for a birthday party?"
wrong = True
while wrong is True:
    ques = Prompt.ask(f"{hint}")
    if ques == word:
        wrong = False
    if not ques == word:
        print("Incorrect!")
