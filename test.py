class A():
	def __init__(self):
		self.data = 1

	def good(self):
		print('good A')

class B():
	def __init__(self):
		self.data = 2

	def good(self):
		print('good B')


def poly(obj):
	obj.good()

poly(A())
poly(B())