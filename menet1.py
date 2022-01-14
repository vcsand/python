import requests
mm = requests.Session()
try:
	mm.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
	reply = mm.get('https://httpbin.org/cookies')
except:
	print("Hiba.")
	exit()
print(reply.text)
