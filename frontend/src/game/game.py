from src.card.card import Card
from src.drawer.drawer import Drawer
from src.utils.consts import ALTO_VENTANA, ANCHO_VENTANA, Value
from src.board.board import dibujar_tablero, dibujar_carta_moviendose, Board
from src.player.player import Jugador, dibujar_info_jugadores
from src.deck.deck import Deck
from src.hand.hand import dibujar_cartas_mano
from src.screen.screen import pantalla_inicio
from src.utils.position import Position
from src.utils import consts
from pygame.image import load

from pygame.draw import circle
from pygame import Surface

import pygame


def main(ventana: Surface):
    reloj = pygame.time.Clock()
    imagen_fondo = load('images/Table_2.png')
    ventana.blit(imagen_fondo, (0, 0))  
    num_IA = pantalla_inicio(ventana)
    deck = Deck()
    deck.init_deck()
    deck.shuffle()
    jugadores = [Jugador("Jugador 1")]

    for i in range(num_IA):
        jugadores.append(Jugador(f"IA {i + 1}"))
    tablero = Board()

    for jugador in jugadores:
        deck.give_card(jugador.hand, 7)
        # jugador.hand._cards = deck.give_card(n=7)

    tablero.add(deck.get(-1))

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
            for card in jugador_actual.hand.get_all():
                if card.value == Value.TAKE_TWO:
                    tiene_tome_dos = True
                    break
            if not tiene_tome_dos:
                for _ in range(acumular_tome_dos):
                    deck.give_card(jugador_actual.hand)
                acumular_tome_dos = 0
                turno += direccion
                continue

        if turno % len(jugadores) == 0:  # Jugador 1 (humano)
            x, y = pygame.mouse.get_pos()
            x_offset = 50
            espaciado = 30 if len(
                jugador_actual.hand) <= 20 else 800 // len(jugador_actual.hand)

            for indice_carta, carta in enumerate(jugador_actual.hand.iterate()):
                if indice_carta < len(jugador_actual.hand) - 1:
                    carta_rect = pygame.Rect(
                        x_offset + espaciado * indice_carta, ALTO_VENTANA - 200, espaciado, carta.img.get_height())
                else:
                    carta_rect = carta.img.get_rect(
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
                        if (ANCHO_VENTANA // 2 - 160) < x < (ANCHO_VENTANA // 2 - 50) and (ALTO_VENTANA // 2 - 40) < y < (ALTO_VENTANA // 2 + 110):
                            deck.give_card(jugador_actual.hand)
                            # turno_completo = True
                        # Jugar carta
                        for indice_carta, carta in reversed(list(enumerate(jugador_actual.hand.iterate()))):
                            if indice_carta < len(jugador_actual.hand) - 1:
                                carta_rect = pygame.Rect(
                                    x_offset + espaciado * indice_carta, ALTO_VENTANA - 200, espaciado, carta.img.get_height())
                            else:
                                carta_rect = carta.img.get_rect(
                                    topleft=(x_offset + espaciado * indice_carta, ALTO_VENTANA - 200))

                            if carta_rect.collidepoint(x, y) and es_movimiento_valido(carta, tablero.get(-1)):
                                start_card = Position(
                                    x - 30, ALTO_VENTANA - 220)
                                end_card = Position(
                                    ANCHO_VENTANA // 2 - 20, ALTO_VENTANA // 2 - 150)
                                Drawer.draw_moving_card(
                                    carta, start_card, end_card)

                                tablero.add(
                                    jugador_actual.hand.pop(indice_carta))
                                # tablero.add(
                                #     jugador_actual.mano.quitar_carta(indice_carta), jugador_actual.nombre)
                                turno_completo = True
                                break

        # Jugador 2 (IA simple)
        else:
            if not turno_completo:
                pygame.time.delay(1000)
                carta_valida_encontrada = False

                for indice_carta, carta in enumerate(jugador_actual.hand.iterate()):
                    if es_movimiento_valido(carta, tablero.get(-1)):
                        if turno % len(jugadores) == 1:
                            x_inicial, y_inicial = 60, 40
                        elif turno % len(jugadores) == 2:
                            x_inicial, y_inicial = ANCHO_VENTANA - 100, 40
                        elif turno % len(jugadores) == 3:
                            x_inicial, y_inicial = ANCHO_VENTANA - 100, ALTO_VENTANA - 220
                        dibujar_carta_moviendose(ventana, carta, [x_inicial, y_inicial], [
                            ANCHO_VENTANA // 2 - 20, ALTO_VENTANA // 2], 20)
                        tablero.add(jugador_actual.hand.pop(indice_carta))
                        # tablero.add(
                        #     jugador_actual.mano.quitar_carta(indice_carta), jugador_actual.nombre)
                        turno_completo = True
                        carta_valida_encontrada = True
                        break

                if not carta_valida_encontrada:
                    deck.give_card(jugador_actual.hand)

        # Acciones comunes para todos los jugadores (salto, tome_dos, reversa)
        if turno_completo:
            card: Card = tablero.get(-1)
            if card.value == Value.JUMP:
                turno += 2 * direccion
            elif card.value == Value.TAKE_TWO:
                acumular_tome_dos += 2
                turno += direccion
            elif card.value == Value.REVERSED:
                direccion *= -1
                turno += direccion
            else:
                turno += direccion

            turno_completo = False

        ventana.fill((255, 255, 255))
        Drawer.draw_board(tablero)
        Drawer.draw_deck(deck)
        # Dibuja las cartas de los jugadores en diferentes posiciones según su número
        # TODO: DRAW ALL HANDS
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
            f"Turno de {jugadores[turno % len(jugadores)].name}", 1, (0, 0, 0))
        ventana.blit(texto_turno, (ANCHO_VENTANA // 2 -
                                   texto_turno.get_width() // 2, ALTO_VENTANA // 2 - 100))
        pygame.display.flip()
        reloj.tick(20)

    pygame.quit()

# Función para verificar si un movimiento es válido


def es_movimiento_valido(carta: Card, ultima_carta: Card):
    return carta.color == ultima_carta.color or carta.value == ultima_carta.value


def dibujar_indicador_turno(ventana, jugador_actual, posiciones):
    radio = 10
    color = (255, 0, 0)
    circle(ventana, color, posiciones[jugador_actual], radio)


def comer_carta(mazo, jugador: Jugador):
    if len(mazo.cartas) == 0:
        return

    carta = mazo.cartas.pop()
    print(f"comio carta el jugador: {jugador.name}")
    # jugador.mano.agregar_carta(carta)
    jugador.hand.add(carta)

    # Añade la animación de tomar cartas
    x_start, y_start = consts.DECK_POSITION
    start = Position(x_start, y_start)

    if jugador.name == "Jugador 1":
        x_end, y_end = (
            50 + 30 * (len(jugador.hand) - 1), ALTO_VENTANA - 200)
    elif jugador.name == "IA 1":
        x_end, y_end = (50 + 30 * (len(jugador.hand) - 1), 10)
    elif jugador.name == "IA 2":
        x_end, y_end = (ANCHO_VENTANA - 100, 10)
    elif jugador.name == "IA 3":
        x_end, y_end = (ANCHO_VENTANA - 100, ALTO_VENTANA - 100)

    end = Position(x_end, y_end)

    Drawer.draw_moving_card(carta, start, end)
