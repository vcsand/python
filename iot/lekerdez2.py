import os, requests
from dotenv import load_dotenv
load_dotenv()
nev = "users"
token = os.environ.get('API_KEY')
url = "http://docker.lan:8888/fetchAll"
d = {"username":"csanad", "token":token}
try:
	reply = requests.get(url, d)
except:
	print("Hiba!")
	exit()
#print(reply.status_code)
if reply.status_code == 200:
	print(reply.json())
else:
	print("Hibas token!")
