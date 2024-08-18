from pprint import pprint
from abc import ABC, abstractmethod


class AbstractComponent(ABC):
    @abstractmethod
    def get_foods(self) -> dict:
        pass


class MainFood(AbstractComponent):
    def __init__(self, name: str):
        self.foods = {"main": name}

    def get_foods(self) -> dict:
        return self.foods if self.foods is not None else {}


class AbstractDecorator(AbstractComponent):
    _wrapped = None

    def __init__(self, wrapped: AbstractComponent):
        self._wrapped = wrapped

    @property
    def foods(self):
        return self._wrapped.foods

    @foods.setter
    def foods(self, value):
        self._wrapped.foods = value

    def get_foods(self) -> dict:
        return self._wrapped.get_foods()


class TeisyokuDecorator(AbstractDecorator):
    def __init__(self, main_food: AbstractComponent, sub_name: str, drink_name: str):
        super().__init__(main_food)
        self.foods["sub"] = sub_name
        self.foods["drink"] = drink_name

    def get_foods(self) -> dict:
        return self.foods if self.foods is not None else {}


main_food = MainFood("からあげ")
teisyoku = TeisyokuDecorator(main_food, "ごはん", "緑茶")
pprint(teisyoku.get_foods())
