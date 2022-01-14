import requests
import show_json_cars as show
import json
h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}
newcars = {'id': '4', 'brand': 'Maserati', 'model': 'Columbia', 'production_year': '1970', 'convertible': 'false'}
try:
	reply = requests.put('http://localhost:3000/cars', headers = h_content, data = json.dumps(newcars))
	reply = requests.get('http://localhost:3000/cars', headers = h_close)
except Except as e:
	print("Hiba: ", e)
	exit()
show.show(reply.json())
