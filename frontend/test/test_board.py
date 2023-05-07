"""Test module for the Board class"""
import unittest

from src.card.card import Card
from src.utils.consts import Color, Value
from src.card_container.card_container import CardContainer
from src.board.board import Board


class TestBoard(unittest.TestCase):
    """Test suite for the Board class"""

    def setUp(self):
        """Setup method for the test suite"""
        self.board = Board()
        self.blue_5_card = Card(color=Color.BLUE, value=Value.FIVE)
        self.blue_6_card = Card(color=Color.BLUE, value=Value.SIX)
        self.red_6_card = Card(color=Color.RED, value=Value.SIX)

    def test_add_valid_card(self):
        """Test adding a valid card"""

        self.board.add(self.blue_5_card)
        self.assertEqual(
            self.board.get(0),
            self.blue_5_card,
            "The blue_5_card should be in the board"
        )
        self.board.add(self.blue_6_card)
        self.assertEqual(
            self.board.get(1),
            self.blue_6_card,
            "The blue_6_card should be in the board"
        )

    def test_add_invalid_card(self):
        """Test adding an invalid card"""

        self.board.add(self.blue_5_card)
        with self.assertRaises(RuntimeError):
            self.board.add(self.red_6_card)

    def test_get(self):
        """Test getting a card by index"""

        self.board.add(self.blue_5_card)
        self.board.add(self.blue_6_card)
        self.assertEqual(
            self.board.get(0),
            self.blue_5_card,
            "The blue_5_card should be in the board"
        )
        self.assertEqual(
            self.board.get(1),
            self.blue_6_card,
            "The blue_6_card should be in the board"
        )

    def test_delete(self):
        """Test deleting the last card"""

        self.board.add(self.blue_5_card)
        self.board.add(self.blue_6_card)
        deleted_card = self.board.delete()

        self.assertEqual(
            deleted_card,
            self.blue_6_card,
            "The deleted card should be the blue_6_card"
        )
        self.assertEqual(
            self.board.get(0),
            self.blue_5_card,
            "The blue_5_card should still be in the board"
        )


if __name__ == "__main__":
    unittest.main()
