from lazy_animal_state import LazyAnimalState


class LazyAnimalStateHelper:
    @staticmethod
    def get_terminal_states_for_tree1() -> dict:
        """
        Returns a dictionary of terminal states for the state transition tree 1.
        The key is the state's tree_key, the value is the utility of the state.
        """
        # TODO: Replace the below stub with the mapping of terminal states to their static tree_key values,
        #  and their utility values.
        return dict(
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

