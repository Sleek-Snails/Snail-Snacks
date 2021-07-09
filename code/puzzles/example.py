import rich  # noqa: F401


class MultipleChoicePuzzle:
    """Multiple Choice Question Class"""

    def __init__(self, question: str = 'What is 1*2', options: list = [2, 4], answer: int = 0) -> None:
        self.question = question  # Question
        self.options = options  # list of possible options
        self.answer = answer  # index of answer in options

    def showPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        print(f"question: {self.question}, options: {self.options}, answer: {self.answer}")

        return True  # Return true if user passed, return false if user failed
