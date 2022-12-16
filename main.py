import sys
sys.path.append('aima-python')

from runner_minimax_game1 import RunnerMinimaxGame1
from runner_genetic_game1 import RunnerGeneticGame1
from runner_montecarlo_game1 import RunnerMonteCarloGame1


def main(args):

    if len(args) == 0:
        print('No arguments passed.')
        return

    # jack1805: This command structure works, but is not obvious,
    # if the user doesn't have access to the code (i.e. not user friendly).
    if args[0] == "minimax":
        print("running minimax (alpha-beta pruning)...")
        RunnerMinimaxGame1.run_minimax()
    elif args[0] == "genetic":
        print("running genetic algorithm...")
        RunnerGeneticGame1.run_genetic()
    elif args[0] == "montecarlo":
        print("running monte carlo tree search...")
        RunnerMonteCarloGame1.run_montecarlo()
    else:
        print('Invalid argument passed - running nothing.')


if __name__ == '__main__':
    main(args=sys.argv[1:])
