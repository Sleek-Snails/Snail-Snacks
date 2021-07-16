import random

import requests
from .MultipleChoicePuzzle import MultipleChoicePuzzle


class TriviaPuzzle(MultipleChoicePuzzle):
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
        self.question = self.sanitize_html(requestRes[0])

        sanitized_options = []
        for each in requestRes[1]:
            sanitized_options.append(self.sanitize_html(each))
        self.options = sanitized_options

        self.answer = requestRes[2]
        super(TriviaPuzzle, self).startPuzzle()

    def sanitize_html(self, sentence: str) -> str:
        """Replace all HMTL syntax with normal punctuation marks.

        Replace &quot; with escaped double quotes.
        Replace &#039; with escaped single quote.
        """
        out = sentence.replace("&quot;", "\"")
        return out.replace("&#039;", "'")


if __name__ == "__main__":
    TriviaPuzzle().startPuzzle()
