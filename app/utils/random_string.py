import string
import random


def random_string(length: int = 3):
    string_generator = string.ascii_letters
    random_string = ''.join(random.choice(string_generator) for i in range(length))
    return random_string
