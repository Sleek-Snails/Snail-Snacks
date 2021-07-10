#library imports
import inspect
import os
import random
import sys

import requests
from rich import prompt

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from puzzles.Puzzle import Puzzle  # noqa: E402
from rich import print  # noqa: E402
from rich.console import RenderGroup  # noqa: E402
from rich.panel import Panel  # noqa: E402
from utils.KeyHandler import KeyHandler  # noqa: E402

## example: https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=multiple



def GetTriviaQuestion(amount=1, category=None, difficulty=None, type="multiple"):
    string = 'https://opentdb.com/api.php?'
    if amount!=None:
        string+="%s=%s%%"%("amount", amount)
    if category!=None:
        string+="%s=%s%%"%("category", category)
    if difficulty!=None:
        string+="%s=%s%%"%("difficulty", difficulty)
    if type!=None:
        string+="%s=%s%%"%("type", type)
    string = string.rstrip("%%")
    req = requests.get(string)
    req = req.json()
    global question
    question = req['results'][0]['question']
    global options
    options = []
    options.append(req['results'][0]['correct_answer'])
    for x in req['results'][0]['incorrect_answers']:
        options.append(x)
    random.shuffle(options)
    global answer
    answer = req['results'][0]['correct_answer']


GetTriviaQuestion()





class Triva(Puzzle):
    """Multiple Choice Question Class"""

    def __init__(self,
                 question: str, options: list, answer: int,
                 ) -> None:
        global answer
        global question
        global options
        self.question = question  # Question
        self.options = options  # List of possible options
        self.answer = answer  # Index of answer in options
        self.passed = None

    def startPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        panel_group = RenderGroup(
            Panel(f"{self.question}"),
            Panel(f"A - {self.options[0]}", style="on blue"),
            Panel(f"B - {self.options[1]}", style="on red"),
            Panel(f"C - {self.options[1]}", style="on green"),
            Panel(f"D - {self.options[1]}", style="on magenta")
        )
        print(panel_group)

        self.thisHere = KeyHandler(self._checkTrue)
        self.thisHere.enable()
        # print(f"question: {self.question}, options: {self.options}, answer: {self.answer}")

        # TODO: Show Timer
        if self.passed is (True or False):
            return self.passed  # Return true if user passed, return false if user failed

    def _checkTrue(self, key: str) -> bool:
        if self.answer == 0:
            if key == 'a':
                self.passed = True
                self.thisHere.disable()
                return False

            if key == 'b':
                self.passed = False
                self.thisHere.disable()
                return True

        if self.answer == 1:
            if key == 'a':
                self.passed = False
                self.thisHere.disable()
                return True

            if key == 'b':
                self.passed = True
                self.thisHere.disable()
                return False
