from typing import NamedTuple, Final


VERTICAL: Final[str] = chr(0x2502)
HORIZONTAL: Final[str] = chr(0x2500)
UPPER_LEFT: Final[str] = chr(0x256d)
UPPER_RIGHT: Final[str] = chr(0x256e)
LOWER_LEFT: Final[str] = chr(0x2570)
LOWER_RIGHT: Final[str] = chr(0x256f)
BLANK: Final[str] = ' '


class Dimensions(NamedTuple):
    width: int
    height: int


def text_dimensions(text: str) -> Dimensions:
    lines = text.split('\n')
    width = max(len(line) for line in lines)
    height = len(lines)
    return Dimensions(width=width, height=height)


def flash_card_string(
    text: str,
    *,
    min_width: int = 0,
    min_height: int = 0,
    indent: int = 0,
) -> str:
    text_dims = text_dimensions(text)
    card_width = max(text_dims.width, min_width)
    card_height = max(text_dims.height, min_height)
    num_blank_lines = card_height - text_dims.height
    text_lines = text.split('\n')
    card_lines = []
    card_lines.append(
        indent*BLANK + UPPER_LEFT + HORIZONTAL*card_width + UPPER_RIGHT
    )
    for _ in range(num_blank_lines // 2):
        card_lines.append(
            indent*BLANK + VERTICAL + BLANK*card_width + VERTICAL
        )
    for text_line in text_lines:
        centered_text_line = text_line.center(card_width, BLANK)
        card_lines.append(
            indent*BLANK + VERTICAL + centered_text_line + VERTICAL
        )
    for _ in range(num_blank_lines - (num_blank_lines // 2)):
        card_lines.append(
            indent*BLANK + VERTICAL + BLANK*card_width + VERTICAL
        )
    card_lines.append(
        indent*BLANK + LOWER_LEFT + HORIZONTAL*card_width + LOWER_RIGHT
    )
    return '\n'.join(card_lines)


if __name__ == '__main__':
    string = 'ABC\nDEFGH\nIJK'
    dims = text_dimensions(string)
    print()
    print(flash_card_string(
        string,
        min_width=dims.width + 2*2,
        min_height=dims.height + 2*1,
        indent=2,
    ))
    print()
