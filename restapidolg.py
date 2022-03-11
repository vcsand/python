import requests
url = "https://172.16.0.10:5000/csanad"
#proxy = {'https:': "https://localhost:8080"}
try:
	reply = requests.get(url, auth=("csanad", "kakukk"))
except:
	print("Hiba!")
	exit()
print(reply.status_code)
print(reply.text)
