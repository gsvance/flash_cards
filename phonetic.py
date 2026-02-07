from typing import Final

from question_types import Question


# Source: https://en.wikipedia.org/wiki/NATO_phonetic_alphabet
NATO_PHONETIC_ALPHABET_COPY_PASTED: Final[str] = """
Alfa 	November
Bravo 	Oscar
Charlie 	Papa
Delta 	Quebec
Echo 	Romeo
Foxtrot 	Sierra
Golf 	Tango
Hotel 	Uniform
India 	Victor
Juliett 	Whiskey
Kilo 	Xray
Lima 	Yankee
Mike 	Zulu 
"""
NATO_PHONETIC_ALPHABET: Final[dict[str, str]] = {
    word[0].upper(): word.title()
    for word in NATO_PHONETIC_ALPHABET_COPY_PASTED.strip().split()
}


def generate_questions() -> list[Question]:
    questions: list[Question] = []
    for letter in sorted(NATO_PHONETIC_ALPHABET.keys()):
        word = NATO_PHONETIC_ALPHABET[letter]
        questions.append(Question(prompt=letter, answer=word))
    return questions


def check_response(question: Question, response: str) -> bool:
    response = response.strip().title()
    return response == question.answer
