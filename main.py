import sys

sys.path.append('aima-python')
from logic import *

from games import alpha_beta_search
from final_minimax_game import FinalGame


class MainHelper:
    def __init__(self):
        pass

    def help(self):
        pass


def main():

    game = FinalGame()
    ab_search_result = alpha_beta_search('A', game)
    print('ab_search_result: ', ab_search_result)


if __name__ == '__main__':
    main()
