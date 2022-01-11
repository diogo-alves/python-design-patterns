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

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self.quack_behavior = quack_behavior

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()


@dataclass
class MallardDuck(Duck):
    fly_behavior = FlyLow()
    quack_behavior = Quack()


@dataclass
class RubberDuck(Duck):
    fly_behavior = FlyNoWay()
    quack_behavior = Squeak()


if __name__ == '__main__':
    print('Narrador: vamos observar um pato selvagem:')
    mallard_duck = MallardDuck()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()
    print('Narrador: Oh, não! Um caçador apareceu!')
    mallard_duck.set_fly_behavior(FlyHigh())
    mallard_duck.perform_fly()

    print('\nNarrador: Vamos observar o pato de borracha de uma criança:')
    rubber_duck = RubberDuck()
    rubber_duck.perform_quack()
    rubber_duck.perform_fly()
    print('Narrador: Xiii... ela descobriu que não era um pato de verdade!')
    rubber_duck.set_fly_behavior(FlyThroughWindow())
    rubber_duck.perform_fly()
