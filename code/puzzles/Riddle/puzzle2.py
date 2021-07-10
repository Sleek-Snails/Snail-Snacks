from rich.prompt import Prompt
wrong = True
while wrong == True:
    riddle = Prompt.ask("I share a name with a brand, I made an electifing invention. Who am I?")
    if riddle == "Nicola Tesla":
        wrong = False
    if not riddle == "Nicola Tesla":
        print("Incorrect!")