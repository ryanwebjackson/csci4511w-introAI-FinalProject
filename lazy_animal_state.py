class Location:
    pass


class LazyAnimalState:
    """
    Notes: Goal test (terminal state test) is handled by the Game object (ex. LazyAnimalMinimaxGame1).
    Legal actions are also handled by the same class (object).
    """
    def __init__(self):
        self._toys = None
        self._food = None
        self.human_location = None
        self.animal_location = None
        # Not sure where to set this (target_animal_kcalories), so that it makes sense.
        # We don't want to start at the goal state, so we need to set it so that current and target are not initially equal.
        # Could something like float('inf'), and re-set it when the Game gets started.
        self.target_animal_kcalories = 50
        self.current_animal_kcalories = 0

    def __str__(self):
        return "animal_location: " + str(self.animal_location) \
            and "human_location: " + str(self.human_location) \
            and "food: " + str(self._food) \
            and "toys: " + str(self._toys)

    def __eq__(self, other):
        return self.animal_location == other.animal_location \
            and self.human_location == other.human_location \
            and self._food == other.food \
            and self._toys == other.toys

    def __hash__(self):
        return hash((self.animal_location, self.human_location, self._food, self._toys))

    # Dev. note: Not sure if the below getters and setters needed - still getting used to Python.
    def get_animal_location(self):
        return self.animal_location

    def set_animal_location(self, location: Location):
        self.animal_location = location

    def get_human_location(self):
        return self.human_location

    def set_human_location(self, location: Location):
        self.human_location = location

    def get_food(self):
        return self._food

    def set_food(self, value: [(Location, int, bool)]):
        self._food = value

    def del_food(self):
        del self._food

    def get_toys(self):
        return self._toys

    def set_toys(self, value: [(Location, int, bool)]):
        """
        integer in the tuple is the amount of KCalories burned by playing with the toy at the given location.
        boolean in the tuple is IsPlayedWith.
        """
        self._toys = value

    def del_toys(self):
        del self._toys

    food = property(get_food, set_food, del_food)
    toys = property(get_toys, set_toys, del_toys)

    def plays(self, location: Location):
        """Sets IsPlayedWith to true for all toys at the given location."""
        pass  # TODO: Add code to flip IsPlayedWith to true (for a given toy location).

    def eats(self, location: Location):
        pass  # TODO: Add code to flip IsEaten to true (for a given food location).

    # TODO: Consider more fine-grained methods for the above two collections (food and toys).