import sys
sys.path.append('aima-python')

from lazy_animal_state import LazyAnimalState
from search import *  # type: ignore
from tests.test_search import *  # type: ignore
from games import alpha_beta_search  # type: ignore
from lazy_animal_minimax_game1 import LazyAnimalMinimaxGame1


class MainHelper:
    def __init__(self):
        pass

    def help(self):
        pass


def run_minimax():
    game = LazyAnimalMinimaxGame1()

    initial_state = LazyAnimalState()
    initial_state.tree_key = 'A'
    initial_state.is_max = True

    ab_search_result = alpha_beta_search(initial_state, game)
    print('ab_search_result: ', ab_search_result)

    # minimax_search_result = alpha_beta_search(initial_state, game, avoid_pruning=True)
    # print('minimax_search_result: ', minimax_search_result)

    # Best Action (key) is returned from 'alpha_beta_search', but not the terminal state that it leads to.
    # Also note that it's possible that a (business) goal state is not reached - seeing this happen.
    # Ideal: Return the whole path, from initial state to terminal state (and if goal was reached). jack1805


def run_genetic():
    # AIMA code example for bootstrapping:

    def aimatest_genetic_algorithm():
        # Graph coloring
        edges = {'A': [0, 1],
                 'B': [0, 3],
                 'C': [1, 2],
                 'D': [2, 3]}

        def fitness(c):
            return sum(c[n1] != c[n2] for (n1, n2) in edges.values())

        solution_chars = GA_GraphColoringChars(edges, fitness)
        assert solution_chars == ['R', 'G', 'R', 'G'] or solution_chars == ['G', 'R', 'G', 'R']

        solution_bools = GA_GraphColoringBools(edges, fitness)
        assert solution_bools == [True, False, True, False] or solution_bools == [False, True, False, True]

        solution_ints = GA_GraphColoringInts(edges, fitness)
        assert solution_ints == [0, 1, 0, 1] or solution_ints == [1, 0, 1, 0]

        # Queens Problem
        gene_pool = range(8)
        population = init_population(100, gene_pool, 8)

        def fitness(q):
            non_attacking = 0
            for row1 in range(len(q)):
                for row2 in range(row1 + 1, len(q)):
                    col1 = int(q[row1])
                    col2 = int(q[row2])
                    row_diff = row1 - row2
                    col_diff = col1 - col2

                    if col1 != col2 and row_diff != col_diff and row_diff != -col_diff:
                        non_attacking += 1

            return non_attacking

        solution = genetic_algorithm(population, fitness, gene_pool=gene_pool, f_thres=25)
        print("fitness(solution) >= 25: ", fitness(solution) >= 25)

    aimatest_genetic_algorithm()


def main(args):

    if len(args) == 0:
        print('No arguments passed.')
        return

    # jack1805: This command structure works, but is not obvious,
    # if the user doesn't have access to the code (i.e. not user friendly).
    if args[0] == "minimax":
        print("running minimax (alpha-beta pruning)...")
        run_minimax()
    elif args[0] == "genetic":
        print("running genetic algorithm...")
        run_genetic()


if __name__ == '__main__':
    main(args=sys.argv[1:])
