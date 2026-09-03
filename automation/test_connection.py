from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.231.132",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco",   # enable password (ถ้ามี)
}

connection = ConnectHandler(**device)
output = connection.send_command("show version")
print(output)
connection.disconnect()