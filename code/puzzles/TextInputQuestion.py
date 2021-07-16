# from rich.console import RenderGroup  # noqa: E402
# from rich.panel import Panel  # noqa: E402
import threading
from time import sleep

from puzzles.Puzzle import Puzzle  # noqa: E402
from rich import print  # noqa: E402
from rich import box
from rich.align import Align
from rich.layout import Layout
from rich.live import Live  # noqa: F401
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TimeRemainingColumn
from rich.prompt import Prompt  # noqa: F401
from rich.text import Text
from utils.KeyHandler import BlockingKeyHandler as KeyHandler


class TextInputQuestion(Puzzle):
    """Multiple Choice Question Class"""

    def __init__(self, question: str = 'What is 1*2', answer: str = "2", timer: int = None) -> None:
        self.question = question  # Question
        self.answer = answer  # Index of answer in options
        self.current_text = ""
        self.timer = timer
        self.passed = False
        # sleep(4)
        # self.lay = Layout(name="layRoot")

    def startPuzzle(self) -> bool:
        """Displays and runs puzzle"""
        Puzzle.displayCase.start()

        self.job_progress = Progress(
            # "{task.description}",
            # SpinnerColumn(),
            BarColumn(),
            TimeRemainingColumn()
            # f"{Progress.Task.total-Progress.Task.completed}s Remaining"
            # TextColumn("[progress.percentage]{(task.percentage/100)*5}"),
            # TimeRemainingColumn(),
            # BarColumn()
            # BarColumn()
        )
        self.job1 = self.job_progress.add_task("[green]Cooking", total=100)

        Puzzle.rootLayout["root"].split_column(
            Layout(Panel(Align(self.job_progress, align="center")), name="timer"),
            Layout(Panel(Text(f"{self.question}")), name="question"),
            Layout(Panel(Text("Answer: _")), name="input"),
            Layout(Panel(Text("(q) quit")), name="exit")
        )
        # Puzzle.rootLayout["root"]["question"].update()
        Puzzle.rootLayout["root"]["timer"].size = 3
        Puzzle.rootLayout["root"]["input"].size = 3
        Puzzle.rootLayout["root"]["exit"].size = 3
        Puzzle.displayCase.update(Panel(Puzzle.rootLayout, box=box.ROUNDED, width=60, height=30), refresh=True)
        self.current_text = "Answer: "

        if self.timer is not None:
            x = threading.Thread(target=self._updateProgress, args=(self.timer, ))
            x.start()

        self.kh = KeyHandler(self._callback)
        ask = self.kh.start()

        print(ask.strip().lower())

        if str(ask).strip().lower() == f"Answer: {str(self.answer).lower()}".strip().lower():
            Puzzle.displayCase.stop()
            self.passed = True
            return True
        else:
            # print("Incorrect!")
            # print(ask)
            Puzzle.rootLayout["root"]["question"].update(Panel(Text("Incorrect.")))
            Puzzle.displayCase.update(Panel(Puzzle.rootLayout, box=box.ROUNDED, width=60, height=30), refresh=True)
            # sleep(1)
            Puzzle.displayCase.stop()
            self.passed = False
            return False

    def _callback(self, key: str) -> str:
        if "KEY" in key:
            if key == "KEY_ENTER":
                self.kh.stop()
                return self.current_text
            elif key == "KEY_BACKSPACE" or key == "KEY_DELETE":
                if self.current_text != "Answer: ":
                    self.current_text = self.current_text[:-1]
                Puzzle.rootLayout["root"]["input"].update(Panel(Text(f"{self.current_text}_")))
                Puzzle.displayCase.update(Panel(Puzzle.rootLayout, box=box.ROUNDED, width=60, height=30), refresh=True)
        else:
            self.current_text += key
            Puzzle.rootLayout["root"]["input"].update(Panel(Text(f"{self.current_text}_")))
            Puzzle.displayCase.update(Panel(Puzzle.rootLayout, box=box.ROUNDED, width=60, height=30), refresh=True)
            return False

    def _updateProgress(self, time: int) -> bool:
        for x in range(100):
            sleep(time/100)
            for job in self.job_progress.tasks:
                if not job.finished:
                    self.job_progress.advance(job.id)
            Puzzle.displayCase.update(Panel(Puzzle.rootLayout, box=box.ROUNDED, width=60, height=30), refresh=True)
        if self.passed is not True:
            self.kh.stop()
            Puzzle.displayCase.stop()
            return False


if __name__ == "__main__":
    TextInputQuestion(question="I am both dead and alive; what is my name?",
                      answer="Schrodinger's cat",
                      timer=5).startPuzzle()

    TextInputQuestion(question="I share a name with a brand, I made an electifing invention. Who am I?",
                      answer="Nicola Tesla",
                      timer=10).startPuzzle()

    TextInputQuestion(question="I'm tall when I'm young, and I'm short when im old. What am I?",
                      answer="candle",
                      timer=15).startPuzzle()
