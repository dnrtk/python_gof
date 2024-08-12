from abc import ABC, abstractmethod

class DatabaseClass(ABC):
    @abstractmethod
    def get_data(self, name: str):
        pass

class TeisyokuDatabaseClass:
    def __init__(self):
        self.data = {
            "焼肉定食": {
                "main": "焼肉",
                "sub": "ごはん",
                "soup": "味噌汁",
            },
            "からあげ定食": {
                "main": "からあげ",
                "sub": "五穀ご飯",
                "soup": "豚汁",
            },
        }

    def get_data(self, name: str):
        return self.data.get(name)

class FoodDatabaseClass:
    def __init__(self):
        self.data = [
            {
                "name": "牛ステーキコース",
                "main": "牛ステーキ",
                "sub": "サラダ",
                "soup": "コーンスープ",
            },
        ]

    def get_all_data(self):
        return self.data

class DatabaseAdapterClass(DatabaseClass):
    def __init__(self, fdc: FoodDatabaseClass):
        self.fdc = fdc

    def get_data(self, name: str):
        datas = self.fdc.get_all_data()
        for data in datas:
            if data.get("name") == name:
                return data
        return None

tdb = TeisyokuDatabaseClass()
print(tdb.get_data("焼肉定食"))

dac = DatabaseAdapterClass(FoodDatabaseClass())
print(dac.get_data("牛ステーキコース"))
