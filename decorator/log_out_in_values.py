"""
Decorator
"""


def log_output_input(func):
    """
    Method that log input and output
    """
    def wrapper(*args, **kwargs):
        print(f"Input values :\n args = {args}, kwargs = {kwargs}")

        result = func(*args, **kwargs)

        print(f"Output values :\n {result}")

        return result

    return wrapper
