from netmiko import ConnectHandler
CSR = {
    'device_type': 'cisco_ios',
    'ip': '172.17.0.100',
    'username': 'admin',
    'password': 'admin1234'
}
net_connect = ConnectHandler(**CSR)
hostname = net_connect.send_command('show run | i host')
device = hostname.split(" ")
print ("Biztonsagi mentes keszitese a kovetkezo eszkozon: " + device[1])
#filename = '/home/konyvadmin/backups/' + device + '.txt'
filename = device[1] + '.txt'
showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
log_file.close()
net_connect.disconnect()
