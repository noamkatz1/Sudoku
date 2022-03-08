import copy
import random

class Board:

    def __init__(self, code=None):
        self.resetBoard()
        self.board = None 
        if code:
            self.fill_code(code)
        else:
            self.code = None
            
    def fill_code(self,code):
            self.code = code
            for row in range(9):
                for col in range(9):
                    self.board[row][col] = int(code[0])
                    code = code[1:]

    def boardToCode(self, input_board=None):
        if input_board:
            _code = ''.join([str(i) for j in input_board for i in j])
            return _code
        else:
            self.code = ''.join([str(i) for j in self.board for i in j])
            return self.code


    def findSpaces(self): 
        #row = [(row, col) for col in range(len(self.board[0])) for row in range(len(self.board)) if self.board[row][col] == 0]
        #return row
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)
        return False


    def checkSpace(self, num, space):
        if not self.board[space[0]][space[1]] == 0: 
            return False

        for col in self.board[space[0]]:
            if col == num:
                return False

        for row in range(len(self.board)):
            if self.board[row][space[1]] == num:
                return False

        internalBoxRow = space[0] // 3
        internalBoxCol = space[1] // 3

        for i in range(3):
            for j in range(3):
                if self.board[i + (internalBoxRow * 3)][j + (internalBoxCol * 3)] == num:
                    return False

        return True


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



    def findNumberOfSolutions(self):
            _z = 0
            _list_of_solutions = []

            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] == 0:
                        _z += 1

            for i in range(1, _z+1):
                _board_copy = copy.deepcopy(self)

                _row, _col = self.__findSpacesToFindNumberOfSolutions(_board_copy.board, i)
                _board_copy_solution = _board_copy.__solveToFindNumberOfSolutions(_row, _col)

                _list_of_solutions.append(self.boardToCode(input_board=_board_copy_solution))

            return list(set(_list_of_solutions))


    def findSpacesToFindNumberOfSolutions(self, board, h):
        _k = 1
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 0:
                    if _k == h:
                        return (row, col)
                    _k += 1
        return False


    def solveToFindNumberOfSolutions(self, row, col): 
        for n in range(1, 10):
            if self.checkSpace(n, (row, col)):
                self.board[row][col] = n

                if self.solve():
                    return self.board

                self.board[row][col] = 0

        return False


    def resetBoard(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        return self.board



