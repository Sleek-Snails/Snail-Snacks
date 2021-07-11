import inspect
import os
import sys

# Horrible Hack for local imports :|
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from puzzles.Puzzle import Puzzle  # noqa: E402
from rich.console import render_group  # noqa: E402
from rich.panel import Panel  # noqa: E402
from utils.KeyHandler import KeyHandler  # noqa: E402


class MultipleChoicePuzzle(Puzzle):
    """Multiple Choice Question Class"""

    def __init__(self,
                 question: str = 'What is 1*2', options: list = [2, 4], answer: int = 0,
                 timer: bool = False, timerLength: int = 5
                 ) -> None:
        self.question = question  # Question
        self.options = options  # List of possible options
        self.answer = answer  # Index of answer in options
        self.passed = None
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        super(MultipleChoicePuzzle, self).__init__(timer=timer, timerLength=timerLength)

    @render_group()
    def get_panels(self) -> Panel:
        """Generator for panels"""
        yield Panel(f"{self.question}")
        yield from [Panel(f"{alph} - {self.options[self.alphabet.find(alph)]}")
                    for alph in self.alphabet[:len(self.options)]]

    def startPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        with Puzzle.displayCase as dc:
            dc.update(self.get_panels(), refresh=True)

        self.keypressHandler = KeyHandler(self._checkTrue)
        self.keypressHandler.enable()
        # print(f"question: {self.question}, options: {self.options}, answer: {self.answer}")

        # TODO: Show Timer
        if self.passed is (True or False):
            return self.passed  # Return true if user passed, return false if user failed

    def _checkTrue(self, key: str) -> bool:
        if key.upper() in self.alphabet[:len(self.options)]:
            if key.upper() == self.alphabet[self.answer]:
                self.passed = True
                self.keypressHandler.disable()
                # print('right')
                return False
            else:
                self.passed = False
                self.keypressHandler.disable()
                # print('wrong')
                return True
