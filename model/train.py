"""
Creator: Plish Andriy
"""
from Python_Lab1_Term2.model.abstract_transport import Transport


class Train(Transport):
    """
    child class that have some values and redefined func
    """
    # pylint: disable = too-many-arguments
    def __init__(self, max_load_on_train=None, name=None, speed_of_train=None,
                 max_speed=None, id_transport=None):
        """
        Constructor
        """
        self.max_load_on_train = max_load_on_train
        self.name = name
        self.speed_of_train = speed_of_train
        super().__init__(max_speed, id_transport)

    def __str__(self):
        """
        Method that return String of objects
        """
        return f"Train({self.max_load_on_train}, {self.name}, " \
               f"{self.speed_of_train}, {self.max_speed}, {self.id_transport})"

    def accelerate(self):
        """
        parent method that are redefined here
        """
        return self.speed_of_train
