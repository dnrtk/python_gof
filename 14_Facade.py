from pprint import pprint


class CookerClass:
    def cook_main(self, name: str) -> dict:
        food = {"main": name}
        return food

    def cook_sub(self, name: str) -> dict:
        food = {"sub": name}
        return food

    def cook_soup(self, name: str) -> dict:
        food = {"soup": name}
        return food


class CookerFacade:
    def __init__(self):
        self.cooker = CookerClass()

    def cook_set_menu(self, name: str) -> dict:
        foods = {}
        if name == "からあげ定食":
            foods.update(self.cooker.cook_main("からあげ"))
            foods.update(self.cooker.cook_sub("白ごはん"))
            foods.update(self.cooker.cook_soup("味噌汁"))
        elif name == "とんかつ定食":
            foods.update(self.cooker.cook_main("とんかつ"))
            foods.update(self.cooker.cook_sub("麦ごはん"))
            foods.update(self.cooker.cook_soup("豚汁"))
        return foods


cf = CookerFacade()
foods = cf.cook_set_menu("からあげ定食")
pprint(foods)

foods = cf.cook_set_menu("とんかつ定食")
pprint(foods)
