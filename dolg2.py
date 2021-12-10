fajlnevv = input("Adj meg egy fajlnevet: ")
try:
	fajlnev = open(fajlnevv, 'rt')
	fajlnev2 = open(fajlnevv + "-output", 'wt')
except:
	print("Nem adtal meg fajlnevet!")
	exit()

fajl = fajlnev.readline()
i = 0
while fajl:
	sorok = ""
	if i % 2 == 1:
		sorok += fajl.upper()
	else:
		sorok += fajl.lower()
	i += 1
	print(sorok, end="")
	fajlnev2.write(sorok)
	fajl = fajlnev.readline()
fajlnev.close()
fajlnev2.close()
