from games4e import Game  # type: ignore
from lazy_animal_environment import LazyAnimalEnvironment
from lazy_animal_state import LazyAnimalState

# def simulate(game, state):
#     """simulate the utility of current state by random picking a step"""
#     player = game.to_move(state)
#     while not game.terminal_test(state):
#         action = random.choice(list(game.actions(state)))
#         state = game.result(state, action)
#     v = game.utility(state, player)
#     return -v

# Need to implement the above hooks on the Game class.
# Then ensure the required data is populated on the State class.


class LazyAnimalMonteCarloGame(Game):
    def __init__(self, initial_state: LazyAnimalState, environment: LazyAnimalEnvironment):
        self.initial_state = initial_state
        self.environment = environment

    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        return state.moves

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        print("Calculating result...")
        print("DEBUG state: " + str(state))
        print("DEBUG move: " + str(move))

        raise NotImplementedError

    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        return not self.actions(state)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def display(self, state):
        """Print or otherwise display the state."""
        print(state)
