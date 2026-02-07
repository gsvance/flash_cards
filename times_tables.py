import random
from typing import Final

from question_types import Question


MIN_FACTOR: Final[int] = 1
MAX_FACTOR: Final[int] = 12
assert MIN_FACTOR <= MAX_FACTOR

TIMES: Final[str] = chr(0xd7)


def generate_questions() -> list[Question]:
    # Note: to keep the number of questions down, we only ever add a*b or b*a.
    # Never both. This means you might get 3*7 in one play and 7*3 in another,
    # but never both. Just one. This cut also means the squares (like 5*5) will
    # not be totally swamped out by all the other questions.
    questions: list[Question] = []
    for factor_a in range(MIN_FACTOR, MAX_FACTOR + 1):
        for factor_b in range(factor_a, MAX_FACTOR + 1):
            a_times_b = f'{factor_a} {TIMES} {factor_b}'
            b_times_a = f'{factor_b} {TIMES} {factor_a}'
            prompt = random.choice([a_times_b, b_times_a])
            answer = str(factor_a * factor_b)
            questions.append(Question(prompt=prompt, answer=answer))
    return questions


def check_response(question: Question, response: str) -> bool:
    response = response.strip()
    try:
        response = str(int(response))
    except ValueError:
        return False
    return response == question.answer
