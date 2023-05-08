from pygame.transform import scale
from src.card_container.card_container import CardContainer
from src.card.card import Card
from collections.abc import Iterable


class Hand(CardContainer):
    """Hand class.
    Asociated with player, contains all cards to be played. Inherits from CardContainer.
    """

    def __init__(self):
        super().__init__()

    def add(self, card: Card) -> None:
        """Add.
        This method allows to add a card into the hand of player. If needed multiple cards adding, recommended to use add_multiple_cards.

        Args:
            card: Card. Card to be added.

        returns: None.
        """
        self._cards.append(card)

    def add_multiple_cards(self, cards: Iterable[Card]) -> None:
        """Add multiple cards.
        This method allows to add multiple cards into the hand of player.
        Args:
            card: Interable[card]. Card to be added.

        returns: None.
        """
        self._cards.extend(cards)

    def get(self, index: int) -> Card:
        """Get.
        This method allows to get a card from the had of the player.
        """
        return self._cards[index]

    def iterate(self):
        """Iterate.
        This method returns a generator with the references to all of the cards.
        """
        return (card for card in self._cards)

    def pop(self, index: int):
        """POP.
        This method allows to get a card from the had of the player and delete it.
        """
        return self._cards.pop(index)


class Mano:
    """Una clase que representa la mano de un jugador en un juego de cartas (versión en español).

    La clase Mano está asociada con un jugador y contiene todas las cartas que
    pueden ser jugadas.
    """
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        """agregar_carta.
        This method allows to add a card into the hand of player

        Args:
            carta: Card. Card to be added.

        returns: None.
        """
        self.cartas.append(carta)

    def quitar_carta(self, indice):
        """quitar_carta.
        This method allows to delete a card into the hand of player.

        Args:
            indice: int. Card to be deleted.

        returns: None.
        """
        return self.cartas.pop(indice)


def dibujar_cartas_mano(ventana, jugador, x_offset, y_offset, carta_resaltada=None):
    """Dibuja las cartas en la mano de un jugador en la ventana de Pygame.

    Args:
        ventana (pygame.Surface): La superficie de Pygame donde se dibujarán las cartas.
        jugador: El jugador cuya mano se va a dibujar.
        x_offset (int): Desplazamiento en el eje X para las cartas en la ventana.
        y_offset (int): Desplazamiento en el eje Y para las cartas en la ventana.
        carta_resaltada (int, optional): El índice de la carta que se va a resaltar. Si es None, ninguna carta será resaltada. Por defecto es None.

    Returns:
        None
    """
    espaciado = 30 if len(
        jugador.hand) <= 20 else 800 // len(jugador.hand)

    for indice_carta, carta in enumerate(jugador.hand.iterate()):
        x_pos = x_offset + espaciado * indice_carta
        if carta_resaltada is not None and indice_carta == carta_resaltada:
            imagen_resaltada = scale(carta.img,
                                     (int(carta.img.get_width() * 1.2),
                                      int(carta.img.get_height() * 1.2)))
            ventana.blit(imagen_resaltada, (x_pos -
                         int(carta.img.get_width() * 0.1), y_offset - 50))
        else:
            ventana.blit(carta.img, (x_pos, y_offset))
