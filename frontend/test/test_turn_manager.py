"""Test module for the TurnManager class"""
import unittest

from src.turn_manager.turn_manager import TurnManager
from src.player.player import BasePlayer


class TestCard(unittest.TestCase):

    def correct_initialization(self):
        """
        Testing correct TurnManager Initialization
        """
        turn_manager: TurnManager = TurnManager()

        self.assertEqual(
            turn_manager.n_players,
            0,
            "There shouldnt be any players in the turn manager at this point"
        )
        self.assertEqual(
            turn_manager.idx_turn,
            0,
            "idx_turn shoud be 0 the first time we call idx_turn"
        )
        self.assertEqual(
            turn_manager.idx_acc,
            1,
            "The default value of idx_acc shoud be 1"
        )

    def test_get_and_set_idx_acc(self):
        """
        Here we test if the restrictions set for idx_acc are efective
        """

        turn_manager: TurnManager = TurnManager()

        # We check the firs value to be 1
        self.assertEqual(
            turn_manager.idx_acc,
            1,
            "Default value for  idx_acc should be 1"
        )

        # we can only set idx_acc to 1 or -1
        with self.assertRaises(
            expected_exception=AssertionError,
            msg="Seting idx_acc to 0 is not allowed"
        ):
            turn_manager.idx_acc = 0

        turn_manager.idx_acc = -1

        self.assertEqual(
            turn_manager.idx_acc,
            -1,
            "Changed value of idx_acc should be -1"
        )


if __name__ == "__main__":
    unittest.main()
