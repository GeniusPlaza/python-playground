"""Decorators from Python test playground."""


_ALLOWED_NAMES = frozenset({'juan', 'joseph', 'kalyan'})


class NameDoesNotExistException(Exception):
    """Raised if given name does not exist."""


def authenticator(f):
    """Base authenticator decorator.

    Checks if a given name is in the allowed names list.

    Raises:
        NameDoesNotExistException: raised if a given name is not allowed.
    """
    def inside(name):
        if name not in _ALLOWED_NAMES:
            raise NameDoesNotExistException(
                f'Given name {name}, does not exist.')
        return f(name)
    return inside
