"""Card Container module, the base for all other clard holding classes"""


from abc import ABC, abstractmethod
from typing import List

from src.card.card import Card


class CardContainer(ABC):
    """"Abstract class used to create other card containers"""

    def __init__(self):
        self._cards: List[Card] = list()

    @property
    def is_empty(self) -> bool:
        """Is the card container empty"""
        return len(self._cards) == 0

    def get_all(self) -> List[Card]:
        """Returns a copy the current list of cards of this container"""
        return list(self._cards)

    def delete(self, index: int) -> None:
        """Deletes the card at the provided index"""
        self._cards.pop(index)

    @abstractmethod
    def add(self, card: Card) -> None:
        """TBD"""

    @abstractmethod
    def get(self, index: int) -> Card:
        """TBD"""
