"""
Lab 2 python
"""


class TransportManager:
    """
    Manager class
    """
    transports = []

    def add_transport(self, transport):
        """
        Method that add new transport to list
        """
        self.transports.append(transport)

    def find_all_objects_with_speed_bigger_than(self, speed):
        """
        Method that will be searching the value I work with in objects I have created
        """
        print("Object with speed is found:",
              *[transport for transport in self.transports if transport.max_speed > speed])

    def find_all_objects_with_same_id(self, id_transport):
        """
        Method that will be searching object with the same id as current
        """
        print("Object with id is found:",
              *[transport for transport in self.transports if transport.id_transport == id_transport])
