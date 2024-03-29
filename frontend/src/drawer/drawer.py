from pygame import Surface
from pygame.display import set_mode, set_caption, flip
from pygame.transform import scale
from pygame.font import Font
from pygame import time
from pygame.image import load
from src.utils.images import load_image
from src.board.board import Board
from src.hand.hand import Hand
from src.deck.deck import Deck
from src.card.card import Card
from src.player.player import BasePlayer
from src.utils.position import Position
from src.utils.consts import SCREEN_SIZE, ANCHO_VENTANA, ALTO_VENTANA
from src.utils.color import WHITE, BLACK


BOARD_POS = (ANCHO_VENTANA // 2 - 50, ALTO_VENTANA // 2 - 50)
MOVING_CARD_DELAY = 10


class Drawer:
    """Una clase que se encarga de dibujar elementos de juego en la ventana de Pygame.

    La clase Drawer es un conjunto de métodos de clase para dibujar el tablero, la baraja, las cartas en movimiento, las manos y los jugadores en la ventana de Pygame. Se utiliza como una utilidad para simplificar el proceso de dibujo en el juego.
    """
    _screen: Surface

    @classmethod
    @property
    def screen(cls):
        return cls._screen

    @classmethod
    def setup(cls):
        """Configura la ventana de Pygame y establece el título de la ventana.

        Returns:
            None
        """
        cls._screen = set_mode(SCREEN_SIZE)

        set_caption('UNO!')

    @classmethod
    def draw_board(cls, board: Board):
        """Dibuja el tablero en la ventana de Pygame.

        Args:
            board (Board): El objeto Tablero que se va a dibujar.

        Returns:
            None
        """
        list_cards = board.get_all()
        if list_cards is not None:
            card = board.get(-1)
            cls.screen.blit(card.img, BOARD_POS)

    @classmethod
    def draw_deck(cls, deck: Deck):
        """Dibuja la baraja en la ventana de Pygame.

        Args:
            deck (Deck): El objeto Deck que se va a dibujar.

        Returns:
            None
        """
        top_card = load_image('mazo')
        weidth, height = top_card.get_size()

        img = scale(top_card,
                    (weidth // 3, height // 3))

        deck_shape = img.get_rect()
        deck_shape.center = (weidth // 2 + 100, height // 2 + 160)
        cls._screen.blit(img, deck_shape)

        font = Font(None, 36)
        deck_length = str(len(deck))
        text = font.render(deck_length, 1, WHITE)
        cls._screen.blit(text, (ANCHO_VENTANA // 2 -
                         115, ALTO_VENTANA // 2 - 20))

    @classmethod
    def draw_moving_card(cls, c: Card, start: Position, end: Position, steps: int = 20):
        """Dibuja una carta moviéndose desde una posición inicial hasta una posición final en la ventana de Pygame.

        Args:
            c (Card): La carta que se va a mover.
            start (Position): La posición inicial de la carta.
            end (Position): La posición final de la carta.
            steps (int, optional): El número de pasos en los que se debe completar el movimiento. Por defecto es 20.

        Returns:
            None
        """
        actual = Position(start.x, start.y)

        for _ in range(steps):
            actual.x += (end.x - start.x) // steps
            actual.y += (end.y - start.y) // steps

            actual_tuple = actual.tuple()
            cls.screen.blit(c.img, actual_tuple)
            flip()
            time.delay(MOVING_CARD_DELAY)


    @classmethod
    def draw_hand(cls, h: Hand, offset: Position, c: Card = None):
        """Dibuja las cartas en la mano de un jugador en la ventana de Pygame.

        Args:
            h (Hand): La mano del jugador que se va a dibujar.
            offset (Position): Desplazamiento en el eje X y Y para las cartas en la ventana.
            c (Card, optional): La carta que se va a resaltar. Si es None, ninguna carta será resaltada. Por defecto es None.

        Returns:
            None
        """
        len_hand = len(h)
        space = 30 if len_hand <= 20 else 800 // len_hand
        cards = h.get_all()

        for idx, card in enumerate(cards):
            x_pos = offset.x + space * idx

            if c is None:
                cls.screen.blit(card.img, (x_pos, offset.y))
                return

            special_card_img = scale(card.img,
                                     (int(card.img.get_width() * 1.2),
                                      int(card.img.get_height() * 1.2)))

            cls.screen.blit(special_card_img,
                            (x_pos - int(card.img.get_width() * 0.1),
                             offset.y - 50))

    @classmethod
    def draw_players(cls, players: list[BasePlayer]):
        """Dibuja los nombres y el número de cartas de los jugadores en la ventana de Pygame.

        Args:
            players (list[BasePlayer]): Una lista de objetos de jugadores que se van a dibujar.

        Returns:
            None
        """
        font = Font(None, 24)

        for player in players:
            name = f'{player.name}: {len(player._hand)} cards'
            text = font.render(name, 1, BLACK)
            cls.screen.blit(text, player.position)
