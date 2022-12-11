from lazy_animal_state import LazyAnimalState


class LazyAnimalStateHelper:
    @staticmethod
    def get_terminal_states_for_tree1() -> dict:
        """
        Returns a dictionary of terminal states for the state transition tree 1.
        The key is the state's tree_key, the value is the utility of the state.
        """

        b2 = LazyAnimalState("B2", True)
        # Note: Had to draw out the state graph to see that B2 is a terminal state
        # (and would be a MAX node functionally if it weren't).
        b2.current_animal_kcalories = 100  # Simulates animal getting too many calories, and refusing to move.
        e1 = LazyAnimalState("E1", False)
        e1.current_animal_kcalories = 20  # Simulates end-of-day animal not getting enough calories.
        e2 = LazyAnimalState("E2", False)
        e2.current_animal_kcalories = e2.target_animal_kcalories  # Simulates perfect match of calories - goal achieved.
        # TODO: Move target_animal_kcalories out (to the LazyAnimalStateHelper class).
        return dict([
            (b2.tree_key, b2.current_animal_kcalories),
            (e1.tree_key, e1.current_animal_kcalories),
            (e2.tree_key, e2.current_animal_kcalories)
            # TODO: Add the rest of the terminal states.
            # E2=1,
            # F1=3,
            # F2=2,
            # G1=1,
            # G2=3,
            # D2=2,
            # H1=1,
            # H2=2,
            # H3=4
        ])

    @staticmethod
    def get_state_children_a() -> dict:
        return dict(
            a1=LazyAnimalState('B', is_max=False),
            a2=LazyAnimalState('C', is_max=False),
            a3=LazyAnimalState('D', is_max=False)
        )

    @staticmethod
    def get_state_children_b() -> dict:
        return dict(
            b1=LazyAnimalState('E', is_max=True),
            b2=LazyAnimalState('B2', is_max=True)
        )

