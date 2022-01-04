import requests
import show_json_cars as show
try:
	reply = requests.get('http://localhost:3000/cars?_sort=production_year&_order=desc')
except:
	print("Hiba!")
	exit()
else:
	show.show(reply.json())
