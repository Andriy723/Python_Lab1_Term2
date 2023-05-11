class Trolleybus:

    def __init__(self, route_number, current_stop, max_speed, capacity, passengers, current_speed, id = 100):
        self.id = id
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.capacity = capacity
        self.passengers = passengers
        self.current_speed = current_speed

    def __str__(self):
        return f"({self.route_number}, {self.current_stop}, {self.max_speed}, {self.capacity}, {self.passengers}," \
               f" {self.current_speed}, {self.id})"

    def stop(self):
        self.current_speed = 0

    def start(self):
        self.current_speed = 20

    def add_passenger(self):
        if self.passengers < self.capacity:
            self.passengers += 1
        else: print("Trolleybus is overcrowded!")

    def remove_passenger(self):
        if self.passengers > self.capacity:
            self.passengers -= 1
        else: print("Trolleybus is not overcrowded! So, you can get into it.")

trolleybus_1 = Trolleybus(44, 36, 122, 27, 3, 22)
trolleybus_2 = Trolleybus(11, 22, 110, 44, 11, 22)

trolleybus_1.add_passenger()
trolleybus_2.stop()
trolleybus_1.start()

print("The object of Trolleybus class: trolleybus 1", trolleybus_1)
print("The object of Trolleybus class: trolleybus 2", trolleybus_2)