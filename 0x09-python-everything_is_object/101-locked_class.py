#!/usr/bin/python3
"""Define a Locked class"""


class LockedClass:
    """
    Prevent the user from instantiating new Locked class attribute
    for anything but attribute called 'first_name'.
    """

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
