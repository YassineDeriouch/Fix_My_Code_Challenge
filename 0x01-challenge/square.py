#!/usr/bin/python3
"""
Module for square class
"""


class Square():
    """ Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Instantiation of class """
        for key, value in kwargs.items():
            setattr(self, key, value)
