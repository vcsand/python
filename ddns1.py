import requests
import show_json_ddns as show
import json
h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}
newddns = {'id': '4', 'nev': 'tesomssz', 'ip': '192.168.1.124', 'datum': '2013.12.01 12:12:23'}
try:
	#reply = requests.delete('http://localhost:3000/cars/3')
	reply = requests.post('http://localhost:3000/ddns', headers = h_content, data = json.dumps(newddns))
	#print("status_code=" + str(reply.status_code))
	reply = requests.get('http://localhost:3000/ddns', headers = h_close)
except Except as e:
	print("Hiba: ", e)
	exit()
show.show(reply.json())
