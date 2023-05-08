from dataclasses import dataclass


@dataclass
class Position:
    """Position.
    Allows to have a two dimensional position for displaying in pygame.

    args:
        x (int): x position
        y (int): y position
    """
    x: int
    y: int

    def tuple(self):
        """Returns a tuple with the coordinates."""
        return (self.x, self.y)
