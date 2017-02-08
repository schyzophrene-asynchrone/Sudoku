#!/usr/bin/env python3
# encoding:utf8

from cell import Cell

class Board(object):
    """Board in a Sudoku Game"""
    def __init__(self):

        self.cells = {}
        for i in range(9):
            for j in range(9):
                self.cells[(i,j)] = Cell()

    def load_boxes(self, config_file):
        pass

    def get_row(self, index):
        return [self.cells[(index,j)] for j in range(9)]

    def get_column(self, index):
        return [self.cells[(i,index)] for i in range(9)]

    def get_square(self, n, m):
        """n is the row number of the square and m is its column number"""
        square = list()
        for i in range(n*3, n*3 + 2):
            for j in range(m*3, m*3 + 2):
                square.append(self.cells[(i,j)])
        return square

    def set_value(self, n, m, value):
        """Set the value of the cell in row n and column m"""
        self.cells[(n,m)].set_value(value)

    def set_guess(self, n, m, guess):
        """Set the guess of the cell in row n and column m"""
        self.cells[(n,m)].set_guess(guess)

    def __getitem__(self, index):
        """Board expects index to be a iterable of size two"""
        if len(index) != 2:
            raise IndexError
        return self.cells[index]
