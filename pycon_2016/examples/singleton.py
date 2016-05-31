class Singleton():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class FooClass(Singleton):
    pass


class BooClass(Singleton):
    pass

a, b = FooClass(), FooClass()
c = BooClass()

print(a is b)
print(a is c)
