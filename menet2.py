import requests
s = requests.Session()
s.auth = ("user", "pass")
s.headers.update({"x-test":"true"})
try:
	r = s.get('https://httpbin.org/headers', headers = {'x-test2':'true'})
except:
	print("Hiba")
	exit()
print(r.text)
