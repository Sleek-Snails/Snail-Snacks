import random

from .TextInputQuestion import TextInputQuestion


class GameQuizPuzzle(TextInputQuestion):
    """Game Quiz Type Puzzles - Subclass of TextInputQuestion"""

    """ questions"""
    puzzles = [
            [["doom", "half-life", "portal"], {        "doom": "What game sparked the First Person Shooter endustry?",
        "half-life": "What game was the most popular story game of the 1990s?",
        "portal": "Which game used portals to proceed to different levels?"}],

            [["Barney", "Gordon", "Eli"], {
            "Barney": "Who is the security gaurd who follows you throughout Half-Life?(First Name Only)",
            "Gordon": "Who is the main character of Half-Life?(First Name Only)",
            "Eli": "Who is Alyx's father?(First Name Only)"}],

            [["GladOS", "Chell", "Cave Johnson"], {"GladOS": "Who runs the facility in portal",
            "Chell": "Who is the main character of Portal? (First Name Only)",
            "Cave Johnson": "Who was the CEO of Aperture Science? (Full name)"}],

            [["Pikachu", "Pallet Town", "Kanto"],
            {"Pikachu": "Who is Ash Kethcum's iconic partner in Pokemon?",
            "Pallet Town": "Where did Ash Ketchum start his grand journey to become the Pokemon master?",
            "Kanto": "What region did Ash Ketchum start in?"}],

            [['1', '100', '3628800'],
            {
                '1': "What is 2 - 1?",
                '100': "What is 10^2?",
                '3628800': "What is 10!"
            }],

            [['mitochondria', 'chlorophyll', 'ATP'],
            {
                'mitochondria' : "What is the powerhouse of a cell?",
                "chlorophyll" : "What makes a plants leaves green?",
                "ATP" : "What molecule in our body stores energy for us to use? (Abreviated form please)"
            }]
    ]

    def __init__(self, choices: list, questions: dict):
        self.choices = choices
        self.questions = questions
        self.timer = 10
        self.passed = False

    def startPuzzle(self) -> None:
        """Start Puzzle"""
        random.shuffle(self.choices)
        for quesChoice in self.choices:
            self.question = self.questions[quesChoice]
            self.answer = quesChoice
            if super(GameQuizPuzzle, self).startPuzzle() is False:
                return False
        return True


if __name__ == "__main__":
    print("puzzle1")
    GameQuizPuzzle(choices=["doom", "half-life", "portal"], questions={
        "doom": "What game sparked the First Person Shooter endustry?",
        "half-life": "What game was the most popular story game of the 1990s?",
        "portal": "Which game used portals to proceed to different levels?"
    }).startPuzzle()

    print("puzzle2")
    GameQuizPuzzle(choices=["Barney", "Gordon", "Eli"], questions={
        "Barney": "Who is the security gaurd who follows you throughout Half-Life?(First Name Only)",
        "Gordon": "Who is the main character of Half-Life?(First Name Only)",
        "Eli": "Who is Alyx's father?(First Name Only)"
    }).startPuzzle()

    print("puzzle3")
    GameQuizPuzzle(choices=["GladOS", "Chell", "Cave Johnson"], questions={
        "GladOS": "Who runs the facility in portal",
        "Chell": "Who is the main character of Portal? (First Name Only)",
        "Cave Johnson": "Who was the CEO of Aperture Science? (Full name)"
    }).startPuzzle()
