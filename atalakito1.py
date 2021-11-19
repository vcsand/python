import sys

try:
	be = sys.argv[1]
except:
	print("Nincs argumentum.")
	exit()
ki = input("Adj meg egy fajl nevet: ")
if ki:
	print("Nem adtal meg fajl nevet a parancssorba!")
	exit()

try:
	b = open(be, 'rt')
	k = open(ki, 'wt')
except:
	print("HibaaaaaAAAAAAAAAAAAA")
	exit()

for line in b:
	line.lower()
	k.write(line)

b.close()
k.close()
