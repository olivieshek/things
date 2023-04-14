""" This program is generating uni-passwords """

import random  # Random choosing symbols


LATIN_LOWER = "abcdefghijklmnopqrstuvwxyz"
LATIN_UPPER = LATIN_LOWER.upper()
NUMERALS = "1234567890"


def generate(
    length: int = 14,
    symbols: str = LATIN_LOWER + LATIN_UPPER + NUMERALS,
    special_symbols: str = "-",
):
    """Main function of the program"""
    result = str()

    for i in range(length):
        if random.randrange(0, 8) == 1:
            result += special_symbols[random.randrange(0, len(special_symbols))]
        result += symbols[random.randrange(0, len(symbols))]
    return result


print(generate())
