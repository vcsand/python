import requests
import show_json_cars as show
headers = {'Connection': 'Close'}
try:
	reply = requests.delete('http://localhost:3000/cars/3')
	print("status_code=" + str(reply.status_code))
	reply = requests.get('http://localhost:3000/cars')
except:
	print("Hiba!")
	exit()
show.show(reply.json())
