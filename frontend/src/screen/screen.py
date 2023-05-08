from pygame.font import Font
from src.utils.consts import ALTO_VENTANA, ANCHO_VENTANA
from pygame import Surface, QUIT, MOUSEBUTTONDOWN
from pygame.event import get
from pygame.display import flip


def pantalla_inicio(screen: Surface):
    """
    Presenta una pantalla de inicio al usuario para seleccionar el número de IA (Inteligencia Artificial) en el juego.
    
    La función permite al usuario elegir entre 1, 2 o 3 IA. La pantalla muestra las opciones y espera a que el usuario haga clic en una de ellas.
    Luego, devuelve el número de IA seleccionado por el usuario.

    Args:
        screen (Surface): La ventana de Pygame donde se mostrarán las opciones de IA.

    Returns:
        int: El número de IA seleccionado por el usuario (1, 2 o 3).
    """
    fuente = Font(None, 36)
    texto1 = fuente.render("Selecciona el número de IA (1-3)", 1, (0, 0, 0))
    opcion1 = fuente.render("1 IA", 1, (0, 0, 0))
    opcion2 = fuente.render("2 IA", 1, (0, 0, 0))
    opcion3 = fuente.render("3 IA", 1, (0, 0, 0))

    inicio = False
    num_IA = 0
    while not inicio:
        screen.fill((255, 255, 255))
        screen.blit(texto1, (ANCHO_VENTANA // 2 -
                     100, ALTO_VENTANA // 2 - 100))
        screen.blit(opcion1, (ANCHO_VENTANA // 2 - 100, ALTO_VENTANA // 2))
        screen.blit(opcion2, (ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
        screen.blit(opcion3, (ANCHO_VENTANA // 2 + 100,
                     ALTO_VENTANA // 2))

        for evento in get():
            if evento.type == QUIT:
                inicio = True

            if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
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

        flip()

    return num_IA