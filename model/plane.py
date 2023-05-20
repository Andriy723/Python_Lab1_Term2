"""
Creator: Plish Andriy
"""
# pylint: disable = import-error
from model.abstract_transport import Transport


class Plane(Transport):
    """
    Child class that have parent method
    """
    # pylint: disable = too-many-arguments
    def __init__(self, num_of_passengers=None, max_height_of_flight=None, speed_of_plane=None,
                 max_speed=None, id_transport=None):
        self.num_of_passengers = num_of_passengers
        self.max_height_of_flight = max_height_of_flight
        self.speed_of_plane = speed_of_plane
        super().__init__(max_speed, id_transport)

    def __str__(self):
        return f"Plane({self.num_of_passengers}, {self.max_height_of_flight}, " \
               f"{self.speed_of_plane}, {self.max_speed}, {self.id_transport})"

    def accelerate(self):
        """
        parent method
        """
        return self.speed_of_plane
