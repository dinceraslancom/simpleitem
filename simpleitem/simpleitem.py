# -*- coding: utf-8 -*-

import yaml

from typing import Iterable, Any


class SimpleItem(object):
    __slots__ = ('__dict__',)

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if isinstance(value, dict):
                value = SimpleItem(**value)
            self.__dict__[key] = value

    def __call__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if isinstance(value, dict):
                value = SimpleItem(**value)
            self.__dict__[key] = value

    def __getitem__(self, item) -> Any:
        if item not in self.__dict__:
            self.__dict__[item] = SimpleItem()

        return self.__dict__[item]

    def __getattr__(self, item) -> Any:
        if item not in self.__dict__:
            self.__dict__[item] = SimpleItem()

        if not isinstance(self.__dict__[item], SimpleItem):
            return item

        return self.__dict__[item]

    def __setitem__(self, key, value) -> None:
        self.__dict__[key] = value

    def __setattr__(self, key, value) -> None:
        self.__dict__[key] = value

    def __eq__(self, other) -> bool:
        return other is None

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self) -> int:
        return len(self.__dict__)

    def __iter__(self) -> Iterable:
        return iter(self.__dict__)

    def __contains__(self, item) -> bool:
        return item in self.__dict__

    @property
    def keys(self) -> Iterable:
        return tuple(self.__dict__.keys())

    @property
    def values(self) -> Iterable:
        return tuple(self.__dict__.values())

    @property
    def len(self) -> int:
        return len(self.__dict__)

    @property
    def print(self) -> None:
        print(self.__dict__)

    @property
    def to_dict(self) -> dict:
        return self.__dict__

    @property
    def delete(self) -> None:
        del self.__dict__

    def from_yaml(self, path):
        data = None
        with open(path) as file:
            data = file.read()
        return self(**yaml.load(data, Loader=yaml.FullLoader))


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class MemoryStorage(SimpleItem, metaclass=Singleton):
    pass
