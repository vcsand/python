import requests
url = "http://postman-echo.com/basic-auth"
#proxy = {'https:': "https://localhost:8080"}
try:
	reply = requests.get(url, auth=("postman", "password"))
except:
	print("Hiba!")
	exit()
print(reply.status_code)
print(reply.text)
