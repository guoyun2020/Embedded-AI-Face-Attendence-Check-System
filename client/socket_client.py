import socket
import os
import sys
import struct
import numpy
import cv2
from PyQt5.QtGui import QFont

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 15]

def sock_client(src, info):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.5.103', 2000))
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))

    def recvall(sock, count):
        buf = b''  # buf是一个byte类型
        while count:
            # 接受TCP套接字的数据。数据以字符串形式返回，count指定要接收的最大数据量.
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

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

        length = recvall(s, 16)  # 获得图片文件的长度,16代表获取长度
        stringData = recvall(s, int(length))  # 根据获得的文件长度，获取图片文件
        data = numpy.frombuffer(stringData, numpy.uint8)  # 将获取到的字符流数据转换成1维数组
        decimg = cv2.imdecode(data, cv2.IMREAD_COLOR)  # 将数组解码成图像
        data1 = s.recv(1024)
        recv_data1 = data1.decode('utf-8')
        data2 = s.recv(1024)
        recv_data2 = data2.decode('utf-8')
        data3 = s.recv(1024)
        recv_data3 = data3.decode('utf-8')
        data4 = s.recv(1024)
        recv_data4 = data4.decode('utf-8')

        info.setText('姓名：'+recv_data1+'\n'+'\n'+'学号：'+recv_data2+'\n'+'\n'+'班级：'+recv_data3+'\n'+'\n'+'专业：'+recv_data4+'\n')
        info.setFont(QFont("微软雅黑", 10, QFont.Bold))
            # return recv_data
        if decimg is not None:
            return decimg




