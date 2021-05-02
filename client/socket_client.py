import socket
import os
import sys
import struct
import numpy
import cv2
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 15]

def sock_client(src):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.5.106', 2000))
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))

    while True:
        result, imgencode = cv2.imencode('.jpg', src, encode_param)
        # 建立矩阵
        data = numpy.array(imgencode)
        # 将numpy矩阵转换成字符形式，以便在网络中传输
        stringData = data.tostring()

        # 先发送要发送的数据的长度
        # ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串
        s.send(str.encode(str(len(stringData)).ljust(16)))
        # 发送数据
        s.send(stringData)

        data=s.recv(1024)
        recv_data = data.decode('utf-8')
        if recv_data != 'Unknown':
            print('签到成功:', recv_data)  # 输出我接收的信息
        break

