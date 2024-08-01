class	HangmanState:
	SHOW = {
		"0": 
'''
 +----+
 |    |
 |
 |
 |
==============
''',
		"1": 
'''
 +----+
 |    |
 |    O
 |
 |
==============
''',
		"2": 
'''
 +----+
 |    |
 |    O
 |    |
 |
==============
''',
		"3": 
'''
 +----+
 |    |
 |    O
 |   /|
 |
==============
''',
		"4": 
'''
 +----+
 |    |
 |    O
 |   /|\\
 |
==============
''',
		"5": 
'''
 +----+
 |    |
 |    O
 |   /|\\
 |   /
==============
''',
		"6": 
'''
 +----+
 |    |
 |    O
 |   /|\\
 |   / \\
==============
''',
	}

	def __init__(self):
		self.state = 0

	def show(self):
		print(HangmanState.SHOW[str(self.state)])

	def nextState(self):
		self.state += 1
	
	def getState(self):
		return (self.state)
	