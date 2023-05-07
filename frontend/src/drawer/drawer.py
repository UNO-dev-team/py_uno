from pygame import Surface
from pygame.display import set_mode, set_caption, flip
from pygame.transform import scale
from pygame.font import Font
from pygame import time

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
    _screen: Surface

    @classmethod
    @property
    def screen(cls):
        return cls._screen

    @classmethod
    def setup(cls):
        cls._screen = set_mode(SCREEN_SIZE)
        set_caption('UNO!')

    @classmethod
    def draw_board(cls, board: Board):
        last_card = board.get_all()

        if last_card is not None:
            cls.screen.blit(last_card.img, BOARD_POS)
    
    @classmethod
    def draw_deck(cls, deck: Deck):
        top_card = load_image('mazo')
        weidth, height = top_card.get_size()

        img = scale(top_card,
                    (weidth // 3, height // 3))
        
        deck_shape = img.get_rect()
        deck_shape.center = (weidth // 2 - 120, height // 2 + 40)
        cls._screen.blit(img, deck_shape)

        font = Font(None, 36)
        deck_length = str(len(deck))
        text = font.render(deck_length, 1, WHITE)
        cls._screen.blit(text, (ANCHO_VENTANA // 2 - 115, ALTO_VENTANA // 2 - 20))
    
    @classmethod
    def draw_moving_card(cls, c: Card, start: Position, end: Position, steps: int = 20):
        actual = Position(0, 0)

        for _ in range(steps):
            actual.x += end.x - start.x // steps
            actual.y += end.y - start.y // steps

            actual_tuple = actual.tuple()
            cls.screen.blit(c.img, actual_tuple)
            flip()
            time.delay(MOVING_CARD_DELAY)
    
    @classmethod
    def draw_hand(cls, h: Hand, offset: Position, c: Card = None):
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
                            (x_pos -int(card.img.get_width() * 0.1), 
                             offset.y - 50))

    @classmethod
    def draw_players(cls, players: list[BasePlayer]):
        font = Font(None, 24)
        
        for player in players:
            name = f'{player.name}: {len(player._hand)} cards'
            text = font.render(name, 1, BLACK)
            cls.screen.blit(text, player.position)
