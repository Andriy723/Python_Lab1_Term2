"""
Lab 2 in python | Plish Andriy
"""
from Python_Lab1_Term2.model.abstract_transport import Transport


class Car(Transport):
    """
    The class that have one method from parent class and some values
    """

    # pylint: disable = too-many-arguments
    def __init__(self, number_of_doors=None, volume=None, max_load=None, speed_of_car=None,
                 max_speed=None, id_transport=None):
        """
        Constructor
        """
        self.number_of_doors = number_of_doors
        self.volume = volume
        self.max_load = max_load
        self.speed_of_car = speed_of_car
        super().__init__(max_speed, id_transport)

    def __str__(self):
        """
        Method that return String of values
        """
        return f"Car({self.number_of_doors}, {self.volume}, " \
               f"{self.max_load}, {self.speed_of_car}, " \
               f"{self.max_speed}, {self.id_transport})"

    def accelerate(self):
        """
        parent method
        """
        return self.speed_of_car
