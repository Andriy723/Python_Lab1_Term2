"""
Plish Andriy
"""
import logging


def logged(exception, mode, filemode):
    """
    logger
    """
    def decorator(func):

        def wrapper(*args, **kwargs):

            try:
                return func(*args, **kwargs)

            except exception as e_1:
                if mode == "console":
                    logging.basicConfig(level=logging.DEBUG)
                    logging.error(str(e_1))

                elif mode == "file":
                    logging.basicConfig(filename='errors.loging', level=logging.DEBUG, filemode=filemode)
                    logging.error(str(e_1))

                return None

        return wrapper

    return decorator
