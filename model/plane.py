"""
Creator: Plish Andriy
"""
from Python_Lab1_Term2.manager.transport_manager import TransportManager
from Python_Lab1_Term2.model.abstract_transport import Transport


class Plane(Transport):
    """
    Child class that have parent method
    """
    # pylint: disable = too-many-arguments
    def __init__(self, num_of_passengers=None, max_height_of_flight=None, speed_of_plane=None,
                 max_speed=None, id_transport=None):
        """
        Constructor
        """
        self.num_of_passengers = num_of_passengers
        self.max_height_of_flight = max_height_of_flight
        self.speed_of_plane = speed_of_plane
        self.mark = {"Buet", "Liow"}
        super().__init__(max_speed, id_transport)

    def __str__(self):
        """
        Method that return String of values
        """
        return f"Plane({self.num_of_passengers}, {self.max_height_of_flight}, " \
               f"{self.speed_of_plane}, {self.max_speed}, {self.id_transport})\n"

    def accelerate(self):
        """
        parent method
        """
        return self.speed_of_plane

    def do_something(self):
        """
        :return: transports
        """
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