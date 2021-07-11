import random

from rich.prompt import Prompt

# from TextInputQuestion import TextInputQuestion

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

theQuestions = [
    {
        "GladOS": "Who runs the facility in portal",
        "Chell": "Who is the main character of Portal? (First Name Only)",
        "Cave Johnson": "Who was the CEO of Aperture Science? (Full name)"
    }
]


class GameQuizPuzzle:
    """Game Quiz Type Puzzles (might merge with Trivia Puzzle) - This is incomplete"""

    def __init__(self, choices: list, questions: dict):
        self.choices = choices
        self.questions = questions

    def startPuzzle(self) -> None:
        """Start Puzzle"""
        self.choices.shuffle()
        # for quesChoice in self.choices:
        #    # self.question = self.questions[quesChoice]
        #    # self.answer = quesChoice

        #    # ask = Prompt.ask(f"{}")
        #    # if ask == ans:
        #    #     wrong = False
        #    # if ask != ans:
        #    #     print("Incorrect!")
