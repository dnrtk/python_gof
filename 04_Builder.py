class Meal:
    def __init__(self):
        self._items = []

    def add_item(self, item: str):
        self._items.append(item)

    def __str__(self):
        return ", ".join(self._items)


class MealBuilder:
    def __init__(self):
        self._meal = Meal()

    def add_main_dish(self):
        self._meal.add_item("鮭の塩焼き")

    def add_side_dish(self):
        self._meal.add_item("味噌汁")

    def add_vegetable(self):
        self._meal.add_item("お新香")

    def add_dessert(self):
        self._meal.add_item("白玉団子")

    def get_meal(self) -> Meal:
        return self._meal


if __name__ == "__main__":
    builder = MealBuilder()
    builder.add_main_dish()
    # builder.add_side_dish()
    # builder.add_vegetable()
    builder.add_dessert()
    meal = builder.get_meal()
    print(meal)

    builder = MealBuilder()
    builder.add_main_dish()
    builder.add_side_dish()
    builder.add_vegetable()
    builder.add_dessert()
    meal = builder.get_meal()
    print(meal)
