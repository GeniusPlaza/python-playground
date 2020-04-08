""""Main program worker."""

import decorators


@decorators.authenticator
def name_formatter(name):
    """Simple name formatter.

    Relies on the decorator to ensure that only allowed names are raised.

    Raises:
        NameDoesNotExistException: raised if a given name is not allowed.
    """
    return 'Hello {}, Welcome!'.format(name.capitalize())


def main():
    """Main program call.

    Raises:
        NameDoesNotExistException: raised if a given name is not allowed.
    """
    name = input('Tell us your name: ')
    try:
        name_response = name_formatter(name.lower())
        print(name_response)

    # Wait for the possible exception.
    except decorators.NameDoesNotExistException:
        print(name, 'is not an allowed name')


if __name__ == "__main__":
    main()
