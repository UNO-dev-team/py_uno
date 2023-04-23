from src.board.board import dibujar_carta_moviendose
from src.hand.hand import Mano, Hand
from src.card.card import Card
from src.utils.consts import ALTO_VENTANA, ANCHO_VENTANA
from pygame.font import Font
from abc import ABC, abstractmethod


class BasePlayer(ABC):
    """BasePlayer.
    clase base para jugadores.
    """
    def __init__(self, name: str):
        self._name = name
        self._hand = Hand()

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
    def turn(self) -> Card:
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


def comer_carta(mazo, jugador, ventana):
    if len(mazo.cartas) == 0:
        return

    carta = mazo.cartas.pop()
    print(f"comio carta el jugador: {jugador.nombre}")
    jugador.mano.agregar_carta(carta)
    pos_inicial = [ANCHO_VENTANA // 2 - 170, ALTO_VENTANA // 2 - 60]
    # Añade la animación de tomar cartas
    if jugador.nombre == "Jugador 1":
        pos_final = [
            50 + 30 * (len(jugador.mano.cartas) - 1), ALTO_VENTANA - 200]
    elif jugador.nombre == "IA 1":
        pos_final = [50 + 30 * (len(jugador.mano.cartas) - 1), 10]
    elif jugador.nombre == "IA 2":
        pos_final = [ANCHO_VENTANA - 100, 10]
    elif jugador.nombre == "IA 3":
        pos_final = [ANCHO_VENTANA - 100, ALTO_VENTANA - 100]

    dibujar_carta_moviendose(ventana, carta, pos_inicial, pos_final, 20)
