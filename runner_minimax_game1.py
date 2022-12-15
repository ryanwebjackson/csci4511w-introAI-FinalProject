from games import alpha_beta_search
from lazy_animal_minimax_game1 import LazyAnimalMinimaxGame1
from lazy_animal_state_helper import LazyAnimalStateHelper


class RunnerMinimaxGame1:
    @staticmethod
    def run_minimax():
        game = LazyAnimalMinimaxGame1()
        initial_state = LazyAnimalStateHelper.get_initial_state()
        ab_search_result = alpha_beta_search(initial_state, game)
        print('ab_search_result: ', ab_search_result)

        # minimax_search_result = alpha_beta_search(initial_state, game, avoid_pruning=True)
        # print('minimax_search_result: ', minimax_search_result)

        # Best Action (key) is returned from 'alpha_beta_search', but not the terminal state that it leads to.
        # Also note that it's possible that a (business) goal state is not reached - seeing this happen.
        # Ideal: Return the whole path, from initial state to terminal state (and if goal was reached). jack1805
