from abc import ABC, abstractmethod


class FoodAbstractClass(ABC):
    def __init__(self, name: str, kcal: int):
        self.name = name
        self.kcal = kcal

    @abstractmethod
    def get_kcal(self) -> int:
        pass


class FoodComposite(FoodAbstractClass):
    def __init__(self, name: str, kcal: int):
        super().__init__(name, kcal)
        self.children = []

    def add_child(self, child: FoodAbstractClass):
        self.children.append(child)

    def get_kcal(self) -> int:
        return sum([child.get_kcal() for child in self.children]) + self.kcal


class FoodLeaf(FoodAbstractClass):
    def __init__(self, name: str, kcal: int):
        super().__init__(name, kcal)

    def get_kcal(self) -> int:
        return self.kcal


karaage_teisyoku = FoodComposite("からあげ定食", 0)
karaage_teisyoku.add_child(FoodLeaf("からあげ", 500))
karaage_teisyoku.add_child(FoodLeaf("麦飯", 200))
karaage_teisyoku.add_child(FoodLeaf("味噌汁", 50))
print(karaage_teisyoku.get_kcal())
