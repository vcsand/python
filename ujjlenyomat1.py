import hashlib, bcrypt

jelszo = input("Jelszo: ")
#sha = hashlib.sha512(jelszo.encode("utf8")).hexdigest()
#print(sha)
so = bcrypt.gensalt()
bcr = bcrypt.hashpw(jelszo.encode("utf8"), so)
print(bcr)
reply = bcrypt.checkpw(jelszo.encode("utf8"), bcr)

jelszo2 = input("Add meg megegyszer: ")
reply2 = bcrypt.checkpw(jelszo2.encode("utf8"), bcr)

if reply2:
	print("Szep munka katona!")
else:
	print("Hiba!")
