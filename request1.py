import requests

try:
	reply = requests.get("http://localhost:3000")
	print(reply.text)
#except requests.exceptions.TooManyRedirects:
#	print("Too many redirects hiba.")
#except requests.exceptions.URLRequired:
#	print("URL required hiba.")
except requests.exceptions.InvalidURL:
	print("Invalid URL hiba")
#except requests.exceptions.Timeout:
#	print("Timeout Hiba")
except requests.exceptions.ConnectionError:
	print("Connection Error Hiba")
except:
	print("Valami mas hiba.")
else:
	print("Sikerult nincs hiba.")
#print(requests.exceptions.__dict__)
