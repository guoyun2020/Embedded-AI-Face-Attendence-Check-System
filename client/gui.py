import socket
import numpy
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
import sys
import face_recognition
from socket_client import sock_client
from PyQt5 import QtCore, QtWidgets
import os
import time


class gui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initTimer()

    def initTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_pic)


    def show_pic(self):
        ret, frame = self.vc.read()
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        reimg=cv2.imread('Unknown.png')
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time

        face_locations = face_recognition.face_locations(rgb_small_frame)

        # Display the results
        for (top, right, bottom, left) in face_locations:
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            area = (right - left) * (bottom - top)

            face = frame[top:bottom, left:right]
            if face.shape[0]*face.shape[1]>28900:
                  reimg = sock_client(face, self.info)

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        if not ret:
            print('read error!\n')
            return
        self.timelabel.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'                                  当前课程：网络编程')
        self.timelabel.setFont(QFont("微软雅黑", 10, QFont.Bold))
        img = cv2.resize(frame, dsize=(491, 271))
        image_height, image_width, image_depth = img.shape  # 读取图像高宽深度
        QIm = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        QIm = QImage(QIm.data, image_width, image_height, image_width * image_depth, QImage.Format_RGB888)
        self.lbl.setPixmap(QPixmap.fromImage(QIm))
        image_height1, image_width1, image_depth1 = reimg.shape  # 读取图像高宽深度
        QIm1 = cv2.cvtColor(reimg, cv2.COLOR_BGR2RGB)
        QIm1 = QImage(QIm1.data, image_width1, image_height1, image_width1 * image_depth1, QImage.Format_RGB888)
        self.img.setPixmap(QPixmap.fromImage(QIm1))


    def openCamera(self):
        self.lbl.setEnabled(True)
        self.vc = cv2.VideoCapture(0)
        self.openCameraBtn.setEnabled(False)
        self.closeCameraBtn.setEnabled(True)
        self.timer.start(100)

    def closeCamera(self):
        self.vc.release()
        self.openCameraBtn.setEnabled(True)
        self.closeCameraBtn.setEnabled(False)
        self.QLable_close()
        self.timer.stop()

    def initUI(self):
        self.resize(530, 630)
        self.lbl = QLabel(self)
        self.lbl.setGeometry(QtCore.QRect(20, 30, 491, 271))
        self.timelabel = QLabel(self)
        self.timelabel.setGeometry(QtCore.QRect(20, 3, 491, 20))
        self.info = QLabel(self)
        self.info.setGeometry(QtCore.QRect(230, 330, 160, 280))
        self.info.setFrameShape(QtWidgets.QFrame.Box)
        self.info.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.info.setLineWidth(1)
        self.img = QLabel(self)
        self.img.setGeometry(QtCore.QRect(20, 330, 200, 280))
        self.img.setFrameShape(QtWidgets.QFrame.Box)
        self.img.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.img.setLineWidth(1)
        self.openCameraBtn = QtWidgets.QPushButton(self)
        self.openCameraBtn.setText('开机')
        self.openCameraBtn.setGeometry(QtCore.QRect(420, 330, 91, 31))
        self.openCameraBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.openCameraBtn.clicked.connect(self.openCamera)
        self.closeCameraBtn = QtWidgets.QPushButton(self)
        self.closeCameraBtn.setText('关机')
        self.closeCameraBtn.setGeometry(QtCore.QRect(420, 380, 91, 31))
        self.closeCameraBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.closeCameraBtn.clicked.connect(self.closeCamera)
        self.openCameraBtn.setEnabled(True)
        self.closeCameraBtn.setEnabled(False)
        self.QLable_close()
        self.setWindowTitle('人脸考勤系统客户端 v1.0')
        self.show()


    def QLable_close(self):
        self.lbl.setStyleSheet("background:black;")
        self.lbl.setPixmap(QPixmap())

    def start(self):
        self.timer.start(100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ex = gui()
    sys.exit(app.exec_())
