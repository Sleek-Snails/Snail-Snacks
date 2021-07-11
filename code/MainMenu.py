from rich import box, print
from rich.console import render_group
# from rich.layout import Layout
# from rich.padding import Padding
from rich.panel import Panel


class MainMenu:
    """The Main Menu"""

    # 56x56 big box
    # holds 3x3 boxes
    # in 3x3 boxes there are 16x16 boxes

    def __init__(self):
        # rendergroups
        pass

    @render_group()
    def get_panels(self) -> Panel:
        """Generator for Panel"""
        yield Panel('left', width=20, height=10)

    def update(self) -> None:
        """Prints new Panels (possibly replace this with a Live Display"""
        print(Panel(MainMenu.get_panels(), box=box.ROUNDED, safe_box=False, width=112, height=56))


# test
main = MainMenu()
main.update()

input()
