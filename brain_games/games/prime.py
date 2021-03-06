"""Logic of game: prime check"""


import random


START_MSG = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    div = 2
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def generate_qa():
    question = random.randint(-100, 100)
    answer = ('yes' if is_prime(question) is True else 'no')
    return (question, answer)
