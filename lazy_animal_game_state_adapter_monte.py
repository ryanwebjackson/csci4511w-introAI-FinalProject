from typing import Tuple

from games4e import GameState  # type: ignore
from lazy_animal_environment import LazyAnimalEnvironment
from lazy_animal_state import LazyAnimalState


class LazyAnimalGameStateAdapterMonteCarlo:
    def __init__(self, game_state: GameState, lazy_animal_state: LazyAnimalState):
        self.game_state = game_state
        self.lazy_animal_state = lazy_animal_state
        self.children: dict = {}
        self.actions = None

    # region Object Overrides

    def __repr__(self):
        return self.game_state.__repr__()

    def __str__(self):
        return self.game_state.__str__()

    def __eq__(self, other):
        return self.game_state == other.game_state

    def __hash__(self):
        return self.game_state.__hash__()

    def __ne__(self, other):
        return not self.__eq__(other)

    # endregion

    def adapt_gamestate_to_domainstate(self) -> GameState:
        print("Should update data based on GameState and LazyAnimalState - stubbed out for now.")
        return self.game_state

    # TODO: Implement and use the below methods for calculations, before returning a new GameState.

    def get_actions(self):
        raise NotImplementedError("get_legal_actions() not implemented")

    def get_parent(self):
        raise NotImplementedError("get_parent() not implemented")

    def get_children(self):
        raise NotImplementedError("get_children() not implemented")

    def get_state(self):
        raise NotImplementedError("get_state() not implemented")

    @staticmethod
    def get_initial_monte_game_state(
        to_move: str,
        animal_location: Tuple[int, int],
        human_location: Tuple[int, int],
        environment: LazyAnimalEnvironment
    ) -> GameState:

        moves: list = []
        if to_move == "animal":
            moves = environment.get_location_moves(animal_location)
            # moves.append("eat")
            # moves.append("play")
        elif to_move == "human":
            moves = environment.get_location_moves(human_location)
            # moves.append("feed")
            # moves.append("pet")
        else:
            raise ValueError("Invalid to_move value: " + str(to_move))

        return GameState(to_move=to_move, utility=0, board=environment, moves=moves)
