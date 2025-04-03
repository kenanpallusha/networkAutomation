import subprocess

def ping_device(ip):
    result = subprocess.run(["ping", "-c", "2", ip], stdout=subprocess.PIPE, text=True)
    if "bytes from" in result.stdout:
        print(f"{ip} is reachable")
    else:
        print(f"{ip} is unreachable")

devices = ["192.168.1.1", "8.8.8.8", "192.168.1.100"]
for device in devices:
    ping_device(device)
