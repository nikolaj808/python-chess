from pieces import *

class Board():
	def __init__(self):
		self.board = {}
		self.createBoard()
		self.setup()

	def createBoard(self):
		for j in range(8):
			for i in range(8):
				self.board['{}{}'.format(chr(97+i), j+1)] = ''

	def printBoard(self):
		for k in self.board:
			print(k, '->', self.board[k])

	def move(self, pos):
		if self.board[pos] == '':
			print('Move is legal')
		else:
			print('Position is occupied by', self.board[pos])

	def insertPiece(self, piece, pos):
		self.board[pos] = piece

	def setup(self):
		# White pieces
		self.insertPiece(Rook(1), 'a1')
		self.insertPiece(Rook(1), 'h1')
		self.insertPiece(Knight(1), 'b1')
		self.insertPiece(Knight(1), 'g1')
		self.insertPiece(Bishop(1), 'c1')
		self.insertPiece(Bishop(1), 'f1')
		self.insertPiece(Queen(1), 'd1')
		self.insertPiece(King(1), 'e1')

		self.insertPiece(Pawn(1), 'a2')
		self.insertPiece(Pawn(1), 'b2')
		self.insertPiece(Pawn(1), 'c2')
		self.insertPiece(Pawn(1), 'd2')
		self.insertPiece(Pawn(1), 'e2')
		self.insertPiece(Pawn(1), 'f2')
		self.insertPiece(Pawn(1), 'g2')
		self.insertPiece(Pawn(1), 'h2')

		# Black pieces
		self.insertPiece(Rook(2), 'a8')
		self.insertPiece(Rook(2), 'h8')
		self.insertPiece(Knight(2), 'b8')
		self.insertPiece(Knight(2), 'g8')
		self.insertPiece(Bishop(2), 'c8')
		self.insertPiece(Bishop(2), 'f8')
		self.insertPiece(Queen(2), 'd8')
		self.insertPiece(King(2), 'e8')

		self.insertPiece(Pawn(2), 'a7')
		self.insertPiece(Pawn(2), 'b7')
		self.insertPiece(Pawn(2), 'c7')
		self.insertPiece(Pawn(2), 'd7')
		self.insertPiece(Pawn(2), 'e7')
		self.insertPiece(Pawn(2), 'f7')
		self.insertPiece(Pawn(2), 'g7')
		self.insertPiece(Pawn(2), 'h7')
