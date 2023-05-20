"""
Lab 2 Term 2 Python
"""
# pylint: disable = import-error
from model.plane import Plane
from model.trolleybus import Trolleybus
from manager.manager import TransportManager


def main():
    """
    main func
    """
    transport_manager = TransportManager()

    transport_manager.add_transport(Trolleybus(44, 44, 44, 44, 44,
                                               44, 44, 44, 44))
    transport_manager.add_transport(Plane(55, 55, 55, 55, 55))

    print("\n")
    for transportsss in TransportManager.transports:
        print(transportsss)
        transport_manager.find_all_objects_with_speed_bigger_than(54)
        transport_manager.find_all_objects_with_same_id(44)

if __name__ == '__main__':
    main()
