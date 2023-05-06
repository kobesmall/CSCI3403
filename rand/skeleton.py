import base64
import sys

if len(sys.argv) != 3:
    print("Usage : python3 dict_gen.py <username_file> <password_file>")
    exit()

username_file = sys.argv[1]
password_file = sys.argv[2]

with open(username_file, 'r') as f:
    username_raw = f.read()

with open(password_file, 'r') as f:
    password_raw = f.read()

username_li = username_raw.split('\n')
password_li = password_raw.split('\n')

unp_li = []
dict_list = []
c = 0
for i in username_li:
    for j in password_li:
        str= i+ ":"+ j
        msgbytes=str.encode('ascii')
        code= base64.b64encode(msgbytes)
        dict_list.append(code)
        
          # Your code here!! Make this code generate base64 value of 'username:password'

with open('dict.list', 'wb') as f:
    for d in dict_list:
        f.write(d)
        f.write(b'\n')

print("DONE!!")
