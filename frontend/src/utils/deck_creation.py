from src.utils.consts import Color, Value


def all_card_colors() -> list[Color]:
    """Returns a list with the colors we want to have in the deck"""
    return list(Color)


def all_card_values() -> list[Value]:
    """Returns a list with all the cards values we want in the deck"""
    return list(Value)
