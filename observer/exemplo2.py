from typing import Protocol


class Observer(Protocol):
    def update(self) -> None:
        ...


class Subject(Protocol):
    def register_observer(self, observer: Observer) -> None:
        ...

    def unregister_observer(self, observer: Observer) -> None:
        ...

    def notify_observers(self) -> None:
        ...


class Display(Protocol):
    def display(self) -> None:
        ...


class WeatherData(Subject):
    """
    >>> weather_data = WeatherData()
    >>> CurrentConditionsDisplay(weather_data)  # doctest: +ELLIPSIS
    <__main__.CurrentConditionsDisplay object at ...>
    >>> StatisticsDisplay(weather_data)  # doctest: +ELLIPSIS
    <__main__.StatisticsDisplay object at ...>
    >>> ForecastDisplay(weather_data)  # doctest: +ELLIPSIS
    <__main__.ForecastDisplay object at ...>
    >>> weather_data.set_measurements(26, 82, 28.4)
    Condições atuais: 26ºc e 82% de umidade
    Tempo estável
    Média: 26.0ºc | mínima: 26.0ºc | máxima: 26.0ºc
    >>> weather_data.set_measurements(28, 65, 29.2)
    Condições atuais: 28ºc e 65% de umidade
    Previsão de sol
    Média: 27.0ºc | mínima: 26.0ºc | máxima: 28.0ºc
    >>> weather_data.set_measurements(25, 90, 27)
    Condições atuais: 25ºc e 90% de umidade
    Previsão de chuva
    Média: 26.3ºc | mínima: 25.0ºc | máxima: 28.0ºc
    """

    temperature: float
    humidity: float
    pressure: float

    def __init__(self) -> None:
        self._observers: set[Observer] = set()

    def register_observer(self, observer: Observer) -> None:
        self._observers.add(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.discard(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

    def set_measurements(
        self,
        temperature: float,
        humidity: float,
        pressure: float,
    ) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    def measurements_changed(self) -> None:
        self.notify_observers()


class CurrentConditionsDisplay(Observer, Display):
    """
    >>> weather_data = WeatherData()
    >>> CurrentConditionsDisplay(weather_data)  # doctest: +ELLIPSIS
    <__main__.CurrentConditionsDisplay object at ...>
    >>> weather_data.set_measurements(26, 82, 28.4)
    Condições atuais: 26ºc e 82% de umidade
    >>> weather_data.set_measurements(28, 65, 29.2)
    Condições atuais: 28ºc e 65% de umidade
    >>> weather_data.set_measurements(25, 90, 27)
    Condições atuais: 25ºc e 90% de umidade
    """

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self) -> None:
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self) -> None:
        print(
            'Condições atuais:',
            f'{self.temperature}ºc e {self.humidity}% de umidade',
        )


class StatisticsDisplay(Observer, Display):
    """
    >>> weather_data = WeatherData()
    >>> StatisticsDisplay(weather_data)  # doctest: +ELLIPSIS
    <__main__.StatisticsDisplay object at ...>
    >>> weather_data.set_measurements(26, 82, 28.4)
    Média: 26.0ºc | mínima: 26.0ºc | máxima: 26.0ºc
    >>> weather_data.set_measurements(28, 65, 29.2)
    Média: 27.0ºc | mínima: 26.0ºc | máxima: 28.0ºc
    >>> weather_data.set_measurements(25, 90, 27)
    Média: 26.3ºc | mínima: 25.0ºc | máxima: 28.0ºc
    """

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperatures: list[float] = []

    def update(self) -> None:
        self.temperatures.append(self.weather_data.temperature)
        self.display()

    def display(self) -> None:
        average_temp = sum(self.temperatures) / len(self.temperatures)
        min_temp = min(self.temperatures)
        max_temp = max(self.temperatures)
        print(
            f'Média: {average_temp:.1f}ºc',
            f'mínima: {min_temp:.1f}ºc',
            f'máxima: {max_temp:.1f}ºc',
            sep=' | ',
        )


class ForecastDisplay(Observer, Display):
    """
    >>> weather_data = WeatherData()
    >>> ForecastDisplay(weather_data)  # doctest: +ELLIPSIS
    <__main__.ForecastDisplay object at ...>
    >>> weather_data.set_measurements(26, 82, 28.4)
    Tempo estável
    >>> weather_data.set_measurements(28, 65, 29.2)
    Previsão de sol
    >>> weather_data.set_measurements(25, 90, 27)
    Previsão de chuva
    """

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.last_pressure: float | None = None
        self.current_pressure: float | None = None

    def update(self) -> None:
        if self.current_pressure is None:
            self.last_pressure = self.weather_data.pressure
            self.current_pressure = self.weather_data.pressure
        else:
            self.last_pressure = self.current_pressure
            self.current_pressure = self.weather_data.pressure
        self.display()

    def display(self) -> None:
        if self.last_pressure is None or self.current_pressure is None:
            return
        if self.current_pressure > self.last_pressure:
            print('Previsão de sol')
        elif self.current_pressure == self.last_pressure:
            print('Tempo estável')
        else:
            print('Previsão de chuva')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
