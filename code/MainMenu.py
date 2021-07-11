from rich import print
from rich.panel import Panel
from rich.padding import Padding
from rich.layout import Layout

from rich.console import render_group

from rich import box

class MainMenu:
    """The Main Menu"""

    # 56x56 big box
    # holds 3x3 boxes
    # in 3x3 boxes there are 16x16 boxes

    def __init__(self):
        # rendergroups
        pass

    @render_group()
    def get_panels():
        yield Panel('left', width=20, height=10)

    def update(self):
        print(Panel(MainMenu.get_panels(), box=box.ROUNDED, safe_box=False, width=112, height=56))

# test
main = MainMenu()
main.update()

input()