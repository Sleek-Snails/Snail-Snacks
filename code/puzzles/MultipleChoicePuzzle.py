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

    def startPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        panel_group = RenderGroup(
            Panel(f"{self.question}"),
            Panel(f"A - {self.options[0]}", style="on blue"),
            Panel(f"B - {self.options[1]}", style="on red")
        )
        print(panel_group)

        thisHere = KeyHandler(self._checkTrue)
        thisHere.enable()
        # print(f"question: {self.question}, options: {self.options}, answer: {self.answer}")

        return True  # Return true if user passed, return false if user failed

    def _checkTrue(self, key: str) -> bool:
        if self.answer == 0:
            print("test")
            if key == 'a':
                print('h')
                return False

            if key == 'b':
                print("Wrong!")
                return True

        if self.answer == 1:
            if key == 'a':
                print('j')
                print("Wrong!")
                return True

            if key == 'b':
                return False
