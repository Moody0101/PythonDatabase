import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as http:
    print(f"Open localhost:{PORT} in your browser and you will find everything!!")
    http.serve_forever()
