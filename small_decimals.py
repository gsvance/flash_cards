from fractions import Fraction
from typing import Final

from question_types import Question


MIN_DENOMINATOR: Final[int] = 2
MAX_DENOMINATOR: Final[int] = 12
assert MIN_DENOMINATOR <= MAX_DENOMINATOR

NUM_DIGITS: Final[int] = 2
assert NUM_DIGITS > 0
FORMAT_STRING: Final[str] = '{:.' + str(NUM_DIGITS) + 'f}'


def generate_questions() -> list[Question]:
    used_fractions: set[Fraction] = set()
    used_prompts: set[str] = set()
    questions: list[Question] = []
    for denominator in range(MIN_DENOMINATOR, MAX_DENOMINATOR + 1):
        for numerator in range(1, denominator):
            fraction = Fraction(numerator, denominator)
            if fraction in used_fractions:
                continue
            used_fractions.add(fraction)
            prompt = FORMAT_STRING.format(float(fraction))
            if prompt in used_prompts:
                raise ValueError('a non-unique decimal prompt was generated')
            used_prompts.add(prompt)
            answer = str(fraction)
            questions.append(Question(prompt=prompt, answer=answer))
    return questions


def check_response(question: Question, response: str) -> bool:
    response_parts = response.strip().split('/')
    try:
        numerator, denominator = [int(part.strip()) for part in response_parts]
    except (ValueError, TypeError):
        return False
    answer = Fraction(question.answer)
    return numerator == answer.numerator and denominator == answer.denominator
