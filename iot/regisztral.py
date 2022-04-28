import requests, json

url = "http://docker.lan:8888/regist"
d = {"username": "csanad"}
try:
	r = requests.post(url,data=d)
except:
	print("Halozati hiba!")
	exit()
print(r.status_code)
j = json.loads(r.json())
token = j["token"]
print(token)
with open(".env", "wt") as f:
	f.write(f"API_KEY = {token}")
