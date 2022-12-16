from games4e import GameState  # type: ignore
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
    def get_initial_monte_game_state(to_move='X', x_positions=[], o_positions=[], h=3, v=3):
        # TODO: Replace the below with stuff that makes sense for the Lazy Animal game.

        """Given whose turn it is to move, the positions of X's on the board, the
        positions of O's on the board, and, (optionally) number of rows, columns
        and how many consecutive X's or O's required to win, return the corresponding
        game state"""

        moves = set([(x, y) for x in range(1, h + 1) for y in range(1, v + 1)]) - set(x_positions) - set(o_positions)
        moves = list(moves)
        board = {}
        for pos in x_positions:
            board[pos] = 'X'
        for pos in o_positions:
            board[pos] = 'O'
        return GameState(to_move=to_move, utility=0, board=board, moves=moves)
