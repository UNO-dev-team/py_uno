from pygame.display import flip
from pygame.time import delay

from src.card.card import Card
from src.utils.consts import ANCHO_VENTANA, ALTO_VENTANA


class Tablero:
    def __init__(self):
        self.cartas_jugadas = []

    def agregar_carta(self, card: Card, jugador):
        print()
        print(f"{jugador} jugo la carta: {card.color.value} - {card.value.value}")
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
