from dataclasses import dataclass
from typing import Protocol


class FlyBehavior(Protocol):
    def fly(self) -> None:
        ...


class FlyNoWay:
    def fly(self) -> None:
        print('Não sai do lugar...')


class FlyThroughWindow:
    def fly(self) -> None:
        print('Voando pela janela...')


class FlyLow:
    def fly(self) -> None:
        print('Voando baixo...')


class FlyHigh:
    def fly(self) -> None:
        print('Voando alto...')


class QuackBehavior(Protocol):
    def quack(self) -> None:
        ...


class Quack:
    def quack(self) -> None:
        print('Grasnando...')


class Squeak:
    def quack(self) -> None:
        print('Chiando...')


class Duck(Protocol):
    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()


@dataclass
class MallardDuck(Duck):
    """
    >>> mallard_duck = MallardDuck()
    >>> mallard_duck.perform_fly()
    Voando baixo...
    >>> mallard_duck.perform_quack()
    Grasnando...
    >>> mallard_duck.fly_behavior = FlyHigh()
    >>> mallard_duck.perform_fly()
    Voando alto...
    """
    fly_behavior = FlyLow()
    quack_behavior = Quack()


@dataclass
class RubberDuck(Duck):
    """
    >>> rubber_duck = RubberDuck()
    >>> rubber_duck.perform_fly()
    Não sai do lugar...
    >>> rubber_duck.perform_quack()
    Chiando...
    >>> rubber_duck.fly_behavior = FlyThroughWindow()
    >>> rubber_duck.perform_fly()
    Voando pela janela...
    """
    fly_behavior = FlyNoWay()
    quack_behavior = Squeak()


if __name__ == '__main__':
    import doctest
    doctest.testmod()