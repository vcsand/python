import requests
import hashlib
url = "http://docker.lan:8420/test"
pw = input("Adj meg egy jelszot: ")
sha512 = hashlib.sha512(pw.encode("utf-8")).hexdigest()
d={"password":sha512}
try:
	reply = requests.post(url, data = d)
except:
	print("Hiba!")
	exit()
print(reply)
