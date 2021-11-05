#!/usr/bin/env python3

def myint(val):
	eredmeny = 0
	for i in val:
		vizsgal=ord(i)
		if vizsgal >= 48 and vizsgal <= 57:
			eredmeny = eredmeny * 10 + vizsgal - 48
		else:
			break
	return eredmeny
#	for i in eredmeny:
#		vmi = ord(i)
#		if(vmi > 58 and vmi < 47):
#			del i
szam = input("Adj meg egy szamot: ")
try:
	assert len(szam) >= 1 and len(szam) <= 10
except:
	print("Tul hosszu!")
	exit()
print(myint(szam))
