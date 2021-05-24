import socket
import os
import sys
import struct
import time
import numpy
import cv2
from PyQt5.QtGui import QFont

from identification import identification
from displayInfo import displayInfo
from SQLite import getInfo
from student import student
from course import course


def recv_reply(self, cour):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.5.103', 2000))
        s.listen(10)
        print("Wait")
        self.course_connect_status.setText("已连接客户端！")

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
        # print('connect from:' + str(addr))

        while True:
            length = recvall(sock, 16)  # 获得图片文件的长度,16代表获取长度
            stringData = recvall(sock, int(length))  # 根据获得的文件长度，获取图片文件
            data = numpy.frombuffer(stringData, numpy.uint8)  # 将获取到的字符流数据转换成1维数组
            decimg = cv2.imdecode(data, cv2.IMREAD_COLOR)  # 将数组解码成图像
            name_result = identification(decimg)
            stu = student(name_result, getInfo(name_result)['id'], getInfo(name_result)['class']
                          , getInfo(name_result)['major'])
            # print('识别结果:' + name_result)
            # print(getInfo(name_result))
            if name_result != 'Unknown':
                cour.sign(stu)
            self.sign_in.setText(','.join(cour.display_singIn()))
            self.sign_in.setFont(QFont("微软雅黑", 10, QFont.Bold))
            self.sign_out.setText(','.join(cour.display_singOut()))
            self.sign_out.setFont(QFont("微软雅黑", 10, QFont.Bold))
            displayInfo(identification(decimg), sock)
            name_stu = name_result.encode('utf-8')
            sock.send(name_stu)
            id_stu = str(getInfo(name_result)['id']).encode('utf-8')
            sock.send(id_stu)
            class_stu = str(getInfo(name_result)['class']).encode('utf-8')
            sock.send(class_stu)
            major_stu = getInfo(name_result)['major'].encode('utf-8')
            sock.send(major_stu)
            break

        sock.close()
        s.close()
    except socket.error as msg:
        print(msg)


