"""
Lab 2 python term 2
"""
from abc import abstractmethod, ABC


class Transport(ABC):
    """
    Abstract class transport that have an abstract method accelerate
    Also that class is a parent one
    """

    def __init__(self, max_speed=None, id_transport=None):
        self.max_speed = max_speed
        self.id_transport = id_transport

    @abstractmethod
    def accelerate(self):
        """
        abstract method that will be redefined in the child classes
        :return:
        """
