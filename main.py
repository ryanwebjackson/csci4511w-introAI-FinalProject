import sys

sys.path.append('aima-python')
# from logic import * # Doesn't appear to be used.

from games import alpha_beta_search  # type: ignore
from lazy_animal_minimax_game1 import LazyAnimalMinimaxGame1


class MainHelper:
    def __init__(self):
        pass

    def help(self):
        pass


def main():

    game = LazyAnimalMinimaxGame1()
    ab_search_result = alpha_beta_search('A', game)
    print('ab_search_result: ', ab_search_result)


if __name__ == '__main__':
    main()
