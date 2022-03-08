from Board import Board
import random
import copy

class Generator(Board):
    def __init__(self, difficulty):
        self.difficulty = difficulty
    
    def generateQuestionBoardCode(self): 
        self.board, _solution_board = self.generateQuestionBoard(self.generateRandomCompleteBoard())
        return self.boardToCode(), self.boardToCode(_solution_board)
    
    def generateQuestionBoard(self, fullBoard):
        self.board = copy.deepcopy(fullBoard)

        if self.difficulty == 0:
            _squares_to_remove = 36
        elif self.difficulty == 1:
            _squares_to_remove = 46
        elif self.difficulty == 2:
            _squares_to_remove = 52
        else:
            return

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(0, 2)
            _rCol = random.randint(0, 2)
            if self.board[_rRow][_rCol] != 0:
                self.board[_rRow][_rCol] = 0
                _counter += 1

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(3, 5)
            _rCol = random.randint(3, 5)
            if self.board[_rRow][_rCol] != 0:
                self.board[_rRow][_rCol] = 0
                _counter += 1

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(6, 8)
            _rCol = random.randint(6, 8)
            if self.board[_rRow][_rCol] != 0:
                self.board[_rRow][_rCol] = 0
                _counter += 1

        _squares_to_remove -= 12
        _counter = 0
        while _counter < _squares_to_remove:
            _row = random.randint(0, 8)
            _col = random.randint(0, 8)

            if self.board[_row][_col] != 0:
                n = self.board[_row][_col]
                self.board[_row][_col] = 0

                if len(self.findNumberOfSolutions()) != 1:
                    self.board[_row][_col] = n
                    continue

                _counter += 1

        return self.board, fullBoard

    def generateRandomCompleteBoard(self):
            self.resetBoard()
            _l = list(range(1, 10))
            for row in range(3):
                for col in range(3):
                    _num = random.choice(_l)
                    self.board[row][col] = _num
                    _l.remove(_num)

            _l = list(range(1, 10))
            for row in range(3, 6):
                for col in range(3, 6):
                    _num = random.choice(_l)
                    self.board[row][col] = _num
                    _l.remove(_num)

            _l = list(range(1, 10))
            for row in range(6, 9):
                for col in range(6, 9):
                    _num = random.choice(_l)
                    self.board[row][col] = _num
                    _l.remove(_num)

            return self.generateCont()
        
    def findNumberOfSolutions(self):
        _z = 0
        _list_of_solutions = []

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    _z += 1

        for i in range(1, _z+1):
            _board_copy = copy.deepcopy(self)

            _row, _col = self.findSpacesToFindNumberOfSolutions(_board_copy.board, i)
            _board_copy_solution = _board_copy.solveToFindNumberOfSolutions(_row, _col)

            _list_of_solutions.append(self.boardToCode(input_board=_board_copy_solution))

        return list(set(_list_of_solutions))
    
    def generateCont(self): 
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    num = random.randint(1, 9)

                    if self.checkSpace(num, (row, col)):
                        self.board[row][col] = num

                        if self.solve():
                            self.generateCont()
                            return self.board

                        self.board[row][col] = 0

        return False