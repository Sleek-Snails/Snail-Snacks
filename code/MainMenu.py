from puzzles.Puzzle import Puzzle
from rich import box  # , print
# from rich.table import Table
from rich.columns import Columns
from rich.console import Console, render_group
# from rich.layout import Layout
# from rich.padding import Padding
from rich.panel import Panel
from utils.KeyHandler import BlockingKeyHandler as KeyHandler

# random
from random import randint

# import all of the game stuff
from puzzles import GameQuizPuzzle, MathPuzzle, MultipleChoicePuzzle, TriviaPuzzle


class MainMenu(Puzzle):
    """The Main Menu"""

    # 56x56 big box
    # holds 3x3 boxes
    # in 3x3 boxes there are 16x16 boxes

    def __init__(self):
        # rendergroups
        self.width = 120
        self.height = 57
        self.current_selection = [0,0] # the selection tool we can change
        # just print out the information again after changing the selection

        self.types = [GameQuizPuzzle.GameQuizPuzzle, MathPuzzle.MathPuzzle, MultipleChoicePuzzle.MultipleChoicePuzzle, TriviaPuzzle.TriviaPuzzle]
        self.ingame = False

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
        for y in range(3):
            columns = []
            for x in range(3):
                style = ""
                if y == self.current_selection[1] and x == self.current_selection[0]:
                    style = "on red"
                columns.append(Panel(self.get_inner_panels(), width=w, height=h, box=box.ROUNDED, style=style))
            yield Columns(columns, equal=True)

        # yield Columns([Panel(self.get_inner_panels(), width=w,
        #                height=h, box=box.ROUNDED) for x in range(3)], equal=True)
        # yield Columns([Panel(self.get_inner_panels(), width=w,
        #                height=h, box=box.ROUNDED) for x in range(3)], equal=True)
        # yield Columns([Panel(self.get_inner_panels(), width=w,
        #                height=h, box=box.ROUNDED) for x in range(3)], equal=True)

    def update(self, console: Console) -> None:
        """Prints new Panels (possibly replace this with a Live Display)"""
        console.print(Panel(self.get_panels(), box=box.ROUNDED, safe_box=False,
                            width=self.width, height=self.height), justify='center')
    
    def select_game(self):
        """Starts a random game"""
        index = randint(0,len(self.types)-1)
        question = self.types[index]
        
        # test
        puzzle_data = self.types[0].puzzles[randint(0,2)]
        q = self.types[0](puzzle_data[0], puzzle_data[1])
        q.startPuzzle()

    def moveSelection(self, key: str) -> None:
        """Move selection with up/down/left/right arrow keys"""
        if self.ingame:
            return
        x = 0
        y = 0

        if key == "KEY_UP":
            y -= 1
        if key == "KEY_DOWN":
            y += 1
        if key == "KEY_LEFT":
            x -= 1
        if key == "KEY_RIGHT":
            x += 1
        if key == "KEY_ENTER":
            self.select_game()
            self.ingame = True

        self.current_selection[0] += x
        self.current_selection[1] += y

        if self.current_selection[0] < 0:
            self.current_selection[0] = 2
        elif self.current_selection[0] > 2:
            self.current_selection[0] = 0

        if self.current_selection[1] < 0:
            self.current_selection[1] = 2
        if self.current_selection[1] > 2:
            self.current_selection[1] = 0

        print('(q) exit')
        self.update(console)


# test
console = Console()
main = MainMenu()
main.update(console)

kh = KeyHandler(main.moveSelection)
kh.start()

# input()
