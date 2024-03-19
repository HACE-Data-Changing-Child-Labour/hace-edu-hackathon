import os
import functools

# Data path needed for Docker to correctly place files
data_path = os.path.join(os.path.dirname(__file__), "../data")


def catch_error(func):
    """ A decorator to catch S3 errors and print them to the console"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    return wrapper
