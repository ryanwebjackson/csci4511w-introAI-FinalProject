import agents  # type: ignore


class LazyAnimalEnvironment(agents.XYEnvironment):
    """
    [jack1805] Might not be perfect (not sure about "holding"), but starting with the XYEnvironment,
    to create a simple environment for the lazy animal to move around in.
    """

    def percept(self, agent):
        return None

    def execute_action(self, agent, action):
        pass

    def is_done(self):
        return True

    def get_location_moves(self, animal_location):
        return [
            (animal_location[0] + 1, animal_location[1]),
            (animal_location[0] + 1, animal_location[1] - 1),
            (animal_location[0] + 1, animal_location[1] + 1),
            (animal_location[0] - 1, animal_location[1]),
            (animal_location[0] - 1, animal_location[1] - 1),
            (animal_location[0] - 1, animal_location[1] + 1),
            (animal_location[0], animal_location[1] - 1),
            (animal_location[0], animal_location[1] + 1),
            (animal_location[0], animal_location[1])
        ]
