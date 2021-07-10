from rich.prompt import Prompt

wrong = True
while wrong is True:
    riddle = Prompt.ask("I am both dead and alive; what is my name?")
    if riddle == "Schrodinger's cat":
        wrong = False
    if not riddle == "Schrodinger's cat":
        print("Incorrect!")
