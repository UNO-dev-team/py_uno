"""Card Container module, the base for all other clard holding classes"""


from abc import ABC, abstractmethod
from typing import List

from src.card.card import Card


class CardContainer(ABC):

    def __init__(self):
        self._cards: List[Card] = list()

    @property
    def is_empty(self) -> bool:
        return len(self._cards) == 0

    @abstractmethod
    def add(self, card: Card) -> None:
        pass

    @abstractmethod
    def get(self, index: int) -> Card:
        pass

    @abstractmethod
    def get_all(self) -> List[Card]:
        pass

    @abstractmethod
    def delete(self, card: Card) -> None:
        pass
