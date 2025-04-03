from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "password",
}

connection = ConnectHandler(**device)
connection.enable()

commands = [
    "interface GigabitEthernet0/1",
    "description Configured by Netmiko",
    "ip address 192.168.1.10 255.255.255.0",
    "no shutdown",
]

output = connection.send_config_set(commands)
print(output)

connection.disconnect()
