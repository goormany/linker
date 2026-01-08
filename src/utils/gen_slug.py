import random
from string import ascii_letters, digits

ALL_SYMBOLS = ascii_letters + digits


def get_slug(size: int = 6) -> str:
    slug = ""

    for _ in range(size):
        slug += random.choice(ALL_SYMBOLS)
    return slug
