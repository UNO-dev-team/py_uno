
from src.player.player import BasePlayer
from src.utils.consts import PlayerType
from src.player.ai_player import AIPlayer
from src.player.player import Player

class PlayerFactory:
    player_counter = 0

    @classmethod
    def create(cls, type: PlayerType) -> BasePlayer:
        """Crea un objeto de jugador basado en el tipo de jugador proporcionado.

        Args:
            type (PlayerType): El tipo de jugador que se desea crear (HUMAN o AI).

        Returns:
            BasePlayer: Un objeto de jugador (Player o AIPlayer) según el tipo proporcionado.
        """
        if type == PlayerType.PLAYER:
            return cls._create_player()
        elif type == PlayerType.AI_PLAYER:
            return cls._create_ia_player()
        else:
            raise ValueError("Tipo de jugador no soportado.")

    @classmethod
    def _create_player(cls) -> Player:
        """Crea un objeto de jugador (Player).

        Returns:
            Player: Un objeto de jugador.
        """
        cls.player_counter += 1
        return Player() 

    @classmethod
    def _create_ia_player(cls) -> AIPlayer:
        """Crea un objeto de jugador IA (AIPlayer).

        Returns:
            AIPlayer: Un objeto de jugador IA.
        """
        cls.player_counter += 1
        return AIPlayer()  