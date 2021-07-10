import inspect
import os
import sys

# Horrible Hack for local imports :|
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from random import randint  # noqa: E402

from MultipleChoicePuzzle import MultipleChoicePuzzle  # noqa: E402

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
