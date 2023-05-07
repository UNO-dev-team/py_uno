from enum import Enum, auto


ANCHO_VENTANA = 800
ALTO_VENTANA = 800

SCREEN_SIZE = (ANCHO_VENTANA, ALTO_VENTANA)
BOARD_POSITION = (ANCHO_VENTANA // 2 - 20, ALTO_VENTANA // 2 - 150)
DECK_POSITION = (ANCHO_VENTANA // 2 - 170, ALTO_VENTANA // 2 - 60)


class Color(Enum):
    YELLOW = 'amarillo'
    BLUE = 'azul'
    RED = 'rojo'
    GREEN = 'verde'


class Value(Enum):
    ZERO = '0'
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    REVERSED = 'reversa'
    JUMP = 'salto'
    TAKE_TWO = 'tome_dos'


class PlayerType(Enum):
    PLAYER = auto()
    AI_PLAYER = auto()


special_card = (Value.REVERSED, Value.JUMP, Value.TAKE_TWO)
