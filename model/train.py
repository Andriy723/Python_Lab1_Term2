"""
Creator: Plish Andriy
"""
# pylint: disable = import-error
from model.abstract_transport import Transport


class Train(Transport):
    """
    child class that have some values and redefined func
    """

    def __init__(self, max_load_on_train=None, name=None, speed_of_train=None):
        self.max_load_on_train = max_load_on_train
        self.name = name
        self.speed_of_train = speed_of_train
        super().__init__(44, 44)

    def __str__(self):
        return f"Train({self.max_load_on_train}, {self.name}, " \
               f"{self.speed_of_train}, {self.max_speed}, {self.id_transport})"

    def accelerate(self):
        """
        parent method that are redefined here
        :return:
        """
        return self.speed_of_train
