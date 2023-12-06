import struct
import snap7

client = snap7.client.Client()
client.connect("192.168.1.202", 0, 0, 102)
print(client.get_connected())
print("====================")

reading = client.db_read(1, 0, 224)
print(reading)

vi_tri_1 = snap7.util.get_int(reading, 0)
vi_tri_2 = snap7.util.get_int(reading, 2)
vi_tri_3 = snap7.util.get_int(reading, 4)
vi_tri_4 = snap7.util.get_int(reading, 6)
vi_tri_5 = snap7.util.get_int(reading, 8)
vi_tri_6 = snap7.util.get_int(reading, 10)
vi_tri_7 = snap7.util.get_int(reading, 12)
vi_tri_8 = snap7.util.get_int(reading, 14)
vi_tri_9 = snap7.util.get_int(reading, 16)
vi_tri_10 = snap7.util.get_int(reading, 18)
vi_tri_11 = snap7.util.get_int(reading, 20)
vi_tri_12 = snap7.util.get_int(reading, 22)
vi_tri_13 = snap7.util.get_int(reading, 24)
vi_tri_14 = snap7.util.get_int(reading, 26)
vi_tri_15 = snap7.util.get_int(reading, 28)
vi_tri_16 = snap7.util.get_int(reading, 30)


CongSua_1 = snap7.util.get_real(reading, 160)
CongSua_2 = snap7.util.get_real(reading, 164)
CongSua_3 = snap7.util.get_real(reading, 168)
CongSua_4 = snap7.util.get_real(reading, 172)
CongSua_5 = snap7.util.get_real(reading, 176)
CongSua_6 = snap7.util.get_real(reading, 180)
CongSua_7 = snap7.util.get_real(reading, 184)
CongSua_8 = snap7.util.get_real(reading, 188)
CongSua_9 = snap7.util.get_real(reading, 182)
CongSua_10 = snap7.util.get_real(reading, 196)
CongSua_11 = snap7.util.get_real(reading, 200)
CongSua_12 = snap7.util.get_real(reading, 204)
CongSua_13 = snap7.util.get_real(reading, 208)
CongSua_14 = snap7.util.get_real(reading, 212)
CongSua_15 = snap7.util.get_real(reading, 216)
CongSua_16 = snap7.util.get_real(reading, 220)
print(CongSua_6)

# def set_int(bytearray_: bytearray, byte_index: int, _int: int):
#     _int = int(_int)
#     _bytes = struct.unpack('2B', struct.pack('>h', _int))
#     bytearray_[byte_index:byte_index + 2] = _bytes
#     return bytearray_

# def get_int(bytearray_: bytearray, byte_index: int):
#     data = bytearray_[byte_index:byte_index + 2]
#     data[1] = data[1] & 0xff
#     data[0] = data[0] & 0xff
#     packed = struct.pack('2B', *data)
#     value = struct.unpack('>h', packed)[0]
#     return value

# def WriteBool(db_number, start_offset, bit_offset, value):
#     reading = client.db_read(db_number, start_offset, 1)
#     snap7.util.set_bool(reading,0,bit_offset,value)
#     client.db_write(db_number,start_offset,reading)


# def WriteInt(Start_offset, length, data):
#     # plc.mb_write(Start_offset, length, bytearray(struct.pack('>f', data)))
#     client.mb_write(Start_offset, length, bytearray(struct.pack('>f', data)))

# # Đọc cả thanh ghi
# reading = client.db_read(1, 0, 220)
# print(reading)
# # Tạo vòng lặp để set giá trị cho từng giá trị cho mỗi thanh ghi
# for i in range(0, 28):
#     set_int(reading, 4, 30) # set giá trị 30 cho vị trí 4 trong thanh ghi
#     set_int(reading, 8, 60) # set giá trị 60 cho vị trí 8 trong thanh ghi
#     # set_int(reading, i * 2, i)
#     print(i)
# client.db_write(2, 0, reading) # Sau khi set xong hết toàn bộ giá tri cho thanh ghi. Một lần ghi và gửi toàn bộ nó lên cho PLC

# # Để lấy từng giá trị trong thanh ghi ==> Sử dụng luôn get_int
# x = get_int(reading, 6)
# print(x)