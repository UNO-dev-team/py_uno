"""Deck Module"""
from random import shuffle

from src.card.card import Card
from src.card_container.card_container import CardContainer
from src.utils.deck_creation import all_card_colors, all_card_values
from src.utils.consts import Color, Value


class Deck(CardContainer):
    """The board deck it holds the all the cards"""

    def add(self, card: Card) -> None:
        """Adds the card to the back of the deck"""
        self._cards.append(card)

    def get(self, index: int) -> Card:
        """ Returns a card at the given index and 
        removes it from the deck"""
        return self._cards.pop(index)

    def shuffle(self) -> None:
        """Shuffles the deck in place and returns None"""
        shuffle(self._cards)

    def give_card(self, container: CardContainer = None, n: int = 1) -> None:
        """Gives n cards from the front of the deck to
        the provided CardContainer, n defaults to 1"""
        if container is None:
            return [self.get(0) for _ in range(n)]

        for _ in range(n):
            container.add(self.get(0))

    def init_deck(self) -> None:
        """Handles the creation of a new standar uno deck"""
        colors: list[Color] = all_card_colors()
        values: list[Value] = all_card_values()

        # We create the all the cards and add it to the deck
        for color in colors:
            for value in values:
                self.add(
                    Card(
                        color=color,
                        value=value
                    )
                )
                if value.value != "0":
                    self.add(
                        Card(color=color, value=value)
                    )
