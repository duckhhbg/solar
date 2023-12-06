import struct
import snap7

client = snap7.client.Client()
client.connect("192.168.1.202", 0, 0, 102)
print(client.get_connected())
print("====================")



