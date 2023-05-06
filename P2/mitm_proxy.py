import http.server
#from msilib.schema import File
import urllib.request
import socketserver
import sys

if len(sys.argv) < 3:
    print('Usage: python3 mitm.py <port> <payload file>')
    exit(1)

#File f = read_file(sys.argv[2])
class MaliciousProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print('[*] Got request for: {}'.format(self.path))
        # Your code will go here
        self.send_response(200)
        self.end_headers()
        #self.wfile.write(sys.argv[2])
        f = open(sys.argv[2])
        for lin in f:
                linstr = lin.strip()
                b  =  bytes(linstr,'utf-8')
                self.wfile.write(b)
        #url = urllib.request.urlopen(self ) 
        #url + sys.argv[2]
        #print(sys.argv[2])


port = int(sys.argv[1])
server = socketserver.ThreadingTCPServer(('', port), MaliciousProxy)
print("[*] Serving on port {}".format(port))
server.serve_forever()