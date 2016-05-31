class MyMeta(type):
    def __new__(meta, name, bases, attrs):
        attrs['_instance'] = None
        return super().__new__(meta, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=MyMeta):
    pass


f = Foo()
g = Foo()

print(f is g)
