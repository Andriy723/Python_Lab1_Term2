"""
Lab 2 Term 2 Python
"""
# pylint: disable = import-error
from model.car import Car
from model.plane import Plane
from model.trolleybus import Trolleybus
from manager.manager import TransportManager


def main():
    """
    main func
    """
    TransportManager.transports.append(Car(4, 4, 4, 4, 45, 54, "Green"))

    transport_manager = TransportManager()

    transport_manager.add_transport(Trolleybus(4, 4, 4, 4, 4,
                                               4, 4, 45, 54, "White"))
    transport_manager.add_transport(Plane(300, 300, 300, 56, 54, "Blue"))

    print("\t\t\t")
    for transportsss in TransportManager.transports:
        print(transportsss)

        transport_manager.find_transport_with_speed_bigger_than(67)

        transport_manager.find_transport_with_colour("Green")

if __name__ == '__main__':
    main()
