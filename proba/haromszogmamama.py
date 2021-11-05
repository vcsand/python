class pont:
	def __init__(self, a, b):
		self.x = a
		self.y = b
	def tavolsag(self, pont):
		return math.sqrt((self.x - pont.x)**2 + (self.y - pont.y)**2)
class haromszog:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	def kerulet(self):
		return self.a.tavolsag(self.b) + self.b.tavolsag(self.c) + self.c.tavolsag(self.a)
	def istriangle(self):
		if a > (b + c) or b > (a + c) or c > (a + b):
			return False
		else:
			return True
try:
	x1 = input("x1: ")
	y1 = input("y1: ")

	x2 = input("x2: ")
	y2 = input("y2: ")

	x3 = input("x3: ")
	y3 = input("y3: ")
except:
	print("Szamot adj meg!")
