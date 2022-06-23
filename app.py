from http.server import BaseHTTPRequestHandler, HTTPServer
import time

host_name = "localhost"
server_port = 9999

class BasicServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/success':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Success\n".encode())
        elif self.path == '/fail':
            self.send_response(430)
            self.send_header("Content-type", "text/html")
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer((host_name, server_port), BasicServer)
    print(f"Server started on http://{host_name}:{server_port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server stopped")
