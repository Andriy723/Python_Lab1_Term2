"""
Class that have many values and methods
"""
# pylint: disable = import-error
from model.abstract_transport import Transport


class Trolleybus(Transport):
    """
    Class that have many values and methods
    """
    __default_trolleybus = None

    # pylint: disable = too-many-arguments
    def __init__(self, route_number=None, current_stop=None,
                 max_speed_of_trolleybus=None, capacity=None, passengers=None,
                 current_speed=None, max_speed=None, id_transport=None,
                 colour=None, id_trolleybus=100):
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed_of_trolleybus = max_speed_of_trolleybus
        self.capacity = capacity
        self.passengers = passengers
        self.current_speed = current_speed
        self.id_trolleybus = id_trolleybus
        super().__init__(max_speed, id_transport, colour)

    def __str__(self):
        return f"Trolleybus({self.route_number}, {self.current_stop}, " \
               f"{self.max_speed_of_trolleybus}, {self.capacity}, " \
               f"{self.passengers}, {self.current_speed}, " \
               f"{self.id_trolleybus}, {self.max_speed}, {self.id_transport}, " \
               f"{self.colour})"

    @staticmethod
    def get_instance():
        """
        Method get_instance() that return an empty object
        """
        if Trolleybus.__default_trolleybus is None:
            Trolleybus.__default_trolleybus = Trolleybus()
        return Trolleybus.__default_trolleybus

    def stop(self):
        """
        That method change current_speed to 0
        """
        self.current_speed = 0

    def start(self):
        """
        That method change current_speed to 20
        """
        self.current_speed = 20

    def add_passenger(self):
        """
        Add_passenger add one passenger to the object when capacity > passengers
        """
        if self.passengers < self.capacity:
            self.passengers += 1
        else:
            print("Trolleybus is overcrowded!")

    def remove_passenger(self):
        """
        That method remove one passenger from the object when capacity < passengers
        """
        if self.passengers > self.capacity:
            self.passengers -= 1
        else:
            print("Trolleybus is not overcrowded! So, you can get into it.")

    @property
    def get_current_speed(self):
        """
        :param self:
        """
        print(self.get_current_speed.__doc__)
        return self.current_speed + 10

    @get_current_speed.setter
    def set_current_speed(self, speed):
        print(self.set_current_speed.__doc__)
        self.current_speed = speed + 10

    def accelerate(self):
        """
        parent method
        """
        return self.current_speed
