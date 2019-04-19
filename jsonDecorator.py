import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return wrapped


@to_json
def get_data():
    return {
        'data': 42
    }


class Test:

    def __init__(self):
        pass

    @staticmethod
    def met():
        pass

    @classmethod
    def init2(cls):
        pass


print({Test(): 123})
