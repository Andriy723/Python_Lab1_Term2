"""
Lab 2 python term 2
"""
from abc import abstractmethod, ABC


# pylint: disable = too-few-public-methods
class Transport(ABC):
    """
    Abstract class transport that have an abstract method accelerate
    Also that class is a parent one
    """

    def __init__(self, max_speed=None, id_transport=0):
        """
        Constructor
        """
        self.max_speed = max_speed
        self.id_transport = id_transport
        super().__init__()

    @abstractmethod
    def accelerate(self):
        """
        abstract method that will be redefined in the child classes
        """
