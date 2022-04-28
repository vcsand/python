import os, requests
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get('API_KEY')
url = "http://docker.lan:8888/upload"
most = datetime.now()
d = {"date":most, "type":"hofok", "value":"17", "token":token}
n = 0
while True:
	try:
		reply = requests.post(url, d)
	except:
		print("Hiba!")
		exit()
	#print(reply.status_code)
	if reply.status_code!=200:
		break
	else:
		print(".", end="")
	n+=1
	sleep(2)
print(f"{n} sort feltoltotte")
