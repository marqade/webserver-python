from http.server import HTTPServer , BaseHTTPRequestHandler
import time


hostname = "localhost"
serverport = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path , "utf-8"))
        self.wfile.write(bytes("<title>GlytchX</title>" , "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("</body></html>" , "utf-8"))
    
if __name__ == "__main__":
    webserver = HTTPServer((hostname, serverport),MyServer)
    print("Server started http://%s:%s" % (hostname, serverport))
    
    try:
        webserver.serve_forever()
        
        
    except KeyboardInterrupt:
        pass   
    
    webserver.serve_close()
    print("Server closed.")
