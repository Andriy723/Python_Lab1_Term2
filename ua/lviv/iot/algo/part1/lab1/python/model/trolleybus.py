"""
Class that have many values and methods
"""
class Trolleybus:
    """
    Class that have many values and methods
    """
    __default_trolleybus = None
    # pylint: disable = too-many-arguments
    def __init__(self, route_number=None, current_stop=None,
        max_speed=None, capacity=None, passengers=None, current_speed=None, id_trolleybus=100):
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.capacity = capacity
        self.passengers = passengers
        self.current_speed = current_speed
        self.id_trolleybus = id_trolleybus

    def __str__(self):
        return f"({self.route_number}, {self.current_stop}, {self.max_speed}, {self.capacity}, " \
               f"{self.passengers}, {self.current_speed}, {self.id_trolleybus})"

    @staticmethod
    def get_instance():
        """
        Method get_instance() that return an empty object
        :return:
        """
        if Trolleybus.__default_trolleybus is None:
            Trolleybus.__default_trolleybus = Trolleybus()
        return Trolleybus.__default_trolleybus

    def stop(self):
        """
        That method change current_speed to 0
        :return:
        """
        self.current_speed = 0

    def start(self):
        """
        That method change current_speed to 20
        :return:
        """
        self.current_speed = 20

    def add_passenger(self):
        """
        Add_passenger add one passenger to the object when capacity > passengers
        :return:
        """
        if self.passengers < self.capacity:
            self.passengers += 1
        else:
            print("Trolleybus is overcrowded!")


    def remove_passenger(self):
        """
        That method remove one passenger from the object when capacity < passengers
        :return:
        """
        if self.passengers > self.capacity:
            self.passengers -= 1
        else:
            print("Trolleybus is not overcrowded! So, you can get into it.")

    @property
    def get_current_speed(self):
        """
        :param self:
        :return:
        """
        print("getter")
        self.get_current_speed.__doc__
        return self.current_speed + 10

    @get_current_speed.setter
    def set_current_speed(self, speed):
        print("setter")
        self.current_speed = speed + 10
