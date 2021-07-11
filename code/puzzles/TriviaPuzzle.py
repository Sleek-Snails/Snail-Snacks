import random

import requests
from MultipleChoicePuzzle import MultipleChoicePuzzle


def GetTriviaQuestion(amount: int = 1, category: str = None, difficulty: str = None,
                      reqType: str = "multiple") -> tuple:
    """example: https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=multiple"""
    string = 'https://opentdb.com/api.php?'
    if amount is not None:
        string += f"&amount={amount}"
    if category is not None:
        string += f"&category={category}"
    if difficulty is not None:
        string += f"&difficulty={difficulty}"
    if reqType is not None:
        # string+="%s=%s%%"%("type", type)
        string += f"&type={reqType}"
    string = string.rstrip("%%")

    req = requests.get(string)
    req = req.json()

    options = []
    options.append(req['results'][0]['correct_answer'])
    for x in req['results'][0]['incorrect_answers']:
        options.append(x)
    random.shuffle(options)

    return (req['results'][0]['question'], options, options.index(req['results'][0]['correct_answer']))


requestRes = GetTriviaQuestion()
MultipleChoicePuzzle(question=requestRes[0], options=requestRes[1], answer=requestRes[2]).startPuzzle()


# class Triva(Puzzle):
#     """Multiple Choice Question Class"""

#     def __init__(self,
#                  question: str, options: list, answer: int,
#                  ) -> None:
#         global answer
#         global question
#         global options
#         self.question = question  # Question
#         self.options = options  # List of possible options
#         self.answer = answer  # Index of answer in options
#         self.passed = None

#     def startPuzzle(self) -> bool:
#         """Displays and runs puzzle"""
#         panel_group = RenderGroup(
#             Panel(f"{self.question}"),
#             Panel(f"A - {self.options[0]}", style="on blue"),
#             Panel(f"B - {self.options[1]}", style="on red"),
#             Panel(f"C - {self.options[1]}", style="on green"),
#             Panel(f"D - {self.options[1]}", style="on magenta")
#         )
#         print(panel_group)

#         self.thisHere = KeyHandler(self._checkTrue)
#         self.thisHere.enable()
#         # print(f"question: {self.question}, options: {self.options}, answer: {self.answer}")

#         # TODO: Show Timer
#         if self.passed is (True or False):
#             return self.passed  # Return true if user passed, return false if user failed

#     def _checkTrue(self, key: str) -> bool:
#         if self.answer == 0:
#             if key == 'a':
#                 self.passed = True
#                 self.thisHere.disable()
#                 return False

#             if key == 'b':
#                 self.passed = False
#                 self.thisHere.disable()
#                 return True

#         if self.answer == 1:
#             if key == 'a':
#                 self.passed = False
#                 self.thisHere.disable()
#                 return True

#             if key == 'b':
#                 self.passed = True
#                 self.thisHere.disable()
#                 return False
# ```
