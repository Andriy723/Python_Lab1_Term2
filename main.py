"""
Lab 2 Term 2 Python
"""
# pylint: disable = import-error
from Python_Lab1_Term2.model.plane import Plane
from Python_Lab1_Term2.model.trolleybus import Trolleybus
from Python_Lab1_Term2.manager.manager import TransportManager


def main():
    """
    main func
    """Зн
    transport_manager = TransportManager()

    transport_manager.add_transport(Trolleybus(44, 44, 44, 44, 44,
                                               44, 44, 44, 44))
    transport_manager.add_transport(Plane(55, 55, 55, 55, 55))

    for transportsss in TransportManager.transports:
        print(transportsss)

    transport_manager.find_all_objects_with_speed_bigger_than(50)
    for speed_a in transport_manager.find_all_objects_with_speed_bigger_than(50):
        print("Object with speed: ", speed_a)

    transport_manager.find_all_objects_with_same_id(44)
    for id_a in transport_manager.find_all_objects_with_same_id(44):
        print("Object with id: ", id_a)


if __name__ == '__main__':
    main()
