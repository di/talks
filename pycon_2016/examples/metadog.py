from inspect import isfunction
from functools import wraps


def woof(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('Woof!')
        return f(*args, **kwargs)
    return wrapper


class MetaDog(type):

    def __new__(meta, name, bases, attrs):
        for name, attr in attrs.items():
            print("Wrapping {}: {}".format(name, attr))
            if isfunction(attr):
                attrs[name] = woof(attr)

        return type.__new__(meta, name, bases, attrs)


class DecoratedDog():
    @woof
    def sit(self):
        print("(sitting)")

    @woof
    def stay(self):
        print("(staying)")


class Dog(metaclass=MetaDog):

    def sit(self):
        print("(sitting)")

    def stay(self):
        print("(staying)")


my_meta_dog = DecoratedDog()

my_meta_dog.sit()

my_meta_dog.stay()
