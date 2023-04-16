class Carta:
    def __init__(self, color, valor, imagen):
        self.color = color
        self.valor = valor
        self.imagen = imagen

    def __str__(self):
        return f"{self.color} {self.valor}"
