from pygame.image import load


def cargar_imagen(nombre):
    return load(f"images/{nombre}.png")
