import requests

reply = requests.get(input("URL: "))
print(reply.text)
