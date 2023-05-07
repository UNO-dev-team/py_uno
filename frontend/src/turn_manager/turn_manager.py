"""
TurnManager Module
"""

from typing import List

from src.player.player import BasePlayer


class TurnManager():
    """
    TurnManager handles the turns depending of
    the number of players
    """

    MAX_PLAYERS: int = 4

    def __init__(self) -> None:
        self._idx_turn: int = -1
        self._idx_acc: int = 1
        self._players: List[BasePlayer] = []

    @property
    def n_players(self) -> int:
        """
        The number of players in the TurnManager
        """
        return len(self._players)

    @property
    def idx_turn(self) -> int:
        """
        Increments the turn index by the index
        accumulator and gives us the index of 
        the next turn
        """

        self._idx_turn += self._idx_acc
        return self._idx_turn % self.n_players

    @property
    def idx_acc(self) -> None:
        """
        The value of the actual index accumulator
        """
        return self._idx_acc

    @idx_acc.setter
    def idx_acc(self, new_idx_acc: int) -> None:
        """
        Set idx_acc this value can only be 1 or -1
        """
        assert new_idx_acc == 1 or new_idx_acc == -1
        self._idx_acc = new_idx_acc

    def add_players(self, new_players: List[BasePlayer]) -> None:
        """
        Adds new players to the TurnManager max number of players is 4
        """
        assert self.n_players + len(new_players) <= self.MAX_PLAYERS
        self._players.extend(new_players)

    def next_turn(self) -> BasePlayer:
        """
        This method is used to cicle the players
        returns the BasePlayer for the next turn
        """
        return self._players[self.idx_turn]
