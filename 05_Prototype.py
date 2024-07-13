import copy


class Monster:
    def __init__(self, name: str, hp: int, attack: int, defense: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense


class MonsterCatalog:
    def __init__(self):
        self._prototypes = {}

    def add_prototype(self, name: str, monster: Monster):
        self._prototypes[name] = monster

    def create_monster(self, prototype_name: str, unique_name: str = None):
        if prototype_name not in self._prototypes:
            raise KeyError("Prototype '{}' not found".format(prototype_name))

        monster = copy.deepcopy(self._prototypes[prototype_name])
        if unique_name is not None:
            monster.name = unique_name
        return monster


class SlimePrototype(Monster):
    def __init__(self):
        super().__init__("スライム", 100, 20, 10)


class GoblinPrototype(Monster):
    def __init__(self):
        super().__init__("ゴブリン", 80, 30, 15)


def show_detail(monster: Monster):
    print(
        "{}\t(HP:{} / Attack:{} / Defense:{})".format(
            monster.name, monster.hp, monster.attack, monster.defense
        )
    )


if __name__ == "__main__":
    # モンスターカタログ(プロトタイプ)作成
    catalog = MonsterCatalog()
    catalog.add_prototype("スライム", SlimePrototype())
    catalog.add_prototype("ゴブリン", GoblinPrototype())

    # モンスターパーティー作成
    monsters = [
        catalog.create_monster("スライム", "スライムA"),
        catalog.create_monster("スライム", "スライムB"),
        catalog.create_monster("スライム", "スライムC"),
        catalog.create_monster("ゴブリン"),
    ]

    # モンスターの詳細を表示
    for monster in monsters:
        show_detail(monster)
