#!/usr/bin/env python3
# encoding:utf8

class Cell(object):
    """Cell in a Sudoku game"""
    def __init__(self):
        self.value = None
        self.guess = []
        self.is_mutable = True
        
    def set_value(self, value):
        """value is an integer between 1 and 9, 
        if not, a ValueError is raised"""
        if value in tuple(x for x in range(1,10)):
            self.value = value
        else:
            raise ValueError
            
    def set_guess(self, guess):
        """guess is a list containing integers between 
        1 and 9, if not, a ValueError is raised"""
        for value in guess:
            if value not in tuple(x for x in range(1,10)):
                raise ValueError
        self.guess = guess 
        
    def set_mutable(self, value):
        """value is a boolean"""
        self.is_mutable = value
