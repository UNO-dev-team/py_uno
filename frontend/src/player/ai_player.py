from src.player.player import BasePlayer
from card.card import Card
from src.card.card import Card
from src.utils.consts import Value
from typing import Optional


class AIPlayer(BasePlayer):
    """AIPlayer class
    Class that allows to play against the computer.

    args:
        name (str): Name of the player
    """
    def __init__(self, name: str, x: int, y: int):
        super().__init__(name, x, y)

    def turn(self, prev_card: Card, acc: int = 0) -> Optional[Card]:
        """Turn.
        Method that verifies which card to play. Return None if the previous card is special
        and the player has no card to play. Otherwise, will eat until find a card.

        Args:
            prev_card (Card): Card played before previous one.

        Returns:
            Optional[Card]: Next card to play. None if previous card is special and player
            has no card to play.
        """
        cards = self._hand.iterate()
        turn_over = False

        while not turn_over:
            for idx, card in enumerate(cards):

                if acc > 0 and prev_card.value == Value.TAKE_TWO:
                   return self.put_card(idx) 

                if prev_card.match(card):
                    return self.put_card(idx)
            
        return None

    def take_card(self, c: Card) -> None:
        """Take card.
        Add the card to the deck.

        Args:
            c (Card): Card to add.
        """
        self._hand.append(c)

    def delete_card(self, c: Card = None, idx: int = -1) -> None:
        """Deletes the card indicated by the index or the card to be deleted.

        Raises:
            RuntimeError: you does not provides a valid index or Card.
        """
        if c in None or idx == -1:
            raise RuntimeError('Card or index must be provided')
        
        if c is not None:
            idx = self._hand.index(c)
        
        if idx == -1:
            raise RuntimeError('Card does not exist on the hand of the player.')
        
        self.put_card(idx)

    def put_card(self, idx: int) -> Card:
        """Put card.
        This method returns the card indicated by the index. Also deletes the card from the hand.

        Args:
            idx (int): The index of the card to return.
        """
        return self._hand.pop(idx)
