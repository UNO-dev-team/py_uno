from pygame.transform import scale


class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def quitar_carta(self, indice):
        return self.cartas.pop(indice)


def dibujar_cartas_mano(ventana, jugador, x_offset, y_offset, carta_resaltada=None):
    espaciado = 30 if len(
        jugador.mano.cartas) <= 20 else 800 // len(jugador.mano.cartas)

    for indice_carta, carta in enumerate(jugador.mano.cartas):
        x_pos = x_offset + espaciado * indice_carta
        if carta_resaltada is not None and indice_carta == carta_resaltada:
            imagen_resaltada = scale(carta.img, (int(
                carta.img.get_width() * 1.2), int(carta.img.get_height() * 1.2)))
            ventana.blit(imagen_resaltada, (x_pos -
                         int(carta.img.get_width() * 0.1), y_offset - 50))
        else:
            ventana.blit(carta.img, (x_pos, y_offset))
