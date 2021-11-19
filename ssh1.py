from netmiko import ConnectHandler
from getpass import getpass

#cisco1 = {"device_type": "cisco_ios", "host": "172.19.0.2", "username": "admin", "password": "admin1234"}
cisco2 = {"device_type": "cisco_ios", "host": "172.17.0.100", "username": "admin", "password": "admin1234"}
nc = ConnectHandler(**cisco1)
nc = ConnectHandler(**cisco2)
#with ConnectHandler(**cisco1) as nc:
#	print(nc.send_config_set(["hostname R1"]))
#print(nc.send_command("sh ip int br"))
print(nc.find_prompt(cisco1))
print(nc.find_prompt(cisco2))
nc.disconnect()
