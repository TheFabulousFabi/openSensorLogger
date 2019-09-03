# This script runs on Python 3
import socket, threading
import ifaddr


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



if __name__ == "__main__":
	main()