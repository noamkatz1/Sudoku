from Generator import Generator
from Solver import Solver

if __name__ == '__main__':
	gen = Generator(0) # get 0 for easy level, 1 for medium and 2 for hard
	question_board_code = gen.generateQuestionBoardCode()
	code = question_board_code[0]
	solution = question_board_code[1]
	solved_board_code = Solver(code,gen.board).solveForCode()
	print('Original Sudoku:',code)
	print('Solved Puzzle:',solved_board_code)
	print('Original Solution',solution)