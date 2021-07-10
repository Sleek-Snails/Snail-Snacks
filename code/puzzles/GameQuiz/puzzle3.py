import random

from rich.prompt import Prompt

choices = ["GladOS", "Chell", "Cave"]
choice = random.choice(choices)
ques = ""
ans = ""
if choice == "GladOS":
    ques = "Who runs the facility in portal?"
    ans = "GladOS"
if choice == "Chell":
    ques = "Who is the main character of Portal?(First Name Only)"
    ans = "Chell"
if choice == "Cave":
    ques = "Who was the CEO of Aperture Science?(Full name)"
    ans = "Cave Johnson"
wrong = True
while wrong is True:
    ask = Prompt.ask(f"{ques}")
    if ask == ans:
        wrong = False
    if ask != ans:
        print("Incorrect!")
