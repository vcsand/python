import requests
import show_json_cars as show
try:
	reply = requests.get('http://localhost:3000/cars?_sort=production_year')
except:
	print("Hiba!")
	exit()
show.show(reply.json())
