"""
Lab 2 python
"""
# pylint: disable = import-error
from model.abstract_transport import Transport
from model.car import Car
from model.plane import Plane
from model.train import Train
from model.trolleybus import Trolleybus


class TransportManager:
    """
    Manager class
    """
    transports = [
        Train(4, 6, 2, 45, 54, "Green"),
        Car(),
    ]

    def add_transport(self, transport):
        """
        Method that add new transport to list
        """
        self.transports.append(transport)

    def find_transport_with_speed_bigger_than(self, current_speed):
        """
        Method that will be searching the value I work with in objects I have created
        """
        filtered_list = list(
            filter(lambda speed: Transport.max_speed1 > current_speed, self.transports))

        print(filtered_list)
        return filtered_list


    def find_transport_with_colour(self, current_colour):
        """
        Method that will be searching object with the same id as current
        """

        filtered_list1 = list(
            filter(lambda color: Transport.colour == current_colour, self.transports))
        print(filtered_list1, "\n\t")
        return filtered_list1
