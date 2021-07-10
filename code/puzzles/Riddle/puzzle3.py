from rich.prompt import Prompt
wrong = True
while wrong == True:
    riddle = Prompt.ask("I'm tall when I'm young, and I'm short when im old. What am I?")
    if riddle == "candle":
        wrong = False
    if not riddle == "candle":
        print("Incorrect!")