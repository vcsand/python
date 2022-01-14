import requests
url = "https://postman-echo.com/basic-auth"
try:
	reply = requests.get(url, auth=("postman", "password"))
except:
	print("Hiba!")
	exit()
print(reply.status_code)
print(reply.text)
