from typing import *
from typing import Tuple

from lazy_animal_constants import Constants


class Location:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class DefaultLocation(Location):
    def __init__(self):
        super().__init__(0, 0)


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
        self.target_animal_kcalories = Constants.target_animal_kcalories
        self.current_animal_kcalories = 0

    def __str__(self):
        ret = "tree_key: " + str(self.tree_key) \
              + "\nis_max: " + str(self.is_max)

        if not isinstance(self.animal_location, DefaultLocation):
            ret += "\nanimal_location: " + str(self.animal_location)

        if not isinstance(self.human_location, DefaultLocation):
            ret += "\nhuman_location: " + str(self.human_location)

        if len(self._food) > 0:
            ret += "\nfood: " + str(self._food)

        if len(self._toys) > 0:
            ret += "\ntoys: " + str(self._toys)

        ret += "\ncurrent_animal_kcalories: " + str(self.current_animal_kcalories)
        ret += "\ntarget_animal_kcalories: " + str(self.target_animal_kcalories)

        return ret

    def __eq__(self, other):
        """Uses tree_key as a unique identifier for the state."""
        return self.tree_key == other.tree_key

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
        for toy in self._toys:
            if toy[0] == location:
                toy[2] = True  # type: ignore

    def eats(self, location: Location):
        for food in self._food:
            if food[0] == location:
                food[2] = True  # type: ignore

    def update(self):
        if self.animal_location == self.human_location:
            print("Constraint: Animal refuses to act while human is present.")
            return

        for food in self._food:
            if self.animal_location == food[0] and food[2] is False:
                self.current_animal_kcalories += food[1]
                food[2] = True

        for toy in self._toys:
            if self.animal_location == toy[0] and toy[2] is False:
                self.current_animal_kcalories -= toy[1]
                toy[2] = True

    # TODO: Consider more fine-grained methods for the above two collections (food and toys).
