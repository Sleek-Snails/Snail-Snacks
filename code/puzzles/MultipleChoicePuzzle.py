import os
import sys

parent_dir = os.path.dirname(os.getcwd())
sys.path.insert(0, parent_dir)

from .Puzzle import Puzzle  # noqa: E402
from rich.console import render_group  # noqa: E402
from rich.panel import Panel  # noqa: E402
from utils.KeyHandler import BlockingKeyHandler as KeyHandler  # noqa: E402


class MultipleChoicePuzzle(Puzzle):
    """Multiple Choice Question Class"""

    def __init__(self,
                 question: str = 'What is 1*2', options: list = [2, 4], answer: int = 0,
                 timer: bool = False, timerLength: int = 5
                 ) -> None:
        super(MultipleChoicePuzzle, self).__init__(timer=timer, timerLength=timerLength)
        self.question = question  # Question
        self.options = options  # List of possible options
        self.answer = answer  # Index of answer in options
        self.passed = None
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @render_group()
    def get_panels(self) -> Panel:
        """Generator for panels"""
        yield Panel(f"{self.question}")
        yield from [Panel(f"({alph}) {self.options[self.alphabet.find(alph)]}")
                    for alph in self.alphabet[:len(self.options)]]

    def startPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        with Puzzle.displayCase as dc:
            os.system('cls' if os.name == 'nt' else 'clear')  # noqa: S605
            dc.update(self.get_panels(), refresh=True)

        self.keypressHandler = KeyHandler(self._checkTrue)
        self.keypressHandler.start()
        # print(f"question: {self.question}, options: {self.options}, answer: {self.answer}")

        # TODO: Show Timer
        if self.passed is (True or False):
            return self.passed  # Return true if user passed, return false if user failed

    def _checkTrue(self, key: str) -> bool:
        if key.upper() in self.alphabet[:len(self.options)]:
            if key.upper() == self.alphabet[self.answer]:
                self.passed = True
                self.keypressHandler.stop()
                # print('right')
                print(key)
                return True
            else:
                self.passed = False
                self.keypressHandler.stop()
                print('wrong')
                print(key)
                return True


if __name__ == "__main__":
    MultipleChoicePuzzle().startPuzzle()
