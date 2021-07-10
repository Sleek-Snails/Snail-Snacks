# Local Imports
from puzzles.Puzzle import Puzzle
# Library Imports
from rich import print
from rich.console import RenderGroup
from rich.panel import Panel
from utils.KeyHandler import KeyHandler


class MultipleChoicePuzzle(Puzzle):
    """Multiple Choice Question Class"""

    def __init__(self,
                 question: str = 'What is 1*2', options: list = [2, 4], answer: int = 0,
                 ) -> None:

        self.question = question  # Question
        self.options = options  # List of possible options
        self.answer = answer  # Index of answer in options
        self.passed = None

    def startPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        panel_group = RenderGroup(
            Panel(f"{self.question}"),
            Panel(f"A - {self.options[0]}", style="on blue"),
            Panel(f"B - {self.options[1]}", style="on red")
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
                print("Wrong!")
                self.passed = False
                self.thisHere.disable()
                return True

        if self.answer == 1:
            if key == 'a':
                print("Wrong!")
                self.passed = False
                self.thisHere.disable()
                return True

            if key == 'b':
                self.passed = True
                self.thisHere.disable()
                return False
