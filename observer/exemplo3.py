import itertools
from contextlib import suppress
from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class Product:
    description: str
    price: float

    def __str__(self) -> str:
        return self.description

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return False
        return self.description.casefold() == other.description.casefold()


class Observer(Protocol):
    def update(self, offers: list[Product]) -> None:
        ...


class Subject(Protocol):
    def register_observer(self, observer: Observer) -> None:
        ...

    def remove_observer(self, observer: Observer) -> None:
        ...

    def notify_observers(self) -> None:
        ...


class Store(Subject):
    def __init__(self, name: str) -> None:
        self.name = name
        self.email_list: list[Observer] = []
        self._offers: list[Product] = []
        print(f'A loja {self} foi inaugurada')

    def __str__(self) -> str:
        return self.name

    @property
    def offers(self):
        return self._offers

    @offers.setter
    def offers(self, offers: list[Product]):
        self._offers = offers
        self.new_offers_added()

    def new_offers_added(self):
        print(f'A loja {self} divulgou uma nova promoção')
        self.notify_observers()
        print(f'A loja {self} encerrou a promoção')

    def register_observer(self, observer: Observer) -> None:
        if observer not in self.email_list:
            self.email_list.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        with suppress(ValueError):
            self.email_list.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.email_list:
            observer.update(self.offers)


@dataclass
class Customer(Observer):
    name: str
    wishlist: list[Product] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def subscribe_mailing_list(self, store: Store) -> None:
        print(
            f'Cliente {self} assinou o recebimento '
            f'de emails promocionais da loja {store}'
        )
        store.register_observer(self)

    def unsubscribe_mailing_list(self, store: Store) -> None:
        store.remove_observer(self)
        print(
            f'Cliente {self} cancelou o recebimento '
            f'de emails promocionais da loja {store}'
        )

    def update(self, offers: list[Product]) -> None:
        self.check_offers(offers)

    def check_offers(self, offers: list[Product]) -> None:
        print(f'Cliente {self} checa se tem algo do seu interesse...')
        for offer, item in itertools.product(offers, self.wishlist):
            if offer == item and offer.price <= item.price:
                self.buy(item)

    def buy(self, product: Product):
        print(f'Cliente {self} comprou {product}')
        self.wishlist.remove(product)


def main():
    """
    >>> store = Store('ABC')
    A loja ABC foi inaugurada

    >>> c1 = Customer(
    ...     name='1',
    ...     wishlist = [
    ...         Product('Celular', 1300),
    ...         Product('Fone', 150),
    ...         Product('Ventilador', 90),
    ...         Product('Bicicleta', 2900),
    ...     ]
    ... )
    >>> c1.subscribe_mailing_list(store)
    Cliente 1 assinou o recebimento de emails promocionais da loja ABC

    >>> c2 = Customer(
    ...     name='2',
    ...     wishlist = [
    ...         Product('Airfryer', 250),
    ...         Product('TV', 2500),
    ...     ]
    ... )
    >>> c2.subscribe_mailing_list(store)
    Cliente 2 assinou o recebimento de emails promocionais da loja ABC

    >>> c3 = Customer('3')
    >>> c3.wishlist.append(Product('Celular', 1400))
    >>> c3.subscribe_mailing_list(store)
    Cliente 3 assinou o recebimento de emails promocionais da loja ABC

    >>> mothers_day_offers = [
    ...     Product('Celular', 1500),
    ...     Product('Airfryer', 220),
    ...     Product('Robô Aspirador', 1000),
    ... ]
    >>> store.offers = mothers_day_offers
    A loja ABC divulgou uma nova promoção
    Cliente 1 checa se tem algo do seu interesse...
    Cliente 2 checa se tem algo do seu interesse...
    Cliente 2 comprou Airfryer
    Cliente 3 checa se tem algo do seu interesse...
    A loja ABC encerrou a promoção

    >>> c3.unsubscribe_mailing_list(store)
    Cliente 3 cancelou o recebimento de emails promocionais da loja ABC

    >>> black_friday_offers = [
    ...     Product('Celular', 1100),
    ...     Product('TV', 2200),
    ...     Product('Bicicleta', 3000),
    ... ]
    >>> store.offers = black_friday_offers
    A loja ABC divulgou uma nova promoção
    Cliente 1 checa se tem algo do seu interesse...
    Cliente 1 comprou Celular
    Cliente 2 checa se tem algo do seu interesse...
    Cliente 2 comprou TV
    A loja ABC encerrou a promoção
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
