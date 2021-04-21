# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os.path
import copy

# 昏暗 n
def darker(image,percetage=0.9):
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    #get darker
    for xi in range(0,w):
        for xj in range(0,h):
            image_copy[xj,xi,0] = int(image[xj,xi,0]*percetage)
            image_copy[xj,xi,1] = int(image[xj,xi,1]*percetage)
            image_copy[xj,xi,2] = int(image[xj,xi,2]*percetage)
    return image_copy

# 亮度 n
def brighter(image, percetage=1.5):
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    #get brighter
    for xi in range(0,w):
        for xj in range(0,h):
            image_copy[xj,xi,0] = np.clip(int(image[xj,xi,0]*percetage),a_max=255,a_min=0)
            image_copy[xj,xi,1] = np.clip(int(image[xj,xi,1]*percetage),a_max=255,a_min=0)
            image_copy[xj,xi,2] = np.clip(int(image[xj,xi,2]*percetage),a_max=255,a_min=0)
    return image_copy



for people in range(3,4):
    # 图片文件夹路径
    file_dir = f"C:\\Users\\Hoshino Naoki\\PycharmProjects\\face_det\\face\\{str(people)}\\"
    for img_name in os.listdir(file_dir):
        img_path = file_dir + img_name
        img = cv2.imread(img_path)

    for img_name in os.listdir(file_dir):
        img_path = file_dir + img_name
        img = cv2.imread(img_path)


        #变暗
        img_darker = darker(img)
        cv2.imwrite(file_dir + img_name[0:-4] + 'darker.jpg', img_darker)

        #变亮、
        img_brighter = brighter(img)
        cv2.imwrite(file_dir + img_name[0:-4] + 'brighter.jpg', img_brighter)

        #高斯模糊
        blur = cv2.GaussianBlur(img, (7, 7), 1.5)
        #      cv2.GaussianBlur(图像，卷积核，标准差）
        cv2.imwrite(file_dir + img_name[0:-4] + 'blur.jpg',blur)
