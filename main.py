from http.server import HTTPServer, CGIHTTPRequestHandler

port = 80

server_object = HTTPServer(server_address=('',80), RequestHandlerClass=CGIHTTPRequestHandler)

print(f'The server is running on port {port}.')

server_object.serve_forever()