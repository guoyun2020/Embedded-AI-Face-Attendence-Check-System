import socket
import os
import sys
import struct
import time
import numpy
import cv2
from identification import identification
from displayInfo import displayInfo

def recv_reply():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.5.106', 2000))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print("Wait")

    def recvall(sock, count):
        buf = b''  # buf是一个byte类型
        while count:
            # 接受TCP套接字的数据。数据以字符串形式返回，count指定要接收的最大数据量.
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf
    sock, addr = s.accept()
    print('connect from:' + str(addr))

    while True:
        start = time.time()  # 用于计算帧率信息
        length = recvall(sock, 16)  # 获得图片文件的长度,16代表获取长度
        stringData = recvall(sock, int(length))  # 根据获得的文件长度，获取图片文件
        data = numpy.frombuffer(stringData, numpy.uint8)  # 将获取到的字符流数据转换成1维数组
        decimg = cv2.imdecode(data, cv2.IMREAD_COLOR)  # 将数组解码成图像
        print('识别结果:' + identification(decimg))
        displayInfo(identification(decimg))
        send_msg = identification(decimg).encode('utf-8')
        sock.send(send_msg)
        break


    sock.close()
    s.close()


