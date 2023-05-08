from src.game import game
from src.drawer.drawer import Drawer
import pygame


def main():
    pygame.init()
    Drawer.setup()
    screen = Drawer.screen
    game.main(screen)

if __name__ == "__main__":
    main()
