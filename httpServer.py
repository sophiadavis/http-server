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
        
        reply = '''HTTP/1.1 200 OK\nContent-Type: text/html;\n\n<html><head><link rel="stylesheet" type="text/css" href="style.css"></head>'''
        
        if not request:
            break
            
        # assume that method was "GET"
        elif path == '/':
            print "request for root"
#             reply += "Content-Disposition: inline; filename=index.html"
            reply += '''<body>
                            <h1>Hello, world!</h1>
                        </body>
                    </html>'''
        elif path == '/picture':
            reply += '''<body>
                            <img src="PushkinNaBereguChernogoMoria.jpeg">
                        </body>
                    </html>'''
        else: 
            reply += '''<body>boring content :(</body>'''
        print reply
        client.sendall(reply) # send reply back to client (sendall sends all available data, unlike send)
        client.close() # http is connection-less, each exchange of information is a whole new session
        print "client socked closed"
    s.close()

if __name__ == "__main__":
	main()
