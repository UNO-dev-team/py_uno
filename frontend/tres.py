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


def dibujar_cartas_mano(ventana, jugador, x_offset, y_offset, carta_resaltada=None):
    espaciado = 30 if len(
        jugador.mano.cartas) <= 20 else 800 // len(jugador.mano.cartas)

    for indice_carta, carta in enumerate(jugador.mano.cartas):
        x_pos = x_offset + espaciado * indice_carta
        if carta_resaltada is not None and indice_carta == carta_resaltada:
            imagen_resaltada = pygame.transform.scale(carta.imagen, (int(
                carta.imagen.get_width() * 1.2), int(carta.imagen.get_height() * 1.2)))
            ventana.blit(imagen_resaltada, (x_pos -
                         int(carta.imagen.get_width() * 0.1), y_offset - 50))
        else:
            ventana.blit(carta.imagen, (x_pos, y_offset))


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


# Función para verificar si un movimiento es válido
def es_movimiento_valido(carta, ultima_carta):
    return carta.color == ultima_carta.color or carta.valor == ultima_carta.valor


def dibujar_indicador_turno(ventana, jugador_actual, posiciones):
    radio = 10
    color = (255, 0, 0)
    pygame.draw.circle(ventana, color, posiciones[jugador_actual], radio)


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

    def agregar_carta(self, carta, jugador):
        print()
        print(f"{jugador} jugo la carta: {carta.color} - {carta.valor}")
        self.cartas_jugadas.append(carta)

    def obtener_ultima_carta(self):
        return self.cartas_jugadas[-1] if self.cartas_jugadas else None


def dibujar_contador_cartas(ventana, jugador, x_offset, y_offset):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(str(len(jugador.mano.cartas)), 1, (0, 0, 0))
    ventana.blit(texto, (x_offset, y_offset))


def dibujar_carta_moviendose(ventana, carta, pos_inicial, pos_final, pasos):
    paso_actual = 0
    pos_actual = pos_inicial

    while paso_actual <= pasos:
        pos_actual[0] += (pos_final[0] - pos_inicial[0]) / pasos
        pos_actual[1] += (pos_final[1] - pos_inicial[1]) / pasos

        ventana.blit(carta.imagen, pos_actual)
        pygame.display.flip()
        pygame.time.delay(10)

        paso_actual += 1


pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Uno")


