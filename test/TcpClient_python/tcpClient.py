# '''
# Author: emmovo
# Date: 2023-01-08 21:38:06
# LastEditors: emmovo
# LastEditTime: 2023-01-09 20:18:53
# FilePath: \undefinedd:\Git\QtChartTCP\QtChartTCP\test\TcpClient_python\tcpClient.py
# Description: 

# Copyright (c) 2023 by mingjkl@live.com/emmovo.com, All Rights Reserved. 
# '''

import socket
import time
import math

pi = 3.1415926
vol = 3300

# 创建一个 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
s.connect(('192.168.50.42', 60212))
print("Tcp connect success");
# 发送数据



send_data = 0x11223344

data = []


for i in range(1,360):

    vol_value = int(vol * math.sin(i * pi / 180))

    data.append(0x55)
    data.append(0xAA)
    data.append((vol_value >> 24) & 0xFF)
    data.append((vol_value >> 16) & 0xFF)
    data.append((vol_value >> 8) & 0xFF)
    data.append((vol_value >> 0) & 0xFF)
    data.append(0x0D)
    data.append(0x0A)

    s.send(bytes(data))

    data.clear();

    time.sleep(0.1)

# # 接收数据
# data = s.recv(1024)

# 关闭 socket
s.close()

print("Tcp data send end")