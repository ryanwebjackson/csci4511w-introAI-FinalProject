import sys
sys.path.append('aima-python')

from lazy_animal_environment import LazyAnimalEnvironment
from lazy_animal_constants import Constants
from lazy_animal_monte_carlo_game import LazyAnimalMonteCarloGame
from lazy_animal_game_state_adapter_monte import LazyAnimalGameStateAdapterMonteCarlo
from lazy_animal_state import LazyAnimalState
from lazy_animal_state_helper import LazyAnimalStateHelper

# Note: Monte Carlo Tree Search (MCTS) is not implemented in the aima-python games.py file
# (non 4e version), so using games4e.py here instead.
from games4e import *  # type: ignore
from tests.test_games4e import *  # type: ignore


class RunnerMonteCarloGame1:
    @staticmethod
    def run_montecarlo():

        game_state = LazyAnimalGameStateAdapterMonteCarlo.get_initial_monte_game_state(
            to_move='animal',  # Could use an Enum here instead for some type safety.
            animal_location=(1, 1),
            human_location=(1, 2)
        )

        lazy_animal_state_initial = LazyAnimalStateHelper.get_initial_state()
        adapter = LazyAnimalGameStateAdapterMonteCarlo(game_state, lazy_animal_state_initial)

        # Note: expected_result not used for now.
        expected_result = LazyAnimalState(tree_key="D", is_max=False)
        expected_result.current_animal_kcalories = Constants.target_animal_kcalories

        state = adapter.adapt_gamestate_to_domainstate()

        environment = LazyAnimalEnvironment()
        
        game = LazyAnimalMonteCarloGame(lazy_animal_state_initial, environment)
        result = monte_carlo_tree_search(state, game)

        # Saving the below for now: random_player will be useful for testing
        # or illustrating performance of the search algorithms.
        #assert ttt.play_game(mcts_player, random_player) >= 0
        # Note: players are functions called by play_game.
