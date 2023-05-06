"""Test module for the Deck class"""
from typing import List
import unittest

from src.deck.deck import Deck
from src.card.card import Card
from src.utils.consts import Color, Value


class TestCard(unittest.TestCase):
    """All the test suite for the Deck Class"""

    def test_creation(self):
        """Testing correct creation"""
        deck: Deck = Deck()

        self.assertEqual(
            deck.is_empty,
            True,
            "The initial deck should be empty"
        )

    def deck_population(self):
        """Testing the deck contains all uno cards"""
        deck: Deck = Deck()
        deck.init_deck()
        print(len(deck))

    def test_adding_card(self):
        """We should be able to add cards to the deck"""
        deck: Deck = Deck()

        test_card = Card(Color.GREEN, Value.JUMP)

        deck.add(test_card)

        self.assertEqual(
            deck.is_empty,
            False,
            "The deck should have at least 1 card"
        )

        card_in_deck: Card = deck.get(0)
        self.assertEqual(
            card_in_deck,
            test_card,
            "We should have the same card in and out"
        )

    def test_get_all(self):
        """The deck should be empty when we get all the cards"""
        deck: Deck = Deck()

        deck.add(Card(Color.BLUE, Value.FIVE))

        cards_in_deck: List[Card] = deck.get_all()

        self.assertGreater(
            len(cards_in_deck),
            0,
            "We should have the same card in and out"
        )

    def test_give_card_to_other_deck(self):
        """Testing give_card that allow us to give a card to other CardContainer"""
        deck_1: Deck = Deck()
        deck_2: Deck = Deck()

        deck_1.add(Card(Color.YELLOW, Value.NINE))

        deck_1.give_card(deck_2)

        self.assertEqual(
            deck_2.is_empty,
            False,
            "Deck 2 should have the card given by deck 1"
        )

    def test_shuffle(self):
        """Testing shuffle functionality since shos"""
        deck: Deck = Deck()

        # Adding cards in specific order
        deck.add(Card(Color.GREEN, Value.FOUR))
        deck.add(Card(Color.BLUE, Value.SEVEN))
        deck.add(Card(Color.YELLOW, Value.NINE))

        # We get the hole deck
        ordered_cards: List[Card] = deck.get_all()

        # We add again same cards in the same order
        deck.add(Card(Color.GREEN, Value.FOUR))
        deck.add(Card(Color.BLUE, Value.SEVEN))
        deck.add(Card(Color.YELLOW, Value.NINE))

        # but we shuffle it before getting all again
        deck.shuffle()
        shuffled_cards: List[Card] = deck.get_all()

        self.assertNotEqual(
            ordered_cards,
            shuffled_cards,
            "Cards should be in fiferent order"
        )


if __name__ == "__main__":
    unittest.main()
