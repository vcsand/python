#!/usr/bin/env python3

x = int(input("Add meg az elso oldalt: "))
y = int(input("Add meg a masodik oldalt: "))
z = int(input("Add meg a harmadik oldalt: "))

def is_a_triangle(a, b, c):
	return a + b >= c and a + c >= b and b + c >= a
print(is_a_triangle(x,y,z)
