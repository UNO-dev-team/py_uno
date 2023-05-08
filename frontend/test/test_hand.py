"""Test module for the Card class"""
import unittest

from src.card.card import Card
from src.utils.consts import Color, Value
from src.hand.hand import Hand


class TestHand(unittest.TestCase):
    """All the test suite for the Card Hand."""

    def test_empty(self):
        """Testing correct creation"""

        h = Hand()

        self.assertTrue(h.is_empty, "Hand must be empty")

    def test_add(self):
        h = Hand()
        c = Card(Color.BLUE, Value.EIGHT)
        h.add(c)

        self.assertFalse(h.is_empty, "Hand has a Card")
        cards = h.get_all()
        test = [c]
        self.assertEqual(test, cards, "Hand must have all cards.")

    def test_add_multiple_cards(self):
        h = Hand()
        cards = [Card(Color.BLUE, Value.EIGHT), Card(Color.GREEN, Value.FIVE)]
        h.add(cards)

        self.assertFalse(h.is_empty, "Hand has multiple cards")
        cards_test = h.get_all()
        self.assertNotEqual(cards, cards_test, "Get all must delivers a copy.")