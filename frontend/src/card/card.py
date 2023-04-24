"""Card Module"""

from dataclasses import dataclass, field

from pygame import Surface

from src.utils.consts import Color, Value
from src.utils.images import cargar_imagen


@dataclass
class Card:
    """Dataclass used to represent a card"""

    color: Color
    value: Value
    img: Surface = field(init=False, compare=False, repr=False)

    def __post_init__(self):
        self.img = cargar_imagen(f"{self.color.value}_{self.value.value}")
