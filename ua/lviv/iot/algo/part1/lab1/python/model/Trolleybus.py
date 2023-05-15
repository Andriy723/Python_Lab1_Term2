class Trolleybus:

    __default_trolleybus = None

    def __init__(self, route_number=None, current_stop=None,
                 max_speed=None, capacity=None, passengers=None, current_speed=None, id=100):
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.capacity = capacity
        self.passengers = passengers
        self.current_speed = current_speed
        self.id = id

    def __str__(self):
        return f"({self.route_number}, {self.current_stop}, {self.max_speed}, {self.capacity}, {self.passengers}," \
               f" {self.current_speed}, {self.id})"

    @staticmethod
    def get_instance():
        if Trolleybus.__default_trolleybus is None:
            Trolleybus.__default_trolleybus = Trolleybus()
        return Trolleybus.__default_trolleybus

    def stop(self):
        self.current_speed = 0

    def start(self):
        self.current_speed = 20

    def add_passenger(self):
        if self.passengers < self.capacity:
            self.passengers += 1
        else:
            print("Trolleybus is overcrowded!")

    def remove_passenger(self):
        if self.passengers > self.capacity:
            self.passengers -= 1
        else:
            print("Trolleybus is not overcrowded! So, you can get into it.")
