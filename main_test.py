"""Tests for main program worker."""

import unittest
from unittest import mock


def mocked_authenticator(f):
    """Mocked main.authenticator.

    This is only to show how we can manually replace a decorator.

    This mocked decorator basically does the same, but it doesn't have any
    conditions or exceptions, it's just calling and returning the function it
    decorates.
    """
    def internal(name):
        return f(name)
    return internal


class MainTestCase(unittest.TestCase):

    def test_name_formatter__mocking_outside(self):
        # We need to patch the decorator before we import the module because
        # decorators are applied at the import level, otherwise the mocked
        # function would not work.
        #
        # Here in this with statement, we are going to import main again but
        # after we mock the decorator.
        #
        # As we can see, the decorators are in their own module that is
        # easily patchable without the need to importing them.
        with mock.patch('decorators.authenticator', mocked_authenticator):
            mocked_name = 'mocked'
            import main  # NOQA W0611
            response = main.name_formatter(mocked_name)

        # Test for returned formatted string from the main function.
        self.assertEqual(
            f'Hello {mocked_name.capitalize()}, Welcome!', response)
