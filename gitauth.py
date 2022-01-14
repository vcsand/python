import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

try:
	reply = requests.get("https://api.github.com/vcsand", auth=HTTPBasicAuth("vcsand", getpass()))
except:
	print("Hiba.")
	exit()
print(reply)
