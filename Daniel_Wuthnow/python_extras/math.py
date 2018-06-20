class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self):
		self.result = 0
	def add(self, *a):
		for i in a:
			print type(i)
			print i
			if type(i) == int:
				self.result += i
			else:
				for x in i:
					self.result += x
		return self

	def sub(self, *a):
		for i in a:
			if type(i) == int:
				self.result -= i
			else:
				for x in i:
					self.result -= x
		return self
	def total(self):
		print self.result


md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4,3,1]).sub((2,3), [2,3], [1.1,2,3]).total()