from time import sleep

from rich import box
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import track


class Puzzle:
    """Utility Functions Useful for all puzzle classes."""

    rootLayout = Layout(name="root")
    displayCase = Live(Panel(rootLayout, box=box.ROUNDED, width=60, height=30), auto_refresh=False, screen=True)

    def __init__(self, timer: bool = True, timerLength: int = 5):
        self.timer = timer  # Enable timer true/false
        self.timerLength = timerLength  # Length of timer in seconds

    def startTimer(self) -> bool:
        """Shows rich progress bar for timerLength seconds."""
        if self.timer:
            for n in track(range(self.timerLength), description="Timer"):
                sleep(1)
            return True
        else:
            return False
