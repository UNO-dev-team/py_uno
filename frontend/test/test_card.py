"""Test module for the Card class"""
import unittest

from src.card.card import Card
from src.utils.consts import Color, Value


class TestCard(unittest.TestCase):
    """All the test suite for the Card Class"""

    def test_creation(self):
        """Testing correct creation"""

        test_card = Card(color=Color.BLUE, value=Value.FIVE)

        self.assertEqual(
            test_card.color.value,
            "azul",
            f"The color of the card should be 'blue' but have: {test_card.color.value} instead"
        )
        self.assertEqual(
            test_card.value.value,
            "5",
            f"The value of the card should be '5' but have: {test_card.value.value} instead"
        )

    def test_comparation(self):
        """Test comparation"""

        blue_5_card = Card(color=Color.BLUE, value=Value.FIVE)
        blue_6_card = Card(color=Color.BLUE, value=Value.SIX)
        red_6_card = Card(color=Color.RED, value=Value.SIX)
        other_red_6_card = Card(color=Color.RED, value=Value.SIX)

        self.assertNotEqual(
            blue_5_card,
            blue_6_card,
            f"This cards are not equal {blue_5_card} != {blue_6_card}"
        )
        self.assertNotEqual(
            blue_6_card,
            red_6_card,
            f"This cards are not equal {blue_5_card} != {blue_6_card}"
        )
        self.assertEqual(
            red_6_card,
            other_red_6_card,
            f"This cards should be equal {red_6_card} == {other_red_6_card}"
        )

    def test_match(self):
        """Testing Match Method"""

        blue_5_card = Card(color=Color.BLUE, value=Value.FIVE)
        blue_6_card = Card(color=Color.BLUE, value=Value.SIX)
        red_6_card = Card(color=Color.RED, value=Value.SIX)
        other_red_6_card = Card(color=Color.RED, value=Value.SIX)

        # No match
        self.assertEqual(
            red_6_card.match(blue_5_card),
            False,
            "red_6 and blue_5 have no match"
        )
        # Match Color
        self.assertEqual(
            blue_5_card.match(blue_6_card),
            True,
            "blue_5 matches the color of blue_6"
        )
        # Match number
        self.assertEqual(
            red_6_card.match(blue_6_card),
            True,
            "red_6 matches the value of blue_6"
        )
        # Match number & value
        self.assertEqual(
            red_6_card.match(other_red_6_card),
            True,
            "2 red_6 cards should match each other"
        )


if __name__ == "__main__":
    unittest.main()
