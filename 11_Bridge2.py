from abc import ABC, abstractmethod
from pprint import pprint


# 抽象クラス
# Implemenater class
class CookerClass(ABC):
    @abstractmethod
    def cook(self, ingredient) -> dict:
        pass


# Abstraction class
class TeisyokuClass(ABC):
    @abstractmethod
    def __init__(self, cooker: CookerClass):
        self.cooker = cooker

    @abstractmethod
    def cook(self) -> dict:
        pass


# 実装クラス
# ConcreteImplementer class
class YakuCookerClass(CookerClass):
    def cook(self, ingredient) -> dict:
        food = {"main": "{}の塩焼き".format(ingredient)}
        return food


class NiruCookerClass(CookerClass):
    def cook(self, ingredient) -> dict:
        food = {"main": "{}の味噌煮".format(ingredient)}
        return food


# RefineAbstraction class
class NikuTeisyokuClass(TeisyokuClass):
    def __init__(self, cooker: CookerClass):
        super().__init__(cooker)
        self.ingredient = "鶏"

    def cook(self) -> dict:
        foods = {
            "sub": "白ごはん",
            "soup": "味噌汁",
        }
        foods.update(self.cooker.cook(self.ingredient))
        return foods


class SakanaTeisyokuClass(TeisyokuClass):
    def __init__(self, cooker: CookerClass):
        super().__init__(cooker)
        self.ingredient = "鯖"

    def cook(self) -> dict:
        foods = {
            "sub": "白ごはん",
            "soup": "赤だし",
        }
        foods.update(self.cooker.cook(self.ingredient))
        return foods


nts = NikuTeisyokuClass(YakuCookerClass()).cook()
pprint(nts)

sts = SakanaTeisyokuClass(NiruCookerClass()).cook()
pprint(sts)


nts2 = NikuTeisyokuClass(NiruCookerClass()).cook()
pprint(nts2)
