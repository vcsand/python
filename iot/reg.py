import requests
url = "http://docker.lan:8888/regist"
d={"username":"csanad"}
try:
	reply = requests.post(url, data = d)
except:
	print("Hiba!")
	exit()
print(reply.status_code)
print(reply.text)
