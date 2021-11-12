from dvrip import DVRIPCam

host_ip = '192.168.1.115'

cam = DVRIPCam(host_ip, user='admin', password='')
print("teszt0")
if cam.login():
	print("Success! Connected to " + host_ip)
else:
	print("Failure. Could not connect.")
	exit()
print("Itt vagyok1")
params = cam.get_general_info()
#params = cam.get_system_info()
#params = cam.get_system_capabilities()
print(params)
