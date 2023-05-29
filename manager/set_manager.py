"""
Lab 9 Term 2 python
"""
from Python_Lab1_Term2.manager.transport_manager import TransportManager
from Python_Lab1_Term2.decorator.log_out_in_values import log_output_input
from Python_Lab1_Term2.decorator.output_iter_obj import length_logger_decorator

class SetManager:
    """
    Class that contains in itself basic magic methods and doesn't
    use in order to create objects or does not have any inheritance
    """
    def __init__(self, regular_manager: TransportManager):
        """
        Constructor
        """
        self.regular_manager = regular_manager
        self.index = 0

    def __str__(self):
        """
        Method that return str of values in current class
        """
        return f"SetManager{self.regular_manager}"

    def __iter__(self):
        """
        Method that return iterator
        """
        for transport in self.regular_manager.transports:
            yield transport

    def __next__(self):
        """
        Method that afford us to iterate all around the transports
        And if index is out of transports then this method will stop iterating and give an error
        """
        if self.index >= len(self.regular_manager):
            raise StopIteration
        something = self.regular_manager[self.index]
        self.index += 1
        return something

    def __getitem__(self, index):
        """
        Method that returns object on current index
        """
        for transports in self.regular_manager:
            return transports[index].mark

    @log_output_input
    @length_logger_decorator
    def __len__(self):
        """
        :return: length
        """
        length = 0
        for transports in self.regular_manager:
            length += 1
        return length
