# coding=utf-8
from abc import ABC, abstractmethod

class Task(ABC):
    """Abstract class with abstract methods: `make_noise` and `name`

    The `make_noise` method takes no argument, and the name is a property.

    Write the body of this class
    """
    @abstractmethod
    def make_noise(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass
