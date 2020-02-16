from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self._v = v

    @property
    def consumption(self):
        v = self._v / 6.5 + 0.5
        return v


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self._h = h

    @property
    def consumption(self):
        h = 2 * self._h + 0.3
        return h


a = Coat('пальто', 48)
b = Suit('костюм', 1.75)

print(a.consumption + b.consumption)

