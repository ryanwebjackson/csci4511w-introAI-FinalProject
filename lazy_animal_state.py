from typing import *


class Location:
    pass


class DefaultLocation(Location):
    pass


class LazyAnimalState:
    """
    Notes: Goal test (terminal state test) is handled by the Game object (ex. LazyAnimalMinimaxGame1).
    Legal actions are also handled by the same class (object).
    """
    # Note: Leaving default values for required parameters for now -
    # games.py code might be initializing the state automatically.
    # TODO: Remove default values for required parameters when possible.
    def __init__(self, tree_key: str = "NotSet", is_max: bool = False):

        self._toys: List[Tuple[Location, int, bool]] = []
        self._food: List[Tuple[Location, int, bool]] = []
        self.human_location: Location = DefaultLocation()
        self.animal_location: Location = DefaultLocation()
        self.is_max = is_max
        self.tree_key = tree_key
        # Not sure where to set this (target_animal_kcalories), so that it makes sense.
        # We don't want to start at the goal state, so we need to set it so that current and target are not initially equal.
        # Could something like float('inf'), and re-set it when the Game gets started.
        self.target_animal_kcalories = 50
        self.current_animal_kcalories = 0

    def __str__(self):
        return "animal_location: " + str(self.animal_location) \
            + "\nhuman_location: " + str(self.human_location) \
            + "\nfood: " + str(self._food) \
            + "\ntoys: " + str(self._toys)

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

    def set_food(self, value: List[Tuple[Location, int, bool]]):
        self._food = value

    def del_food(self):
        del self._food

    def get_toys(self):
        return self._toys

    def set_toys(self, value: List[Tuple[Location, int, bool]]):
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
