#!/usr/bin/env python3

try:
	a = int(input("Adjon meg egy szamot: "))
except:
	print("Szamot adj meg!")
	exit(0)
t2 = ["0" for i in range(a)]
print(t2)
#t = [["0"for j in range(3)] for i in range(3)]
#print(t)