def pantalla_inicio():
    fuente = pygame.font.Font(None, 36)
    texto1 = fuente.render("Selecciona el número de IA (1-3)", 1, (0, 0, 0))
    opcion1 = fuente.render("1 IA", 1, (0, 0, 0))
    opcion2 = fuente.render("2 IA", 1, (0, 0, 0))
    opcion3 = fuente.render("3 IA", 1, (0, 0, 0))

    inicio = False
    num_IA = 0
    while not inicio:
        ventana.fill((255, 255, 255))
        ventana.blit(texto1, (ANCHO_VENTANA // 2 -
                     100, ALTO_VENTANA // 2 - 100))
        ventana.blit(opcion1, (ANCHO_VENTANA // 2 - 100, ALTO_VENTANA // 2))
        ventana.blit(opcion2, (ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
        ventana.blit(opcion3, (ANCHO_VENTANA // 2 + 100,
                     ALTO_VENTANA // 2))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                inicio = True

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = evento.pos

                if (ANCHO_VENTANA // 2 - 100) < x < (ANCHO_VENTANA // 2 - 10) and (ALTO_VENTANA // 2) < y < (ALTO_VENTANA // 2 + 50):
                    num_IA = 1
                    inicio = True
                elif (ANCHO_VENTANA // 2) < x < (ANCHO_VENTANA // 2 + 90) and (ALTO_VENTANA // 2) < y < (ALTO_VENTANA // 2 + 50):
                    num_IA = 2
                    inicio = True
                elif (ANCHO_VENTANA // 2 + 100) < x < (ANCHO_VENTANA // 2 + 190) and (ALTO_VENTANA // 2) < y < (ALTO_VENTANA // 2 + 50):
                    num_IA = 3  # Asignar valor de 3 para la opción 3
                    inicio = True

        pygame.display.flip()

    return num_IA


def dibujar_info_jugadores(ventana, jugadores):
    fuente = pygame.font.Font(None, 24)
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


def main():
    reloj = pygame.time.Clock()
    num_IA = pantalla_inicio()
    mazo = generar_mazo()
    mazo.barajar()
    jugadores = [Jugador("Jugador 1")]
    for i in range(num_IA):
        jugadores.append(Jugador(f"IA {i + 1}"))
    tablero = Tablero()
    for jugador in jugadores:
        mazo.repartir(jugador.mano, 7)
    tablero.agregar_carta(mazo.cartas.pop(), "Tablero")
    turno = 0
    juego_terminado = False
    turno_completo = False
    acumular_tome_dos = 0
    direccion = 1
    posiciones_turno = [
        (20, ALTO_VENTANA - 240),
        (20, 40),
        (ANCHO_VENTANA - 220, 40),
        (ANCHO_VENTANA - 220, ALTO_VENTANA - 240)
    ]

    while not juego_terminado:
        jugador_actual = jugadores[turno % len(jugadores)]
        carta_resaltada = None

        # Comprobar si el jugador actual debe comer cartas acumuladas y no tiene un "tome_dos" en su mano
        if acumular_tome_dos > 0:
            tiene_tome_dos = False
            for c in jugador_actual.mano.cartas:
                if c.valor == "tome_dos":
                    tiene_tome_dos = True
                    break
            if not tiene_tome_dos:
                for _ in range(acumular_tome_dos):
                    comer_carta(mazo, jugador_actual, ventana)
                acumular_tome_dos = 0
                turno += direccion
                continue

        if turno % len(jugadores) == 0:  # Jugador 1 (humano)
            x, y = pygame.mouse.get_pos()
            x_offset = 50
            espaciado = 30 if len(
                jugador_actual.mano.cartas) <= 20 else 800 // len(jugador_actual.mano.cartas)

            for indice_carta, carta in enumerate(jugador_actual.mano.cartas):
                if indice_carta < len(jugador_actual.mano.cartas) - 1:
                    carta_rect = pygame.Rect(
                        x_offset + espaciado * indice_carta, ALTO_VENTANA - 200, espaciado, carta.imagen.get_height())
                else:
                    carta_rect = carta.imagen.get_rect(
                        topleft=(x_offset + espaciado * indice_carta, ALTO_VENTANA - 200))

                if carta_rect.collidepoint(x, y):
                    carta_resaltada = indice_carta
                    break

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    juego_terminado = True

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if not turno_completo:
                        x, y = evento.pos
                        x_offset = 50

                        # Comer carta
                        if (ANCHO_VENTANA // 2 - 120) < x < (ANCHO_VENTANA // 2 - 20) and (ALTO_VENTANA // 2 - 70) < y < (ALTO_VENTANA // 2 + 30):
                            comer_carta(mazo, jugador_actual, ventana)
                            # turno_completo = True
                        # Jugar carta
                        for indice_carta, carta in reversed(list(enumerate(jugador_actual.mano.cartas))):
                            if indice_carta < len(jugador_actual.mano.cartas) - 1:
                                carta_rect = pygame.Rect(
                                    x_offset + espaciado * indice_carta, ALTO_VENTANA - 200, espaciado, carta.imagen.get_height())
                            else:
                                carta_rect = carta.imagen.get_rect(
                                    topleft=(x_offset + espaciado * indice_carta, ALTO_VENTANA - 200))

                            if carta_rect.collidepoint(x, y) and es_movimiento_valido(carta, tablero.obtener_ultima_carta()):
                                dibujar_carta_moviendose(ventana, carta, [x - 30, ALTO_VENTANA - 220], [
                                                         ANCHO_VENTANA // 2 - 20, ALTO_VENTANA // 2 - 150], 20)
                                # animacion_jugar_carta(ventana, carta, (x - 30, ALTO_VENTANA - 220),
                                #                       (ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 - 50), mazo, tablero, jugadores)
                                50 + 30 * (len(jugador.mano.cartas) -
                                           1), ALTO_VENTANA - 200
                                tablero.agregar_carta(
                                    jugador_actual.mano.quitar_carta(indice_carta), jugador_actual.nombre)
                                turno_completo = True
                                break

        # Jugador 2 (IA simple)
        else:
            if not turno_completo:
                pygame.time.delay(1000)
                carta_valida_encontrada = False

                for indice_carta, carta in enumerate(jugador_actual.mano.cartas):
                    if es_movimiento_valido(carta, tablero.obtener_ultima_carta()):
                        if turno % len(jugadores) == 1:
                            x_inicial, y_inicial = 60, 40
                        elif turno % len(jugadores) == 2:
                            x_inicial, y_inicial = ANCHO_VENTANA - 100, 40
                        elif turno % len(jugadores) == 3:
                            x_inicial, y_inicial = ANCHO_VENTANA - 100, ALTO_VENTANA - 220
                        dibujar_carta_moviendose(ventana, carta, [x_inicial, y_inicial], [
                            ANCHO_VENTANA // 2 - 20, ALTO_VENTANA // 2], 20)
                        tablero.agregar_carta(
                            jugador_actual.mano.quitar_carta(indice_carta), jugador_actual.nombre)
                        turno_completo = True
                        carta_valida_encontrada = True
                        break

                if not carta_valida_encontrada:
                    comer_carta(mazo, jugador_actual, ventana)

        # Acciones comunes para todos los jugadores (salto, tome_dos, reversa)
        if turno_completo:
            carta = tablero.obtener_ultima_carta()
            if carta.valor == "salto":
                turno += 2 * direccion
            elif carta.valor == "tome_dos":
                acumular_tome_dos += 2
                turno += direccion
            elif carta.valor == "reversa":
                direccion *= -1
                turno += direccion
            else:
                turno += direccion

            turno_completo = False

        ventana.fill((255, 255, 255))
        dibujar_tablero(ventana, tablero)
        dibujar_mazo(ventana, mazo)
        # Dibuja las cartas de los jugadores en diferentes posiciones según su número
        dibujar_cartas_mano(
            ventana, jugadores[0], 50, ALTO_VENTANA - 200, carta_resaltada)
        if num_IA == 1:
            dibujar_cartas_mano(ventana, jugadores[1], 50, 50)
        elif num_IA == 2:
            dibujar_cartas_mano(ventana, jugadores[2], ANCHO_VENTANA - 200, 50)
            dibujar_cartas_mano(ventana, jugadores[1], 50, 50)
        elif num_IA == 3:
            dibujar_cartas_mano(ventana, jugadores[2], ANCHO_VENTANA - 200, 50)
            dibujar_cartas_mano(ventana, jugadores[1], 50, 50)
            dibujar_cartas_mano(
                ventana, jugadores[3], ANCHO_VENTANA - 200, ALTO_VENTANA - 200,)

        dibujar_info_jugadores(ventana, jugadores)
        dibujar_indicador_turno(ventana, turno %
                                len(jugadores), posiciones_turno)
        fuente_turno = pygame.font.Font(None, 30)
        texto_turno = fuente_turno.render(
            f"Turno de {jugadores[turno % len(jugadores)].nombre}", 1, (0, 0, 0))
        ventana.blit(texto_turno, (ANCHO_VENTANA // 2 -
                                   texto_turno.get_width() // 2, ALTO_VENTANA // 2 - 100))
        pygame.display.flip()
        reloj.tick(20)

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    main()
