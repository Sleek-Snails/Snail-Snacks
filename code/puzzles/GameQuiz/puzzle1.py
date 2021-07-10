import random

from rich.prompt import Prompt

choices = ["doom", "half-life", "portal"]
choice = random.choice(choices)
ques = ""
ans = ""
wrong = True
if choice == "doom":
    ques = "What game sparked the First Person Shooter endustry?"
    ans = "DOOM"
if choice == "half-life":
    ques = "What game was the most popular story game of the 1990s?"
    ans = "Half-Life"
if choice == "portal":
    ques = "Which game used portals to proceed to different levels?"
    ans = "Portal"
while wrong is True:
    ask = Prompt.ask(f"{ques}")
    if ask == ans:
        wrong = False
    if ask != ans:
        print("Incorrect!")
