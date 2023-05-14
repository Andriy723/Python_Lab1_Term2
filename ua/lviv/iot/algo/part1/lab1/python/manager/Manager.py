from wheel.cli import main

from Python_Lab1_Term2.ua.lviv.iot.algo.part1.lab1.python.model.Trolleybus import Trolleybus, trolleybus_1, trolleybus_2

class Manager:
  def main(self):
   trolleybus_1 = Trolleybus(44, 36, 122, 27, 3, 22)
   trolleybus_2 = Trolleybus(11, 22, 110, 44, 11, 22)

   trolleybus_1.add_passenger()
   trolleybus_2.stop()
   trolleybus_1.start()

  print("The object of Trolleybus class: trolleybus 1", trolleybus_1)
  print("The object of Trolleybus class: trolleybus 2", trolleybus_2)

if __name__ == '__main__':
   main()