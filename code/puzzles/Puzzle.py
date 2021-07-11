import time

# from rich.layout import Layout
from rich.live import Live
from rich.progress import track
from rich.text import Text


class Puzzle:
    """Utility Functions Useful for all puzzle classes."""

    displayCase = Live(Text("Hello World"), auto_refresh=False)

    def __init__(self, timer: bool = True, timerLength: int = 5):
        self.timer = timer  # Enable timer true/false
        self.timerLength = timerLength  # Length of timer in seconds

        # self.displayCase =
        # with self.displayCase as live:
        # with self.displayCase:
        #     self.displayCase = live
        #     print(self.displayCase)

    def startTimer(self) -> bool:
        """Shows rich progress bar for timerLength seconds."""
        if self.timer:
            for n in track(range(self.timerLength), description="Timer"):
                time.sleep(1)
            return True
        else:
            return False
