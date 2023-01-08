
import socket
import time

# 创建一个 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
s.connect(('192.168.50.42', 60212))
print("Tcp connect success");
# 发送数据

send_data = 0x11223344

data = []

data.append((send_data) & 0xFF)
data.append((send_data >> 8) & 0xFF)
data.append((send_data >> 16) & 0xFF)
data.append((send_data >> 24) & 0xFF)

for i in range(1,10):
    s.send(bytes(data))
    time.sleep(1)

# # 接收数据
# data = s.recv(1024)

# 关闭 socket
s.close()

print("Tcp data send end")