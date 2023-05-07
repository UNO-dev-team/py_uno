from src.utils import consts
from src.utils.position import Position

from src.drawer.drawer import Drawer
from src.hand.hand import Mano, Hand
from src.card.card import Card
from src.drawer.drawer import Drawer
from src.utils.consts import ALTO_VENTANA, ANCHO_VENTANA
from src.utils.consts import special_card
from pygame.font import Font
from abc import ABC, abstractmethod
from typing import Optional


class BasePlayer(ABC):
    """BasePlayer.
    clase base para jugadores.
    """

    def __init__(self, name: str, x: int, y: int):
        self._name = name
        self._hand = Hand()
        self._position = Position(x, y)

    @property
    def name(self) -> str:
        """Name.

        Returns:
            str: Return the name of the player.
        """
        return self._name

    @property
    def is_winner(self) -> bool:
        """is_winner.
        Returns a boolean indicating the player is winner.

        Returns:
            bool: The hand is empty.
        """
        return self._hand.empty

    @abstractmethod
    def turn(self, previous_card: Card) -> Optional[Card]:
        """Turn.
        When is called, this method returns a Card instance, which follows the game logic.

        returns:
            Card: The following card to play.
        """

    @abstractmethod
    def take_card(self, c: Card) -> None:
        """Take card.
        This method adds to the hand the passed card.

        Args:
            c (Card): Card to add

        retunrs:
            None
        """

    @abstractmethod
    def delete_card(self, c: Card = None, idx: int = -1) -> None:
        """Deletes the card indicated by the index or the card to be deleted.

        Raises:
            RuntimeError: you does not provides a valid index or Card.
        """

    @abstractmethod
    def put_card(self, idx: int) -> Card:
        """Put card.
        This method returns the card indicated by the index. Also deletes the card from the hand.

        Args:
            idx (int): The index of the card to return.
        """

    @property
    def position(self):
        return self._position.tuple()

    def __len__(self) -> int:
        return len(self._hand)


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = Mano()


def dibujar_info_jugadores(ventana, jugadores):
    fuente = Font(None, 24)
    for i, jugador in enumerate(jugadores):
        nombre = f"{jugador.nombre}: {len(jugador.mano.cartas)} cartas"
        texto = fuente.render(nombre, 1, (0, 0, 0))
        if i == 0:
            ventana.blit(texto, (10, ALTO_VENTANA - 280))
        elif i == 1:
            ventana.blit(texto, (10, 10))
        elif i == 2:
            ventana.blit(texto, (ANCHO_VENTANA - 200, 10))
        elif i == 3:
            ventana.blit(texto, (ANCHO_VENTANA - 200, ALTO_VENTANA - 280))


def comer_carta(mazo, jugador):
    if len(mazo.cartas) == 0:
        return

    carta = mazo.cartas.pop()
    print(f"comio carta el jugador: {jugador.nombre}")
    jugador.mano.agregar_carta(carta)

    # Añade la animación de tomar cartas
    x_start, y_start = consts.DECK_POSITION
    start = Position(x_start, y_start)

    if jugador.nombre == "Jugador 1":
        x_end, y_end = (
            50 + 30 * (len(jugador.mano.cartas) - 1), ALTO_VENTANA - 200)
    elif jugador.nombre == "IA 1":
        x_end, y_end = (50 + 30 * (len(jugador.mano.cartas) - 1), 10)
    elif jugador.nombre == "IA 2":
        x_end, y_end = (ANCHO_VENTANA - 100, 10)
    elif jugador.nombre == "IA 3":
        x_end, y_end = (ANCHO_VENTANA - 100, ALTO_VENTANA - 100)

    end = Position(x_end, y_end)

    Drawer.draw_moving_card(carta, start, end)
