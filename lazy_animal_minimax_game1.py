from games import *


class LazyAnimalMinimaxGame1(Game):
    """
    A MiniMax Game, designed with one possible state transition tree.
    The problem: A lazy animal wants as much food as possible.
    A responsible owner wants to feed the animal as little as possible,
    while still keeping it alive, and healthy.

    From 'games.py' in aima-python:
    'A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost' - For this Game,
    however, there will be something similar t a path cost - if the animal moves in the environment,
    its KCalories will decrease. The utility of a state will be the KCalories of the animal.
    There will arise some complications with that, but the experiments will start simply, and get more complex.

    One of the planned enhancements: Randomize the initial state.
    It is not realistic that the animal is in the same place,
    and at the same hunger level (current KCalories), at the same time, every day.
    
    Note that Alpha-Beta pruning and non-pruning algorithms will be run in the main.py - both are minimax problems (games), so can share the same Game object definition.
    However, leaving this class named with an ordinal to show that there may be other state transition trees possible for this problem.
    """

    # TODO: Replace the below definitions with your own,
    #  defined by one possible state transition tree for the given problem.
    successors = dict(A=dict(a1='B', a2='C', a3='D'),
                      B=dict(b1='E', b2='B2'),
                      C=dict(c1='F', c2='G'),
                      D=dict(d1='H', d2='D2'),
                      E=dict(e1='E1', e2='E2'),
                      F=dict(f1='F1', f2='F2'),
                      G=dict(g1='G1', g2='G2'),
                      H=dict(h1='H1', h2='H2', h3='H3'))
    utils = dict(
        B2=3,
        E1=2,
        E2=1,
        F1=3,
        F2=2,
        G1=1,
        G2=3,
        D2=2,
        H1=1,
        H2=2,
        H3=4)
    initial = 'A'

    def actions(self, state):
        return list(self.successors.get(state, {}).keys())

    def result(self, state, move):
        return self.successors[state][move]

    def utility(self, state, player):
        if player == 'MAX':
            return self.utils[state]
        else:
            return -self.utils[state]

    def terminal_test(self, state):
        return state not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

    def to_move(self, state):
        return 'MIN' if state in 'BCD' else 'MAX'
