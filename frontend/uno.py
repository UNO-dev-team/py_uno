from src.game import game
from src.utils.consts import ALTO_VENTANA, ANCHO_VENTANA
import pygame


pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Uno")


if __name__ == "__main__":
    game.main(ventana)
