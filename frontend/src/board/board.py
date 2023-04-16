from src.utils.consts import ANCHO_VENTANA, ALTO_VENTANA
from pygame.display import flip
from pygame.time import delay


class Tablero:
    def __init__(self):
        self.cartas_jugadas = []

    def agregar_carta(self, carta, jugador):
        print()
        print(f"{jugador} jugo la carta: {carta.color} - {carta.valor}")
        self.cartas_jugadas.append(carta)

    def obtener_ultima_carta(self):
        return self.cartas_jugadas[-1] if self.cartas_jugadas else None


def dibujar_tablero(ventana, tablero):
    if tablero.obtener_ultima_carta():
        ventana.blit(tablero.obtener_ultima_carta().imagen,
                     (ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 - 50))


def dibujar_carta_moviendose(ventana, carta, pos_inicial, pos_final, pasos):
    paso_actual = 0
    pos_actual = pos_inicial

    while paso_actual <= pasos:
        pos_actual[0] += (pos_final[0] - pos_inicial[0]) / pasos
        pos_actual[1] += (pos_final[1] - pos_inicial[1]) / pasos

        ventana.blit(carta.imagen, pos_actual)
        flip()
        delay(10)

        paso_actual += 1
