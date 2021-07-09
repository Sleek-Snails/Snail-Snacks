import rich  # noqa: F401


class MultipleChoicePuzzle:
    """Multiple Choice Question Class"""

    def __init__(self,
                 question: str = 'What is 1*2', options: list = [2, 4], answer: int = 0,
                 timer: bool = True, timerLength: int = 5
                 ) -> None:

        self.question = question  # Question
        self.options = options  # List of possible options
        self.answer = answer  # Index of answer in options
        self.timer = timer  # Enable timer true/false
        self.timerLength = timerLength  # Length of timer in seconds

    def showPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        print(f"question: {self.question}, options: {self.options}, answer: {self.answer}")

        # TODO: Write display logic
        # * Show Question
        # * Show timer (using rich progress bar)

        return True  # Return true if user passed, return false if user failed
