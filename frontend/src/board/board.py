from pygame.display import flip
from pygame.time import delay

from src.card.card import Card
from src.utils.consts import ANCHO_VENTANA, ALTO_VENTANA
from src.card_container.card_container import CardContainer


class Board(CardContainer):
    """
    Board class that extends CardContainer.
    Represents the game board where cards are played and matched.
    """

    def __init__(self):
        """
        Initializes a new instance of the Board class.
        """
        super().__init__()

    def add(self, card: Card) -> None:
        """
        Adds a card to the board if it matches the last card in the board.

        Args:
            card (Card): The card to be added to the board.

        Raises:
            RuntimeError: If the card added does not match the last card in the board.
        """
        if not self._cards:  # Check if the board is empty
            self._cards.append(card)
            return
        last_card = self._cards[-1]
        if card.match(last_card):
            self._cards.append(card)
            return
        raise RuntimeError("Carta agregada no válida.")

    def get(self, index: int) -> Card:
        """
        Returns the card at the given index in the board.

        Args:
            index (int): The index of the card to be retrieved.

        Returns:
            Card: The card at the given index.
        """
        return self._cards[index]

    def delete(self) -> Card:
        """
        Removes and returns the last card in the board.

        Returns:
            Card: The removed card.
        """
        return self._cards.pop()


class Tablero:
    def __init__(self):
        self.cartas_jugadas = []

    def agregar_carta(self, card: Card, jugador):
        self.cartas_jugadas.append(card)

    def obtener_ultima_carta(self):
        return self.cartas_jugadas[-1] if self.cartas_jugadas else None


def dibujar_tablero(ventana, tablero):
    if tablero.obtener_ultima_carta():
        ventana.blit(tablero.obtener_ultima_carta().img,
                     (ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 - 50))


def dibujar_carta_moviendose(ventana, card: Card, pos_inicial, pos_final, pasos):
    paso_actual = 0
    pos_actual = pos_inicial

    while paso_actual <= pasos:
        pos_actual[0] += (pos_final[0] - pos_inicial[0]) / pasos
        pos_actual[1] += (pos_final[1] - pos_inicial[1]) / pasos

        ventana.blit(card.img, pos_actual)
        flip()
        delay(10)

        paso_actual += 1
