from random import randint

from .MultipleChoicePuzzle import MultipleChoicePuzzle


class MathPuzzle(MultipleChoicePuzzle):
    """Math Puzzles"""

    puzzles = [
        ["/", ''],["*",''],["+",'']
    ]

    def __init__(self, operator: str, placeholder: str):
        self.operator = operator
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        num3 = randint(1, 10)
        num4 = randint(0, 1)

        if self.operator == "/":
            ans = num1 / num2
            wro = num1 / num3
        elif self.operator == "*":
            ans = num1 * num2
            wro = num1 * num3
        elif self.operator == "-":
            ans = num1 - num2
            wro = num1 - num3
        else:
            ans = num1 + num2
            wro = num1 + num3

        if num4 == 0:
            opt = [ans, wro]
        elif num4 == 1:
            opt = [wro, ans]

        self.question = f"What is {num1} {self.operator} {num2}?"
        self.options = opt
        self.answer = num4
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.passed = False
        super(MultipleChoicePuzzle, self).__init__()


if __name__ == "__main__":
    MathPuzzle("/").startPuzzle()
    MathPuzzle("*").startPuzzle()
    MathPuzzle("-").startPuzzle()
