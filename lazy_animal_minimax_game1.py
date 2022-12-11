from typing import List

import games  # type: ignore
from lazy_animal_state import LazyAnimalState
from lazy_animal_state_helper import LazyAnimalStateHelper


class LazyAnimalMinimaxGame1(games.Game):
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

    # Assume that the animal agent starts (the day/experiment) in the bedroom, and is hungry.
    initial = 'A'
    successors = dict(A=LazyAnimalStateHelper.get_state_children_a(),
                      B=dict(b1='E', b2='B2'),
                      C=dict(c1='F', c2='G'),
                      D=dict(d1='H', d2='D2'),
                      E=dict(e1='E1', e2='E2'),
                      F=dict(f1='F1', f2='F2'),
                      G=dict(g1='G1', g2='G2'),
                      H=dict(h1='H1', h2='H2', h3='H3'))
    # Second-level successors:
    utils = LazyAnimalStateHelper.get_terminal_states_for_tree1()

    def actions(self, state: LazyAnimalState) -> List[str]:
        return list(self.successors.get(state.tree_key, {}).keys())

    def result(self, state: LazyAnimalState, move) -> LazyAnimalState:
        return self.successors[state.tree_key][move]

    def utility(self, state: LazyAnimalState, player):
        if player == 'MAX':
            return self.utils[state.tree_key]
        else:
            return -self.utils[state.tree_key]

    def terminal_test(self, state: LazyAnimalState):
        return state.current_animal_kcalories == state.target_animal_kcalories

    def to_move(self, state: LazyAnimalState) -> str:
        return 'MIN' if not state.is_max else 'MAX'
