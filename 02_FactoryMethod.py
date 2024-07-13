from abc import ABC, abstractmethod


class FoodFactory(ABC):
    @abstractmethod
    def cook(self):
        raise NotImplementedError


class Food:
    def __init__(self, staple_food: str, main_dish: str, soup: str):
        self.staple_food = staple_food
        self.main_dish = main_dish
        self.soup = soup

    def print_foods(self):
        print(" 主食: {}".format(self.staple_food))
        print(" 主菜: {}".format(self.main_dish))
        print(" 汁物: {}".format(self.soup))
        print("")


class JapaneseFoodFactory(FoodFactory):
    def cook(self):
        print("日本食を作る")
        return Food("ご飯", "鯖の味噌煮", "味噌汁")


class ItalianFoodFactory(FoodFactory):
    def cook(self):
        print("イタリア料理を作る")
        return Food("Risotto", "Pollo al pomodoro", "Espresso")


if __name__ == "__main__":
    factory = JapaneseFoodFactory()
    food = factory.cook()
    food.print_foods()

    factory = ItalianFoodFactory()
    food = factory.cook()
    food.print_foods()
