try:
	f = open(input("Add meg a fajl nevet: "), 'wt')
except:
	print ("Hiba a fajl megnyitasa kozben")
	exit()
line = input("Irjal: ")
while line:
	i = 0
	szoveg = ""
	for c in line:
		if i == 0:
			szoveg += c.upper()
		else:
			szoveg += c
		i += 1
	f.write(szoveg)
	f.write("\n")
	line = input ("Irjal: ")
