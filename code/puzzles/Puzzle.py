import time

from rich.layout import Layout
from rich.progress import track


class Puzzle:
    """Utility Functions Useful for all puzzle classes."""

    def __init__(self, timer: bool = True, timerLength: int = 5):
        self.timer = timer  # Enable timer true/false
        self.timerLength = timerLength  # Length of timer in seconds

        self.displayCase = Layout()

    def showTimer(self) -> bool:
        """Shows rich progress bar for timerLength seconds."""
        if self.timer:
            for n in track(range(self.timerLength), description="Timer"):
                time.sleep(1)
            return True
        else:
            return False
