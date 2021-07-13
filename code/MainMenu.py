from rich import box  # , print
# from rich.table import Table
from rich.columns import Columns
from rich.console import Console, render_group
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
        self.width = 120
        self.height = 57
        pass

    @render_group()
    def get_inner_panels(self) -> Columns:
        """Generator for the get_panels command"""
        w = (self.width // 3 - 3) // 3 - 2
        # h = (self.height //3 - 2) // 3 - 2
        yield Columns([Panel(Columns(equal=True), width=w, height=5) for x in range(3)], equal=True)
        yield Columns([Panel(Columns(equal=True), width=w, height=5) for x in range(3)], equal=True)
        yield Columns([Panel(Columns(equal=True), width=w, height=5) for x in range(3)], equal=True)

    @render_group()
    def get_panels(self) -> Columns:  # dont add self please, static func, idk what that means but it seems that way
        """Generator for Panel"""
        w = self.width // 3 - 3
        h = self.height // 3 - 1
        yield Columns([Panel(self.get_inner_panels(), width=w, height=h,
                             box=box.ROUNDED) for x in range(3)], equal=True)
        yield Columns([Panel(self.get_inner_panels(), width=w, height=h,
                             box=box.ROUNDED) for x in range(3)], equal=True)
        yield Columns([Panel(self.get_inner_panels(), width=w, height=h,
                             box=box.ROUNDED) for x in range(3)], equal=True)

    def update(self, console: Console) -> None:
        """Prints new Panels (possibly replace this with a Live Display"""
        console.print(Panel(self.get_panels(), box=box.ROUNDED, safe_box=False,
                            width=self.width, height=self.height), justify='center')


# test
console = Console()
main = MainMenu()
main.update(console)

input()
