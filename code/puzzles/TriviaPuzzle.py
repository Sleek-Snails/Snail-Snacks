import random

import requests
from MultipleChoicePuzzle import MultipleChoicePuzzle


class Trivia(MultipleChoicePuzzle):
    """Trivia Question Class"""

    def GetTriviaQuestion(self, amount: int = 1, category: str = None, difficulty: str = None,
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

    def startPuzzle(self) -> None:
        """Start trivia question puzzle."""
        requestRes = self.GetTriviaQuestion()
        self.question = requestRes[0]
        self.options = requestRes[1]
        self.answer = requestRes[2]
        super(Trivia, self).startPuzzle()


if __name__ == "__main__":
    Trivia().startPuzzle()
