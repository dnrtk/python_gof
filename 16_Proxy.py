from abc import ABC, abstractmethod


class CookerAbstractClass(ABC):
    @abstractmethod
    def cook_food(self, name: str):
        pass


class CookerClass(CookerAbstractClass):
    def __init__(self):
        print("new CookerClass instance")

    def cook_food(self, kind: str):
        food = {}
        if kind == "main":
            food = {kind: "からあげ"}
        elif kind == "sub":
            food = {kind: "サラダ"}
        elif kind == "soup":
            food = {kind: "味噌汁"}
        return food


class CookerProxyClass(CookerAbstractClass):
    def __init__(self):
        self.cooker = None
        print("new CookerProxyClass instance")

    def _realise(self):
        if self.cooker is None:
            self.cooker = CookerClass()

    def cook_food(self, kind: str):
        self._realise()
        print(f"call cook_food({kind=})")
        ret = self.cooker.cook_food(kind)
        print(f"called cook_food({kind=}) {ret=}")


cooker = CookerClass()
print("Processing...")
cooker.cook_food("main")
cooker.cook_food("sub")
cooker.cook_food("soup")

print("\n----------------------\n")

cooker = CookerProxyClass()
print("Processing...")
cooker.cook_food("main")
cooker.cook_food("sub")
cooker.cook_food("soup")
