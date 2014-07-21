import socket
import sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create server socket (IPv4, stream = TCP protocol)
    
    host = 'localhost'
    port = 8000
    try:
        s.bind((host, port)) # bind to host 'localhost', port 8000, on this machine
        print "Socket bind complete -- host " + host + ", port: " + str(port)
    except socket.error, msg:
        print "Could not bind socket."
        print "Error message: " + msg[1]
        sys.exit(1)
        
    s.listen(5) # up to 5 connect requests (waiting to connect)
    print "Listening..."
    
    while 1:
        client, address = s.accept() # client = new socket object to communicate with connection
        print "Connected to " + address[0] + ":" + str(address[1])
        
        data = client.recv(1024) # arg is max num bytes to receive
        
        reply = 'OK...' + data
        
        if not data:
            break
        print "Got data: " + data
        client.sendall(reply) # send data back to client (sendall sends all available data, unlike send)
        
    client.close()
    s.close()

if __name__ == "__main__":
	main()
