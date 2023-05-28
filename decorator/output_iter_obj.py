"""
Decorator
"""


def length_logger_decorator(func):
    """
    Decorator that returns the length of an iterable object
    If the object is not iterable, it returns 1
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        try:
            length = len(result)
            if hasattr(result, '__iter__') and not isinstance(result, str):
                print(f"Length of iterable object is: {length}")
            else:
                print("Object is not iterable")
                length = 1
        except TypeError:
            print("Object is not iterable")
            length = 1

        return result

    return wrapper
