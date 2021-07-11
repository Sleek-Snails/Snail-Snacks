from rich import box, print
from rich.console import render_group
from rich.layout import Layout
# from rich.padding import Padding
from rich.panel import Panel
# from rich.table import Table
from rich.columns import Columns

class MainMenu:
    """The Main Menu"""

    # 56x56 big box
    # holds 3x3 boxes
    # in 3x3 boxes there are 16x16 boxes

    def __init__(self):
        # rendergroups
        pass

    @render_group()
    def get_panels() -> Panel: # dont add self please, error appears
        """Generator for Panel"""
        # using Layout again
        # yield Layout()
        yield Columns([Panel("", width=35,height=18) for x in range(3)], equal=True)
        yield Columns([Panel("", width=35,height=18) for x in range(3)], equal=True)
        yield Columns([Panel("", width=35,height=18) for x in range(3)], equal=True)


    def update(self) -> None:
        """Prints new Panels (possibly replace this with a Live Display"""
        print(Panel(MainMenu.get_panels(), box=box.ROUNDED, safe_box=False, width=112, height=56))


# test
main = MainMenu()
main.update()

input()
