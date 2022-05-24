import os


def _right(collection, key, default=None):
    if key in collection:
        return collection[key]
    return default


def _fail1(collection, key, default=None):
    if key in collection:
        return collection[key]
    return None


def _fail2(collection, key, default=None):
    return default if default else collection[key]


def _fail3(collection, key, default=None):
    if (key in collection and default is None):
        return None
    return _right(collection, key, default)


functions = {
    "right": _right,
    "fail1": _fail1,
    "fail2": _fail2,
    "fail3": _fail3,
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]
