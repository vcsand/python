#!/usr/bin/env python3

szoveg = input("Irj be valami szoveget: ")
try:
	eltolas = int(input("Adj meg egy szamot 1-25 kozott: "))
	assert eltolas >= 1 and eltolas <= 25
except:
	print("Nem jo erteket adtal meg!")
	exit()

for i in szoveg:
	kod = ord(i)
	if kod >= 97 and kod <= 122:
		kod += eltolas
		if kod > 122:
			kod -= 25
		print(chr(kod), end = "")
	elif kod >= 65 and kod <= 90:
		kod += eltolas
		if kod > 90:
			kod -= 25
		print(chr(kod), end = "")
	else:
		print(ord(kod), end="")
print("")
