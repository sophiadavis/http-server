import socket
import sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create server socket (IPv4, stream = TCP protocol)
    
    host = 'localhost'
    port = 8000
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
        print "\nConnected to " + address[0] + ":" + str(address[1])
        
        request = client.recv(10000) # arg is max num bytes to receive
        
        print "Here is the http request: "
        print request
        parsed = request.split(' ', 2)
        
        method = parsed[0]
        path = parsed[1] 
        
        response = '''HTTP/1.1 200 OK\r\n'''
        
        if not request:
            break
            
        elif path == "/":
            content_type_header = "Content-Type: text/html;\r\n\r\n"
            file = "index.html"
            
        elif path == "/style.css":
            content_type_header = "Content-Type: text/css;\r\n\r\n"
            file = "style.css"
        
        elif path == "/picture":
            content_type_header = "Content-Type: image/jpeg;\r\n\r\n"
            file = "PushkinNaBereguChernogoMoria.jpeg"
        else: 
            content_type_header = "Content-Type: text/html;\r\n\r\n"
            file = "boring.html"
            
        response += content_type_header
        data = open(file, "r")
        response += data.read()
        
        print response
        client.sendall(response) # send reply back to client (sendall sends all available data, unlike send)
        client.close() # http is connection-less, each exchange of information is a whole new session
        print "client socked closed"
    s.close()

if __name__ == "__main__":
	main()
