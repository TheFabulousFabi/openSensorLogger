import socket
import netifaces





def get_ip():
	IP = ""
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1'
	finally:
		s.close()

	return IP


def get_mask():
    for i in netifaces.interfaces():
        try:
            # Address
            print("IP Address: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
            print("Mask: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
            print("Gateway: ", netifaces.gateways()['default'][netifaces.AF_INET][0])

        except:pass


print(get_ip())	
print(get_mask())