"""Card Module"""

from dataclasses import dataclass, field

from pygame import Surface

from src.utils.consts import Color, Value
from src.utils.images import load_image


@dataclass
class Card:
    """Dataclass used to represent a card"""

    color: Color
    value: Value
    img: Surface = field(init=False, compare=False, repr=False)

    def __post_init__(self):
        self.img = load_image(f"{self.color.value}_{self.value.value}")

    def match(self, card) -> bool:
        """Checks if the card value or color
          is the same as the supplied card"""

        if isinstance(card, Card):
            return (self.value == card.value) or (self.color == card.color)
        return False
