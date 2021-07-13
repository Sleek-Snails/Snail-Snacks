# import rich

from Puzzle import Puzzle


class Cell:
    """A Cell in the maze"""

    def __init__(self):
        self.rightWall = False
        self.bottomWall = True


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
        for x in self._emptyMaze(width=width, height=height):
            print(x)


MazePuzzle().generateMaze()
