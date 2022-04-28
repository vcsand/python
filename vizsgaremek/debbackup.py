from netmiko import ConnectHandler
CSR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'debadmin',
    'password': 'Admin123deb'
}
net_connect = ConnectHandler(**CSR)
hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
hostname,device = hostname.split(" ")
print ("Biztonsagi mentes keszitese a kovetkezo eszkozon: " + device)
filename = '/home/konyvadmin/backups/' + device + '.txt' 
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
net_connect.disconnect()
