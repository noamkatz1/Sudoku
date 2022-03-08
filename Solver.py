from Board import Board
import random
import copy

class Solver(Board):
    def __init__(self,code,board):
        self.code = code
        self.board = board
    
    def solveForCode(self):
        return self.boardToCode(self.solve())
    
    def solve(self): 
        _spacesAvailable = self.findSpaces()

        if not _spacesAvailable:
            return True
        else:
            row, col = _spacesAvailable

        for n in range(1, 10):
            if self.checkSpace(n, (row, col)):
                self.board[row][col] = n

                if self.solve():
                    return self.board

                self.board[row][col] = 0

        return False

        
    