

from pygame.transform import scale
from pygame.font import Font
from random import shuffle

from src.card.card import Card
from src.utils.deck_creation import all_card_colors, all_card_values
from src.utils.consts import ALTO_VENTANA, ANCHO_VENTANA, Color, Value
from src.utils.images import cargar_imagen


class Mazo:
    def __init__(self):
        self.cartas: list[Card] = []

    def agregar_carta(self, carta: Card):
        self.cartas.append(carta)

    def barajar(self):
        shuffle(self.cartas)

    def repartir(self, mano, cantidad):
        for _ in range(cantidad):
            mano.agregar_carta(self.cartas.pop())


def generate_deck():
    """Handles the creation of a new standar uno deck"""
    colors: list[Color] = all_card_colors()
    values: list[Value] = all_card_values()
    deck = Mazo()

    # We create the all the cards and add it to the deck
    for color in colors:
        for value in values:
            deck.agregar_carta(
                Card(
                    color=color,
                    value=value
                )
            )
            if value.value != "0":
                deck.agregar_carta(
                    Card(color=color, value=value)
                )

    return deck


def dibujar_mazo(ventana, mazo):
    imagen_carta_volteada = cargar_imagen("mazo")
    ancho_mazo, alto_mazo = imagen_carta_volteada.get_size()
    img = scale(
        imagen_carta_volteada, (ancho_mazo // 3, alto_mazo // 3))
    mazo_rect = img.get_rect()
    # Ajusta la posición aquí
    mazo_rect.center = (ANCHO_VENTANA // 2 - 120, ALTO_VENTANA // 2 + 40)
    ventana.blit(img, mazo_rect)
    fuente = Font(None, 36)
    texto = fuente.render(str(len(mazo.cartas)), 1, (255, 255, 255))
    ventana.blit(texto, (ANCHO_VENTANA // 2 - 115, ALTO_VENTANA // 2 - 20))
