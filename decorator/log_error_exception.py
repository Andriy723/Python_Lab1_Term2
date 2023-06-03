"""
Plish Andriy
"""
import logging


def logged(exception, mode):
    """
    logger
    """
    def decorator(func):

        def wrapper(*args, **kwargs):

            try:
                return func(*args, **kwargs)

            except exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.DEBUG)
                    logging.error(str(e))

                elif mode == "file":
                    logging.basicConfig(filename='errors.loging', level=logging.DEBUG)
                    logging.error(str(e))

        return wrapper

    return decorator
