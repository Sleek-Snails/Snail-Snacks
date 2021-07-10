import inspect
import os
import sys

# Horrible Hack for local imports :|
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from puzzles.Puzzle import Puzzle  # noqa: E402
from rich import print  # noqa: E402
from rich.console import RenderGroup  # noqa: E402
from rich.panel import Panel  # noqa: E402
from utils.KeyHandler import KeyHandler  # noqa: E402


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
