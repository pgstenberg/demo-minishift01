#!/usr/bin/python
import socket
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


PORT_NUMBER = 8080


class simpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(
            "<h1>Greatings {0} from {1}</h1>".format(
                self.client_address,
                (socket.gethostname(), PORT_NUMBER)))
        return


try:
    server = HTTPServer(('', PORT_NUMBER), simpleHandler)
    print 'Started httpserver on port ', PORT_NUMBER
    server.serve_forever()


except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
