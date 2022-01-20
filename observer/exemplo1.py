from typing import Protocol


class Observer(Protocol):
    def update(self) -> None:
        ...


class Subject(Protocol):
    def attach(self, observer: Observer) -> None:
        ...

    def detach(self, observer: Observer) -> None:
        ...

    def notify(self) -> None:
        ...


class ConcreteSubject(Subject):
    """
    >>> subject = ConcreteSubject(name='subject')
    >>> observer1 = ConcreteObserver(subject, name='observer1')
    >>> observer2 = ConcreteObserver(subject, name='observer2')
    >>> subject.state = 'Novo estado'
    observer2: subject mudou seu estado para 'Novo estado'
    observer1: subject mudou seu estado para 'Novo estado'
    """

    def __init__(self, name: str) -> None:
        self._observers: set[Observer] = set()
        self.name = name
        self._state: str = ''

    def __str__(self) -> str:
        return self.name

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        self._state = value
        self.notify()

    def attach(self, observer: Observer) -> None:
        self._observers.add(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.discard(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update()


class ConcreteObserver(Observer):
    def __init__(self, subject: ConcreteSubject, name: str) -> None:
        self.subject = subject
        self.subject.attach(self)
        self.name = name
        self.state: str = ''

    def __str__(self) -> str:
        return self.name

    def update(self) -> None:
        self.state = self.subject.state
        print(f'{self}: {self.subject} mudou seu estado para {self.state!r}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
