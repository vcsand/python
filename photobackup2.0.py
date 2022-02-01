import requests
import hashlib
import os
photo = input("Adj meg egy fajlnevet: ")
url = "http://docker.lan:8420/"
pw = input("Adj meg egy jelszot ocsinasz: ")
sha512 = hashlib.sha512(pw.encode("utf8")).hexdigest()
fsize = os.path.getsize(photo)
d={"password":sha512, "filesize": fsize}
try:
	f = open(photo, 'rb')
	reply = requests.post(url, data = d, files = {"upfile": f})
	f.close()
except:
	print("Szar van a palacsintaban.")
	exit()
print(reply)
