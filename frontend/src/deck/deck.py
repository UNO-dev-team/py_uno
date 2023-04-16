from src.utils.consts import ALTO_VENTANA, ANCHO_VENTANA
from src.utils.images import cargar_imagen

from src.card.card import Carta

from pygame.transform import scale
from pygame.font import Font
from random import shuffle

class Mazo:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def barajar(self):
        shuffle(self.cartas)

    def repartir(self, mano, cantidad):
        for _ in range(cantidad):
            mano.agregar_carta(self.cartas.pop())


def generate_deck():
    colores = ["rojo", "verde", "azul", "amarillo"]
    valores = list(range(10)) + ["salto", "reversa", "tome_dos"]
    mazo = Mazo()

    for color in colores:
        for valor in valores:
            if valor == 0:
                mazo.agregar_carta(
                    Carta(color, valor, cargar_imagen(f"{color}_{valor}")))
            else:
                for _ in range(2):
                    mazo.agregar_carta(
                        Carta(color, valor, cargar_imagen(f"{color}_{valor}")))

    return mazo


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
