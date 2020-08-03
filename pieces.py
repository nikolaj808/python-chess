class Piece():
	def __init__(self, name, team):
		self.name = name
		self.getTeam(team)
	def __str__(self):
		return '{} {}'.format(self.team, self.name)

	def getTeam(self, team):
		if team == 1:
			self.team = 'White'
		else:
			self.team = 'Black'

	def move(self, pos):
		raise NotImplementedError()

class Pawn(Piece):
	def __init__(self, team):
		super().__init__(name='Pawn', team=team)

class Knight(Piece):
	def __init__(self, team):
		super().__init__(name='Knight', team=team)

class Bishop(Piece):
	def __init__(self, team):
		super().__init__(name='Bishop', team=team)

class Rook(Piece):
	def __init__(self, team):
		super().__init__(name='Rook', team=team)

class King(Piece):
	def __init__(self, team):
		super().__init__(name='King', team=team)

class Queen(Piece):
	def __init__(self, team):
		super().__init__(name='Queen', team=team)