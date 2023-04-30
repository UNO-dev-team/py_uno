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


class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def quitar_carta(self, indice):
        return self.cartas.pop(indice)


def dibujar_cartas_mano(ventana, jugador, x_offset, y_offset, carta_resaltada=None):
    espaciado = 30 if len(
        jugador.mano.cartas) <= 20 else 800 // len(jugador.mano.cartas)

    for indice_carta, carta in enumerate(jugador.mano.cartas):
        x_pos = x_offset + espaciado * indice_carta
        if carta_resaltada is not None and indice_carta == carta_resaltada:
            imagen_resaltada = scale(carta.img, (int(
                carta.img.get_width() * 1.2), int(carta.img.get_height() * 1.2)))
            ventana.blit(imagen_resaltada, (x_pos -
                         int(carta.img.get_width() * 0.1), y_offset - 50))
        else:
            ventana.blit(carta.img, (x_pos, y_offset))
