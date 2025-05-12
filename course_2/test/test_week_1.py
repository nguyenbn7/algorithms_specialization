from sys import path as sys_path
from os import path as os_path

# Resolve for parent module
current = os_path.dirname(os_path.realpath(__file__))
sys_path.append(os_path.join(current, ".."))

from course_2.src.week_1 import karatsuba


def test_question():
    answer = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184

    with open(os_path.join(current, "../input/week_1/question.txt"), "r") as f:
        num1, num2 = map(int, f.readline().split())

    attempt = karatsuba(num1, num2)

    assert attempt == answer
