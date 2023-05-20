"""
Lab 2 python term 2
"""
from abc import abstractmethod, ABC


class Transport(ABC):
    """
    Abstract class transport that have an abstract method accelerate
    Also that class is a parent one
    """
    max_speed1 = 450
    colour = "Green"

    def __init__(self, max_speed=None, colour=None, id_transport=0):
        self.max_speed = max_speed
        self.id_transport = id_transport
        self.colour = colour
        super().__init__()

    @abstractmethod
    def accelerate(self):
        """
        abstract method that will be redefined in the child classes
        """
