class cica():
	def __init__(self):
		self.alom = 0
	def szuletes(self):
		self.alom += 1

class sziami(cica):
	def __init__(self):
		cica.__init__(self)
		self.nevek = []
	def ujnev(self, nev):
	self.nevek.append(nev)

c = cica()
m = cica()

c.szuletes()

print(c.alom)
print(m.alom)

sz = sziami()
print(sz.__dict__)
