"""
Lab 2 python
"""


class TransportManager:
    """
    Manager class
    """
    transports = []
    index = 0

    def add_transport(self, transport):
        """
        Method that add new transport to list
        """
        self.transports.append(transport)

    def find_all_objects_with_speed_bigger_than(self, speed):
        """
        Method that will be searching the value I work with in objects I have created
        """
        return filter(lambda transport: transport.max_speed > speed, self.transports)

    def find_all_objects_with_same_id(self, id_transport):
        """
        Method that will be searching object with the same id as current
        """
        return filter(lambda transport: transport.id_transport is id_transport, self.transports)

    def __len__(self):
        """
        Method that returns the length of transports
        """
        return len(self.transports)

    def __getitem__(self, index):
        """
        Method that prints type of transports
        """
        return self.transports[index]

    def __iter__(self):
        """
        Method that returns itself
        """
        self.index = 0
        return self

    def __next__(self):
        """
        Method that afford us to iterate all around the transports
        And if index is out of transports then this method will stop iterating and give an error
        """
        if self.index >= len(self.transports):
            raise StopIteration
        something = self.transports[self.index]
        self.index += 1
        return something

    def any_func(self, value):
        """
        Method that returns any of the current true variable
        """
        any_a = any(transport.max_speed == value for transport in self.transports)
        return any_a

    def all_func(self, value):
        """
        Method that returns all the current true variable
        """
        all_a = all(transport.id_transport > value for transport in self.transports)
        return all_a
