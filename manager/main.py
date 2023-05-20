"""
main func
"""
from typing import List, Any

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
        Train(4, 6, 2, 7, 3),
]

    def add_transport(self, transport):
        """
        Method that add new transport to list
        :param transport:
        :return:
        """
        self.transports.append(transport)

    def find_transport_with_speed_bigger_than(self, current_speed):
        """
        Method that will be searching the value I work with in objects I have created
        :param current_speed:
        :return:
        """
        small = list(filter(lambda speed: Transport.max_speed if Transport.max_speed > current_speed
        else None, self.transports))

        small = [x for x in small if x != None]

        print(small)

    def find_transport_with_id(self, current_id):
        """
        Method that will be searching object with the same id as current
        :param current_id:
        :return:
        """

    def main(self):
        """
        main func
        :return:
        """
        self.transports.append(Car(4, 4, 4, 4, 4, 4))

        transport_manager = TransportManager()

        transport_manager.add_transport(Trolleybus(4, 4, 4, 4, 4, 4, 4, 4, 4))
        transport_manager.add_transport(Plane(300, 300, 300, 300, 300))

        for transportsss in self.transports:
            print(transportsss)

        t = transport_manager.find_transport_with_speed_bigger_than(39)
        if t is not None:
            for x in t:
                print(x, "\n")

if __name__ == '__main__':
    TransportManager().main()
