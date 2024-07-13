class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    singleton = Singleton()
    print(singleton)

    singleton2 = Singleton()
    print(singleton2)

    assert singleton is singleton2
