import socket
import sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create server socket
    s.bind(('localhost', 8000)) # bind to port 8000, on this machine
    try:
        s.bind((host, port)) # bind to host 'localhost', port 8000, on this machine
        print "Socket bind complete -- host " + host + ", port: " + str(port)
    except socket.error, msg:
        print "Could not bind socket."
        print "Error message: " + msg[1]
        sys.exit(1)
        
    s.listen(5) # up to 5 connect requests (waiting to connect)
    
    while 1:
        client, address = s.accept() # client = new socket object to communicate with connection
        data = client.recv(1024) # arg is max num bytes to receive
        if data:
            client.send(data) # send data back to client
        client.close()

if __name__ == "__main__":
	main()
