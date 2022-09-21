import os
from dotenv import load_dotenv
load_dotenv()

SECRET = os.getenv('SECRET')
SECRET2 = os.getenv('ANOTHER_SECRET')


def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return not is_even(num)


print(SECRET2)