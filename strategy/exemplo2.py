from typing import Callable


def calculate(arg1: int, arg2: int, strategy: Callable) -> int | float:
    return strategy(arg1, arg2)


def addition(number1: int, number2: int) -> int:
    print(f'{number1} + {number2} = {number1 + number2}')
    return number1 + number2


def subtraction(number1: int, number2: int) -> int:
    print(f'{number1} - {number2} = {number1 - number2}')
    return number1 - number2


def multiplication(number1: int, number2: int) -> int:
    print(f'{number1} * {number2} = {number1 * number2}')
    return number1 * number2


def division(number1: int, number2: int) -> float:
    print(f'{number1} / {number2} = {number1 / number2}')
    return number1 / number2


def main():
    assert calculate(4, 6, strategy=addition) == 10
    assert calculate(4, 6, strategy=subtraction) == -2
    assert calculate(4, 6, strategy=multiplication) == 24
    assert calculate(4, 6, strategy=division) == 0.6666666666666666
    

if __name__ == '__main__':
    main()
