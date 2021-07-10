from random import randint

from puzzles.MultipleChoicePuzzle import MultipleChoicePuzzle

num1 = randint(1, 10)
num2 = randint(1, 10)
num3 = randint(1, 10)
num4 = randint(0, 1)
ans = num1 * num2
wro = num1 * num3

if num4 == 0:
    opt = [ans, wro]
elif num4 == 1:
    opt = [wro, ans]

MultipleChoicePuzzle(question=f"What is {num1} * {num2}", options=opt, answer=num4).startPuzzle()
