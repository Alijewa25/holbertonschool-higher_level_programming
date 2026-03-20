#!/usr/bin/python3

class Square:
    '''
    This class defines a square.
    '''

    def __init__(self, size):
        '''
        Initializes the square with a given size.

        Args:
            size: size of the square (no validation required)
        '''
        self.__size = size
