# import rich

from Puzzle import Puzzle


class MazePuzzle(Puzzle):
    """Maze puzzle arrows keys"""

    def __init__(self, size: int = 10, difficulty: int = 2):
        self.size = size
        self.difficulty = difficulty

    def _emptyMaze(width: int, height: int) -> list:
        """Generates list of lists width by height"""
        return [[]]

    def generateMaze(self, width: int = 54, height: int = 108) -> list:
        """Generate Maze list of lists"""
        return
