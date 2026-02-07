from typing import Callable, NamedTuple, TypeAlias


class Question(NamedTuple):
    prompt: str
    answer: str


Checker: TypeAlias = Callable[[Question, str], bool]
