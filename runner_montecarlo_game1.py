import sys
sys.path.append('aima-python')

# Note: Monte Carlo Tree Search (MCTS) is not implemented in the aima-python games.py file
# (non 4e version), so using games4e.py here instead.
from games4e import *  # type: ignore
from tests.test_games4e import *  # type: ignore


class RunnerMonteCarloGame1:
    @staticmethod
    def run_montecarlo():

        # TEMP: Copied test code to prove we can run MCTS on a simple game.
        state = gen_state(to_move='X', x_positions=[(1, 1), (3, 3)],
                          o_positions=[(1, 2), (3, 2)])
        assert monte_carlo_tree_search(state, ttt) == (2, 2)

        state = gen_state(to_move='O', x_positions=[(1, 1), (3, 1), (3, 3)],
                          o_positions=[(1, 2), (3, 2)])
        assert monte_carlo_tree_search(state, ttt) == (2, 2)

        state = gen_state(to_move='X', x_positions=[(1, 1), (3, 1)],
                          o_positions=[(2, 2), (3, 1)])
        assert monte_carlo_tree_search(state, ttt) == (1, 3)

        # should never lose to a random or alpha_beta player in a ttt game
        assert ttt.play_game(mcts_player, random_player) >= 0
        assert ttt.play_game(mcts_player, alpha_beta_player) >= 0

        # should never lose to a random player in a Connect Four game
        assert con4.play_game(mcts_player, random_player) >= 0
