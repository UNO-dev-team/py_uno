import random
import os
import pygame
import time


def cargar_imagen(nombre):
    return pygame.image.load(
        f"images/{nombre}.png")


def generar_mazo():
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

    # for _ in range(4):
    #     mazo.agregar_carta(Carta("comodin", "cambiocolor",
    #                        cargar_imagen("cambiocolor.png")))
    #     mazo.agregar_carta(Carta("comodin", "mas4", cargar_imagen("mas4.png")))

    return mazo


def dibujar_tablero(ventana, tablero):
    if tablero.obtener_ultima_carta():
        ventana.blit(tablero.obtener_ultima_carta().imagen,
                     (ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 - 50))


def dibujar_mazo(ventana, mazo):
    imagen_carta_volteada = cargar_imagen("mazo")
    ancho_mazo, alto_mazo = imagen_carta_volteada.get_size()
    img = pygame.transform.scale(
        imagen_carta_volteada, (ancho_mazo // 3, alto_mazo // 3))
    mazo_rect = img.get_rect()
    # Ajusta la posición aquí
    mazo_rect.center = (ANCHO_VENTANA // 2 - 120, ALTO_VENTANA // 2 + 40)
    ventana.blit(img, mazo_rect)
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(str(len(mazo.cartas)), 1, (255, 255, 255))
    ventana.blit(texto, (ANCHO_VENTANA // 2 - 115, ALTO_VENTANA // 2 - 20))


def dibujar_cartas_mano(ventana, jugador, y_offset):
    x_offset = 50
    for carta in jugador.mano.cartas:
        ventana.blit(carta.imagen, (x_offset, y_offset))
        x_offset += 30


def comer_carta(mazo, jugador):
    if len(mazo.cartas) == 0:
        return

    carta = mazo.cartas.pop()
    print(f"comio carta el jugador: {jugador.nombre}")
    jugador.mano.agregar_carta(carta)


# Función para verificar si un movimiento es válido
def es_movimiento_valido(carta, ultima_carta):
    return carta.color == ultima_carta.color or carta.valor == ultima_carta.valor


def dibujar_turno(ventana, jugador_actual):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(f"Turno de {jugador_actual.nombre}", 1, (0, 0, 0))
    ventana.blit(texto, (ANCHO_VENTANA // 2 - 100, 50))


class Mazo:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def barajar(self):
        random.shuffle(self.cartas)

    def repartir(self, mano, cantidad):
        for _ in range(cantidad):
            mano.agregar_carta(self.cartas.pop())


class Carta:
    def __init__(self, color, valor, imagen):
        self.color = color
        self.valor = valor
        self.imagen = imagen

    def __str__(self):
        return f"{self.color} {self.valor}"


class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def quitar_carta(self, indice):
        return self.cartas.pop(indice)


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = Mano()


class Tablero:
    def __init__(self):
        self.cartas_jugadas = []

    def agregar_carta(self, carta):
        print(f"Se jugo la carta: {carta.valor}")
        self.cartas_jugadas.append(carta)

    def obtener_ultima_carta(self):
        return self.cartas_jugadas[-1] if self.cartas_jugadas else None


def dibujar_contador_cartas(ventana, jugador, x_offset, y_offset):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(str(len(jugador.mano.cartas)), 1, (0, 0, 0))
    ventana.blit(texto, (x_offset, y_offset))


pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Uno")


def main():
    reloj = pygame.time.Clock()
    mazo = generar_mazo()
    mazo.barajar()
    jugadores = [Jugador("Jugador 1"), Jugador("Jugador 2")]
    tablero = Tablero()
    for jugador in jugadores:
        mazo.repartir(jugador.mano, 7)
    tablero.agregar_carta(mazo.cartas.pop())
    turno = 0
    juego_terminado = False
    turno_completo = False

    while not juego_terminado:
        jugador_actual = jugadores[turno % len(jugadores)]

        if turno % len(jugadores) == 0:  # Jugador 1 (humano)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    juego_terminado = True

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if not turno_completo:
                        x, y = evento.pos
                        x_offset = 50

                        # Comer carta
                        if (ANCHO_VENTANA // 2 - 120) < x < (ANCHO_VENTANA // 2 - 20) and (ALTO_VENTANA // 2 - 70) < y < (ALTO_VENTANA // 2 + 30):
                            comer_carta(mazo, jugador_actual)
                            # turno_completo = True

                        # Jugar carta
                        for indice_carta, carta in reversed(list(enumerate(jugador_actual.mano.cartas))):
                            carta_rect = carta.imagen.get_rect(
                                topleft=(x_offset + 30 * indice_carta, ALTO_VENTANA - 200))
                            if carta_rect.collidepoint(x, y) and es_movimiento_valido(carta, tablero.obtener_ultima_carta()):
                                tablero.agregar_carta(
                                    jugador_actual.mano.quitar_carta(indice_carta))
                                turno_completo = True
                                break
        else:  # Jugador 2 (IA simple)
            if not turno_completo:
                pygame.time.delay(1000)
                carta_valida_encontrada = False

                for indice_carta, carta in enumerate(jugador_actual.mano.cartas):
                    if es_movimiento_valido(carta, tablero.obtener_ultima_carta()):
                        tablero.agregar_carta(
                            jugador_actual.mano.quitar_carta(indice_carta))
                        turno_completo = True
                        carta_valida_encontrada = True
                        break

                if not carta_valida_encontrada:
                    comer_carta(mazo, jugador_actual)
                    # turno_completo = True

        if turno_completo:
            turno += 1
            turno_completo = False

        ventana.fill((255, 255, 255))
        dibujar_tablero(ventana, tablero)
        dibujar_mazo(ventana, mazo)
        dibujar_cartas_mano(ventana, jugadores[0], ALTO_VENTANA - 200)
        dibujar_cartas_mano(ventana, jugadores[1], 20)
        dibujar_contador_cartas(ventana, jugadores[0], 10, ALTO_VENTANA - 250)
        dibujar_contador_cartas(ventana, jugadores[1], 10, 60)
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    main()
