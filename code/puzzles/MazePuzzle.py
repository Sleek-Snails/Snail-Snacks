# import rich

import random

from .Puzzle import Puzzle


class Cell:
    """A Cell in the maze"""

    def __init__(self):
        self.rightWall = True
        self.bottomWall = True

    def __repr__(self):
        out = ""
        if self.rightWall and self.bottomWall:
            out += "┌───┐\n"
            out += "│   │\n"
            out += "└───┘\n"
            return out
        elif self.rightWall:
            return " │"
        elif self.bottomWall:
            return "──"
        else:
            return "  "

        # return "#"
    def __str__(self):
        out = ""
        if self.rightWall and self.bottomWall:
            # return "─┘"
            out += "┌───┐\n"
            out += "│   │\n"
            out += "└───┘\n"
            return out
        elif self.rightWall:
            return " │"
        elif self.bottomWall:
            return "──"
        else:
            return "  "


class MazePuzzle(Puzzle):
    """Maze puzzle arrows keys"""

    def __init__(self, size: int = 10, difficulty: int = 2):
        self.size = size
        self.difficulty = difficulty

    def _emptyMaze(self, width: int, height: int) -> list:
        """Generates list of lists width by height"""
        return [[Cell() for x in range(width)] for y in range(height)]

    def generateMaze(self, width: int = 10, height: int = 10) -> list:
        """Generate Maze list of lists"""
        for y in self._emptyMaze(width=width, height=height):
            for x in y:
                x.rightWall = random.choice([True, False])
                x.bottomWall = random.choice([True, False])
                print(x, end="")
            print("")


MazePuzzle().generateMaze()
