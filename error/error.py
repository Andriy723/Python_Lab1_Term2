"""
Plish Andriy
"""


class SpeedError(Exception):
    """
    Class for errors
    """
    value = "Speed shouldn't be more than 200 km per hour!\n" \
            "Please, slow down! Otherwise the police will arrest you!"

    def __init__(self):
        super().__init__(self.value)
