from pygame.image import load
from pygame import Surface
from pygame.transform import scale


def load_image(nombre):
    carta = load(f"images/{nombre}.png")
    if nombre == "mazo":
        return carta
    width, height = carta.get_size()
    resized_card = scale(carta, (width // 3, height // 3))
    # scale(carta, )
    return resized_card
