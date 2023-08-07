#Author: Harsh Choudhary, 2103117
'''
Nmap alternative
'''

#import needed libraries and modules
import socket
import sys			#used to take arguments from command line
import threading		#as scanning the ports serially is rather slow, so we use threading
import time			#to print time usage statistics during the scan

default_start_port=1
default_end_port=1024		#nmap scans by default for all ports between 1 and 1000 but we keep it till 1024
usage="Error: Invalid format!\nFormat: python3 port_scanner_harsh.py <ip_address_target> [start_port_no] [end_port_no]"

#usage="Error: Invalid format!\nFormat: python3 port_scanner_harsh.py <ip_address_target> [-T]/[-U] [start_port_no] [end_port_no]"

start_port=default_start_port
end_port=default_end_port

#tcp port scanning using three way handshake and thus determining if some port is open or not
#if response for tcp connection request comes then the port is open else not

#check the validity of argumnets passed from command line

arg_list=sys.argv
print(arg_list)
if(len(arg_list)<2):
	print("Warning: Target ip address missing!")
	print(usage)
	sys.exit(0)
elif(len(arg_list)==3):
	#assume start port is given and end port is not given
	start_port=int(arg_list[2])
	if(start_port<=0 or start_port>65535):
		print("Warning: Invalid start port")
		print(usage)
		sys.exit(0)
elif(len(arg_list)==4):
	#both start and end_port given
	start_port=int(arg_list[2])
	end_port=int(arg_list[3])
	if(start_port<=0 or start_port>65535 or end_port<start_port):
		print("Warning: Invalid start port or end port")
		print(usage)
		sys.exit(0)
elif(len(arg_list)>4):
	#more than 4 arguments is also illegal
	print(usage)
	sys.exit(0)

#reached here means correct input format
#ip address is in string format
target_ip=arg_list[1]

print("***************Python simple PoRt ScAnNiNg tool******************")

print("Scanning ",target_ip," from port no. ",start_port," to port no. ",end_port)

#scanning code serially is very slow, so we use threading and scan multiple ports concurrently

def port_scan(port):
	#for all i's port numbers we have to create the socket connection
	#for now default option is TCP
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		client_socket.settimeout(3)	#waits for 3s at max to receive response from any port, else times out
		con=client_socket.connect_ex((target_ip,port))	#i=port no. currently being scannned
		if(con==0):
			print("Port no. ",port," is open [tcp]")
	except 'connectionRefusedError':
		client_socket.close()
		return
	#IMPORTANT: s.connect((ip,port)) simply terminates the program if connection failed, so use the variant connection_ex
	#clinetsocket.connect_ex() returns 0 if connection was successful and 1 otherwise

	client_socket.close()	

time_start=time.time()

for i in range(start_port,end_port+1):
	thread=threading.Thread(target=port_scan, args=(i,))
	thread.start()	


time.sleep(3.5)		#set it equal to the max time out value for sockets else time usage statistics printed even before the outputs
time_end=time.time()

print("Total time elapsed is ",time_end-time_start," seconds")
	
