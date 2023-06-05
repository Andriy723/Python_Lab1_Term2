"""
Lab 2 Term 2 Python
"""
from Python_Lab1_Term2.manager.set_manager import SetManager
from Python_Lab1_Term2.model.abstract_transport import Transport
from Python_Lab1_Term2.model.plane import Plane
from Python_Lab1_Term2.model.trolleybus import Trolleybus
from Python_Lab1_Term2.manager.transport_manager import TransportManager


def main():
    """
    main func
    """
    transport_manager = TransportManager()

    transport_manager.add_transport(Trolleybus(440, 440, 440, 440, 440,
                                               440, 440, 440, 660))
    transport_manager.add_transport(Plane(55, 55, 55, 55, 44))

    for transportsss in TransportManager.transports:
        print(transportsss)

    transport_manager.find_all_objects_with_speed_bigger_than(50)
    for speed_a in transport_manager.find_all_objects_with_speed_bigger_than(50):
        print("Object with speed: ", speed_a)

    transport_manager.find_all_objects_with_same_id(44)
    for id_a in transport_manager.find_all_objects_with_same_id(44):
        print("Object with id: ", id_a)

    # Using abstract method from Transport class
    print("\nDo something :\n", Transport.do_something(Transport))

    # Enumerating
    object_enumerating = enumerate(transport_manager)

    print("Return type:", type(object_enumerating))
    print(list(enumerate(transport_manager)))

    # Getitem
    print("\nGetitem:\n", TransportManager.__getitem__(transport_manager, 1))

    # Zipping
    zipped = zip(transport_manager, Transport.do_something(Transport))
    print("Zipping :\n", *zipped)

    # Any
    print("\nAny:\n", TransportManager.any_func(transport_manager, 55))

    # All
    print("\nAll:\n", TransportManager.all_func(transport_manager, 40))

    set_manager = SetManager(transport_manager)
    for x in set_manager:
        print(x)

    set_manager = SetManager(transport_manager)
    print(len(set_manager))

    plane = Plane(100, 3060, 300, 30, 30)
    plane.dictionary(int)

    print("\n")
    Transport.error(transport_manager)

    a = ["Immmm", "rllI", "uuuuI", "Iraaaaa"]
    b = [x for x in a if x.startswith("I")]
    print (b)

if __name__ == '__main__':
    main()
