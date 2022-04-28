import requests, sys
url = "http://docker.lan:8888/fetch"
id = sys.argv[1]
d = {"id":id}
try:
	r = requests.get(url, data = d)
except e:
	print("Hiba!")
	exit()
if r.status_code == 200:
	print(r.json())
else:
	print("Nem 200.")
