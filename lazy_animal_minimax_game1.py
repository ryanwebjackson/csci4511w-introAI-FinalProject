from typing import List

import games  # type: ignore
from lazy_animal_state import LazyAnimalState
from lazy_animal_state_helper import LazyAnimalStateHelper
from py_utility_functions import PyUtilityFunctions


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

    # TODO: Clarify why the following state transition tree is valid,
    # or create a new one that is valid.

    # Assume that the animal agent starts (the day/experiment) in the bedroom, and is hungry.
    initial = 'A'
    # First-level (root): A (MAX)
    # Second-level: B, C, D (MIN)
    # Third-level: E, B2, F, G, H, D2
    # Fourth-level: E1, E2, F1, F2, G1, G2, H1, H2, H3
    successors = dict(A=LazyAnimalStateHelper.get_state_children_a(),
                      B=LazyAnimalStateHelper.get_state_children_b(),
                      C=dict(c1=LazyAnimalState('F', is_max=True), c2=LazyAnimalState('G', is_max=True)),
                      D=dict(d1=LazyAnimalState('H', True), d2=LazyAnimalState('D2', True)),
                      E=dict(e1=LazyAnimalState('E1'), e2=LazyAnimalState('E2')),  # E's children are MIN nodes.
                      F=dict(f1=LazyAnimalState('F1'), f2=LazyAnimalState('F2')),
                      G=dict(g1=LazyAnimalState('G1'), g2=LazyAnimalState('G2')),
                      H=dict(h1=LazyAnimalState('H1'), h2=LazyAnimalState('H2'), h3=LazyAnimalState('H3'))
                      )
    # Note: Can clean up the code above later - may or may not need the helper functions.

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
        # Original logic: return state not in ('A', 'B', 'C', 'D')
        ret = state.current_animal_kcalories == state.target_animal_kcalories
        if ret:
            # [jack1805] Not seeing this as true. 11 Dec 2022
            # Checked in max_value and min_value of alpha_beta_search in games.py
            print("terminal_test: true")
            # PyUtilityFunctions.print_traceback()
        else:
            print("terminal_test: false")

        return ret

    def to_move(self, state: LazyAnimalState) -> str:
        return 'MIN' if not state.is_max else 'MAX'
