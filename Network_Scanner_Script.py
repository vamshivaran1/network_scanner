import os
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def scan_network(ip_range):
    alive_hosts = []
    for i in range(1, 255):
        ip = ip_range + str(i)
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            alive_hosts.append(ip)
    return alive_hosts

if __name__ == "__main__":
    ip = get_ip()
    ip_range = ".".join(ip.split(".")[:-1]) + "."
    hostname = get_hostname()
    print("Hostname: " + hostname)
    print("IP: " + ip)
    print("Scanning network...")
    alive_hosts = scan_network(ip_range)
    print("Alive hosts: " + str(alive_hosts))

