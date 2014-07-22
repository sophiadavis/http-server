import socket
import sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket (IPv4, 'stream' means TCP protocol)
    
    host = 'localhost'
    port = 8000
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port)) # Bind to host 'localhost', port 8000
        print "Socket bind complete -- host " + host + ", port: " + str(port)
    
    except socket.error, msg:
        print "Could not bind socket."
        print "Error message: " + msg[1]
        sys.exit(1)
        
    s.listen(5) # Up to 5 connect requests can be waiting
    print "Listening..."
    
    while 1:
        client, address = s.accept() # A new 'client' socket now connected to the server socket
        print "\nConnected to " + address[0] + ":" + str(address[1])
        
        request = client.recv(10000) # Specify max num bytes to receive
        
        print "Here is the client's http request: "
        print request
        parsed = request.split(' ', 2)
        
        method = parsed[0] # Not really necessary -- I'm assuming all methods are "GET"
        path = parsed[1] 
        
        ## Formulate http corresponding response
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
        
        else: # I guess this would technically be a 404...
            content_type_header = "Content-Type: text/html;\r\n\r\n"
            file = "boring.html"
            
        response += content_type_header
        data = open(file, "r")
        response += data.read()
        
        print "Sending http response: "
        print response
        
        client.sendall(response) # Send reply back to client (.sendall() sends all available data, .send() sends in increments)
        client.close() # http is a stateless protocol, so each exchange of information represents a whole new session
        print "Client socked closed."
    s.close()

if __name__ == "__main__":
	main()
