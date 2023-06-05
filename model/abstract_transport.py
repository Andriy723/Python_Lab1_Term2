"""
Lab 2 python term 2
"""
from abc import abstractmethod, ABC
from Python_Lab1_Term2.decorator.log_error_exception import logged
from Python_Lab1_Term2.error.error import SpeedError
from Python_Lab1_Term2.manager.transport_manager import TransportManager


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
        self.mark = None
        super().__init__()

    def __str__(self):
        """
        Method that return str of all values in class
        """
        return f"Transport({self.max_speed}, {self.id_transport})" \
               f"\nDictionary of Transport: \n{self.__class__.__name__}: {self.__dict__}"

    @abstractmethod
    def accelerate(self):
        """
        abstract method that will be redefined in the child classes
        """

    @abstractmethod
    def do_something(self):
        """
        :return: transports
        """
        print("\nSomething have done")
        return [x for x in TransportManager.transports]

    def dictionary(self, value_type=None):
        """
        Method that output values in dictionary with current type
        There are keys and values
        If the value != type we use then this value won't be added to list we print
        """
        if value_type is not None:
            transport_dict = {key: value for key, value in self.__dict__.items()
                           if isinstance(value, value_type)}
            print(transport_dict)

    def iter(self):
        """
        Iteration method
        """
        return iter(self.mark)

    # Exception
    @logged(SpeedError, "file", "w")
    def error(self):
        if [self.max_speed for self in TransportManager.transports if self.max_speed > 200]:
            raise SpeedError()
        else:
            print("Be careful! Good luck in a travel!")
