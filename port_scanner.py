#!/usr/bin/env python3

import sys
import socket
import threading
import time

usage = "python3 port_scanner.py TARGET START PORT END_PORT"
start_time = time.time()

if (len(sys.argv) != 4):
	print(usage)
	sys.exit()

try:
	target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
	print("Name resolution error")
	sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target:", target)

def scan_port(port):
	#print("Scanning target:", target)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5)
	conn = s.connect_ex((target, port))
	if(not conn):	 
		print("Port {} is OPEN".format(port))
	s.close()

for port in range(start_port,end_port+1):
	thread = threading.Thread(target = scan_port, args = (port,))
	thread.start()

end_time = time.time()
print("time: ",end_time-start_time,"sec")