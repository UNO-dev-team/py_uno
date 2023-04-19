from src.board.board import dibujar_carta_moviendose
from src.hand.hand import Mano
from src.utils.consts import ALTO_VENTANA, ANCHO_VENTANA
from pygame.font import Font


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
