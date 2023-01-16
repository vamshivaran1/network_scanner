# Network Scanner


This is a basic network mapper written in Python that allows you to scan for alive hosts on your local network.

Requirements
Python 3
The os and socket modules
Usage
Clone the repository to your local machine.
Open the command line and navigate to the directory where the script is located.
Run the script using the command python network_mapper.py
The script will print your hostname, IP address, and a list of alive hosts on your local network.
Features
get_ip() function: gets the local IP address of the machine running the script.
get_hostname() function: gets the hostname of the machine running the script.
scan_network(ip_range) function: takes in an IP range (in the format of a string) and uses the ping command to check if hosts are alive. It then appends any alive hosts to a list and returns the list.
Note
By default, the script will scan for hosts on the same network as the machine running the script. You can change this by modifying the ip_range variable in the main function.
The script uses the ping command to check for alive hosts, which may not work on all operating systems.
This script is for educational purpose only, you may want to check your company or network security policy before run it.
