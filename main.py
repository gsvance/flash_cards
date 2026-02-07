import random
import sys
import time
from types import ModuleType
from typing import Final

import flash_card_string
import question_types


import alphabetical
import phonetic
import small_decimals
import times_tables


SUBJECT_MODULES: Final[set[ModuleType]] = {
    alphabetical,
    phonetic,
    small_decimals,
    times_tables,
}
assert all(
    hasattr(subject_module, 'generate_questions')
    for subject_module in SUBJECT_MODULES
)
assert all(
    hasattr(subject_module, 'check_response')
    for subject_module in SUBJECT_MODULES
)


CARD_LEFT_RIGHT_MARGIN: Final[int] = 2
CARD_TOP_BOTTOM_MARGIN: Final[int] = 1
CARD_INDENT: Final[int] = 2


def run_quiz(
    questions: list[question_types.Question],
    checker: question_types.Checker,
    recycle: bool = True,
) -> None:
    prompt_dims = [
        flash_card_string.text_dimensions(q.prompt) for q in questions
    ]
    max_prompt_width = max(dims.width for dims in prompt_dims)
    max_prompt_height = max(dims.height for dims in prompt_dims)
    card_width = max_prompt_width + CARD_LEFT_RIGHT_MARGIN*2
    card_height = max_prompt_height + CARD_TOP_BOTTOM_MARGIN*2

    random.shuffle(questions)
    missed: list[question_types.Question] = []

    print(f'{len(questions)} questions generated and shuffled!')
    input('Press enter to begin...')

    while questions:

        while questions:
            question = questions.pop()
            card = flash_card_string.flash_card_string(
                question.prompt, min_width=card_width,
                min_height=card_height, indent=CARD_INDENT,
            )
            print('\n', card, '\n\n', sep='', end='')
            response = input('?> ')
            if checker(question, response):
                print('Correct! Nice job.')
            else:
                print(f'Sorry, the answer was {question.answer}.')
                missed.append(question)
            time.sleep(1.5)

        if recycle and missed:
            questions.extend(missed)
            random.shuffle(questions)
            missed.clear()

    print('\n', 'All questions completed.', sep='')


def main() -> None:
    assert len(sys.argv) == 2, 'one command line argument is required'
    _, subject = sys.argv
    subject_module = globals().get(subject)
    if subject_module not in SUBJECT_MODULES:
        raise ValueError(f'invalid subject: {subject}')
    questions = subject_module.generate_questions()
    checker = subject_module.check_response
    run_quiz(questions, checker)


if __name__ == '__main__':
    main()
