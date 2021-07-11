from Puzzle import Puzzle  # noqa: E402
from rich import print  # noqa: E402
from rich.prompt import Prompt

# from rich.console import RenderGroup  # noqa: E402
# from rich.panel import Panel  # noqa: E402


class TextInputQuestion(Puzzle):
    """Multiple Choice Question Class"""

    def __init__(self, question: str = 'What is 1*2', answer: str = "2") -> None:
        self.question = question  # Question
        self.answer = answer  # Index of answer in options

    def startPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        ask = Prompt.ask(f"{self.question}")
        if ask == self.answer:
            return True
        else:
            print("Incorrect!")
            return False


if __name__ == "__main__":
    TextInputQuestion(question="I am both dead and alive; what is my name?",
                      answer="Schrodinger's cat").startPuzzle()

    TextInputQuestion(question="I share a name with a brand, I made an electifing invention. Who am I?",
                      answer="Nicola Tesla").startPuzzle()

    TextInputQuestion(question="I'm tall when I'm young, and I'm short when im old. What am I?",
                      answer="candle").startPuzzle()
