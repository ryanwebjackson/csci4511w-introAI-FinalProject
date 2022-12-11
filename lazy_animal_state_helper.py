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
        f1 = LazyAnimalState("F1", False)
        f1.current_animal_kcalories = 25
        f2 = LazyAnimalState("F2", False)
        f2.current_animal_kcalories = 30
        g1 = LazyAnimalState("G1", False)
        g1.current_animal_kcalories = 35
        g2 = LazyAnimalState("G2", False)
        g2.current_animal_kcalories = 40
        d2 = LazyAnimalState("D2", True)  # D2 is one level higher, but is still a terminal state.
        d2.current_animal_kcalories = 51
        # 1 calorie over the target. Should be close enough, but will not currently satisfy the terminal_test.
        h1 = LazyAnimalState("H1", False)
        h1.current_animal_kcalories = 45
        h2 = LazyAnimalState("H2", False)
        h2.current_animal_kcalories = 55
        h3 = LazyAnimalState("H3", False)
        h3.current_animal_kcalories = 60
        return dict([
            (b2.tree_key, b2.current_animal_kcalories),
            (e1.tree_key, e1.current_animal_kcalories),
            (e2.tree_key, e2.current_animal_kcalories),
            (f1.tree_key, f1.current_animal_kcalories),
            (f2.tree_key, f2.current_animal_kcalories),
            (g1.tree_key, g1.current_animal_kcalories),
            (g2.tree_key, g2.current_animal_kcalories),
            (d2.tree_key, d2.current_animal_kcalories),
            (h1.tree_key, h1.current_animal_kcalories),
            (h2.tree_key, h2.current_animal_kcalories),
            (h3.tree_key, h3.current_animal_kcalories)
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

