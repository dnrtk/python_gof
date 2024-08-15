from pprint import pprint


class FoodFlyweightClass:
    def __init__(self, kind: str, name: str):
        self.food = {kind: name}


class FoodFlyweightFactory:
    def __init__(self):
        self.foods = {}

    def cook_food(self, kind: str, name: str):
        if kind not in self.foods.keys():
            self.foods[kind] = FoodFlyweightClass(kind, name)
            print("add {}".format(kind))
        return self.foods.get(kind)


fff = FoodFlyweightFactory()
pprint(fff.cook_food("main", "ごはん").food)
pprint(fff.cook_food("main", "ごはん").food)

pprint(fff.cook_food("sub", "サラダ").food)
pprint(fff.cook_food("sub", "サラダ").food)
pprint(fff.cook_food("sub", "サラダ").food)
