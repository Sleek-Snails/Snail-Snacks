from puzzles.Puzzle import Puzzle  # noqa: E402
from rich import print  # noqa: E402
from rich.layout import Layout
from rich.live import Live  # noqa: F401
from rich.panel import Panel
from rich.prompt import Prompt  # noqa: F401
from rich.text import Text
from utils.KeyHandler import BlockingKeyHandler as KeyHandler

# from rich.console import RenderGroup  # noqa: E402
# from rich.panel import Panel  # noqa: E402


class TextInputQuestion(Puzzle):
    """Multiple Choice Question Class"""

    def __init__(self, question: str = 'What is 1*2', answer: str = "2") -> None:
        self.question = question  # Question
        self.answer = answer  # Index of answer in options
        self.current_text = ""
        # self.lay = Layout(name="layRoot")

    def startPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        Puzzle.displayCase.start()
        Puzzle.rootLayout["root"].split_column(
            Layout(name="question"),
            Layout(Panel(Text("Answer: ")), name="input")
        )
        Puzzle.rootLayout["root"]["question"].update(Panel(Text(f"{self.question}")))
        Puzzle.rootLayout["root"]["question"].size = 3
        Puzzle.rootLayout["root"]["input"].size = 3
        Puzzle.displayCase.update(Puzzle.rootLayout, refresh=True)
        self.current_text = "Answer: "

        self.kh = KeyHandler(self._callback)
        ask = self.kh.start()
        print(ask)
        print(self.answer)
        # ask = str(Prompt.ask(f"{self.question}")).lower()
        # ask = input(f"{self.question}")
        if ask.lower() == "Answer: " + str(self.answer).lower():
            Puzzle.displayCase.stop()
            return True
        else:
            print("Incorrect!")
            print(ask)
            Puzzle.displayCase.stop()
            return False

    def _callback(self, key: str) -> str:
        if "KEY" in key:
            if key == "KEY_ENTER":
                self.kh.stop()
                return self.current_text
            elif key == "KEY_BACKSPACE" or key == "KEY_DELETE":
                # self.kh.stop()
                # return self.current_text
                if self.current_text != "Answer: ":
                    self.current_text = self.current_text[:-1]
                Puzzle.rootLayout["root"]["input"].update(Panel(Text(f"{self.current_text}")))
                Puzzle.displayCase.update(Puzzle.rootLayout, refresh=True)
        else:
            self.current_text += key

            # with Puzzle.displayCase:
            Puzzle.rootLayout["root"]["input"].update(Panel(Text(f"{self.current_text}")))
            Puzzle.displayCase.update(Puzzle.rootLayout, refresh=True)

        # self.lay['layRoot'].update(Text(f"{self.current_text}"))
        # self.live.update(self.lay, refresh=True)
        # with Puzzle.displayCase as pdc:
            # os.system('cls' if os.name == 'nt' else 'clear')  # noqa: S605
            # pdc.update(self.lay, refresh=True)


if __name__ == "__main__":
    TextInputQuestion(question="I am both dead and alive; what is my name?",
                      answer="Schrodinger's cat").startPuzzle()

    TextInputQuestion(question="I share a name with a brand, I made an electifing invention. Who am I?",
                      answer="Nicola Tesla").startPuzzle()

    TextInputQuestion(question="I'm tall when I'm young, and I'm short when im old. What am I?",
                      answer="candle").startPuzzle()
