from typing import Final

from question_types import Question


MIN_LETTER: Final[str] = 'A'
MAX_LETTER: Final[str] = 'Z'
ALL_LETTERS: Final[list[str]] = [
    chr(c) for c in range(ord(MIN_LETTER), ord(MAX_LETTER) + 1)
]

# Limit how far apart the pairs of letters can be in the alphabet
# This cuts down the number of questions to something reasonable
# It mainly gets rid of the really easy ones like 'AZ'
DIFFERENCE_LIMIT: Final[int] = 4


def generate_questions() -> list[Question]:
    questions: list[Question] = []
    for letter_a in ALL_LETTERS:
        for letter_b in ALL_LETTERS:
            if letter_a == letter_b:
                continue
            if abs(ord(letter_a) - ord(letter_b)) > DIFFERENCE_LIMIT:
                continue
            a_then_b = letter_a + letter_b
            b_then_a = letter_b + letter_a
            prompt = f'{a_then_b} or {b_then_a}'
            answer = a_then_b if letter_a < letter_b else b_then_a
            questions.append(Question(prompt=prompt, answer=answer))
    return questions


def check_response(question: Question, response: str) -> bool:
    response = response.strip()
    response = ''.join(response.split())
    response = response.upper()
    return response == question.answer
