# This script runs on Python 3
import socket, threading
import ifaddr
from scapy.all import ARP, Ether, srp


def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''


def scan_ports(host_ip, port):

	output = {}         # For printing purposes

	print("Scanning Port:{}".format(port))

	TCP_connect(host_ip, port, 1, output)

	print(output)

def main():
	host_ip = "127.0.0.1" #input("Enter host IP: ")
	port = 8085 #int(input("Port to Scan: "))   
	scan_ports(host_ip, port)



	target_ip = "169.254.39.193/16"
	# IP Address for the destination
	# create ARP packet
	arp = ARP(pdst=target_ip)
	# create the Ether broadcast packet
	# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
	ether = Ether(dst="ff:ff:ff:ff:ff:ff")
	# stack them
	packet = ether/arp

	result = srp(packet, timeout=3, verbose=0)[0]

	# a list of clients, we will fill this in the upcoming loop
	clients = []

	for sent, received in result:
	    # for each response, append ip and mac address to `clients` list
		clients.append({'ip': received.psrc, 'mac': received.hwsrc})

	# print clients
	print("Available devices in the network:")
	print("IP" + " "*18+"MAC")
	for client in clients:
		print("{:16}    {}".format(client['ip'], client['mac']))




if __name__ == "__main__":
	main()