"""
main func
"""
# pylint: disable = import-error
from Python_Lab1_Term2.ua.lviv.iot.algo.part1.lab1.python.model.trolleybus import Trolleybus


def main():
    """
    main func
    :return:
    """
    trolleybuses = [
        Trolleybus(44, 36, 122, 27, 3, 22),
        Trolleybus(11, 22, 110, 44, 11, 22),
        Trolleybus.get_instance(),
        Trolleybus.get_instance(),
]

    print(trolleybuses[::])

    for trolleybus in trolleybuses:
        print(trolleybus)


if __name__ == '__main__':
    main()
