#!/usr/bin/env python3
# encoding:utf8

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
                
