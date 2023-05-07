from src.card.card import Card
from src.drawer.drawer import Drawer
from src.utils.consts import ALTO_VENTANA, ANCHO_VENTANA, Value
from src.board.board import dibujar_tablero, dibujar_carta_moviendose, Board
from src.player.player import Jugador, dibujar_info_jugadores, comer_carta
from src.deck.deck import Deck
from src.hand.hand import dibujar_cartas_mano
from src.screen.screen import pantalla_inicio
from src.utils.position import Position

from pygame.draw import circle
from pygame import Surface

import pygame


def main(ventana: Surface):
    reloj = pygame.time.Clock()
    num_IA = pantalla_inicio(ventana)
    deck = Deck()
    deck.init_deck()
    jugadores = [Jugador("Jugador 1")]

    for i in range(num_IA):
        jugadores.append(Jugador(f"IA {i + 1}"))
    tablero = Board()

    for jugador in jugadores:
        jugador.mano.cartas = deck.give_card(n = 7)

    tablero.agregar_carta(deck.get(-1), "Tablero")

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
            for card in jugador_actual.mano.cartas:
                if card.value == Value.TAKE_TWO:
                    tiene_tome_dos = True
                    break
            if not tiene_tome_dos:
                for _ in range(acumular_tome_dos):
                    comer_carta(mazo, jugador_actual)
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
                        if (ANCHO_VENTANA // 2 - 120) < x < (ANCHO_VENTANA // 2 - 20) and (ALTO_VENTANA // 2 - 70) < y < (ALTO_VENTANA // 2 + 30):
                            comer_carta(mazo, jugador_actual)
                            # turno_completo = True
                        # Jugar carta
                        for indice_carta, carta in reversed(list(enumerate(jugador_actual.mano.cartas))):
                            if indice_carta < len(jugador_actual.mano.cartas) - 1:
                                carta_rect = pygame.Rect(
                                    x_offset + espaciado * indice_carta, ALTO_VENTANA - 200, espaciado, carta.img.get_height())
                            else:
                                carta_rect = carta.img.get_rect(
                                    topleft=(x_offset + espaciado * indice_carta, ALTO_VENTANA - 200))

                            if carta_rect.collidepoint(x, y) and es_movimiento_valido(carta, tablero.obtener_ultima_carta()):
                                start_card = Position(x - 30, ALTO_VENTANA - 220)
                                end_card = Position(ANCHO_VENTANA // 2 - 20, ALTO_VENTANA // 2 - 150)
                                Drawer.draw_moving_card(carta, start_card, end_card)

                                tablero.add(
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
                        tablero.add(
                            jugador_actual.mano.quitar_carta(indice_carta), jugador_actual.nombre)
                        turno_completo = True
                        carta_valida_encontrada = True
                        break

                if not carta_valida_encontrada:
                    comer_carta(mazo, jugador_actual)

        # Acciones comunes para todos los jugadores (salto, tome_dos, reversa)
        if turno_completo:
            card: Card = tablero.obtener_ultima_carta()
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
            f"Turno de {jugadores[turno % len(jugadores)].nombre}", 1, (0, 0, 0))
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
