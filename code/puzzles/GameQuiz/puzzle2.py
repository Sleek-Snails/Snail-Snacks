import random

from rich.prompt import Prompt

choices = ["Barney", "Gordon", "Alyx"]
choice = random.choice(choices)
ques = ""
ans = ""
if choice == "Barney":
    ques = "Who is the security gaurd who follows you throughout Half-Life?(First Name Only)"
    ans = "Barney"
if choice == "Gordon":
    ques = "Who is the main character of Half-Life?(First Name Only)"
    ans = "Gordon"
if choice == "Alyx":
    ques = "Who is Alyx's father?(First Name Only)"
    ans = "Eli"
wrong = True
while wrong is True:
    ask = Prompt.ask(f"{ques}")
    if ask == ans:
        wrong = False
    if ask != ans:
        print("Incorrect!")
