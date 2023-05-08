from pygame.image import load
from pygame import Surface
from pygame.transform import scale


def load_image(nombre):
    """
    Carga una imagen desde el directorio "images" y la redimensiona si no es la imagen del mazo.

    La función carga una imagen con el nombre especificado en el argumento y la redimensiona a 1/3 de
    su tamaño original si no es la imagen del mazo. Si la imagen es del mazo, la retorna sin redimensionar.

    Args:
        nombre (str): Nombre del archivo de la imagen sin la extensión .png.

    Returns:
        pygame.Surface: Objeto Surface de Pygame que contiene la imagen cargada y redimensionada si es necesario.
    """
    carta = load(f"images/{nombre}.png")
    if nombre == "mazo":
        return carta
    width, height = carta.get_size()
    resized_card = scale(carta, (width // 3, height // 3))
    return resized_card

