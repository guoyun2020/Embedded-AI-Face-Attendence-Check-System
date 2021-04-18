# import paddlehub as hub
# import cv2
#
# vc = cv2.VideoCapture(0)
# module = hub.Module(name="pyramidbox_lite_mobile")
# while(True):
#     ret, frame = vc.read()
#     results = module.face_detection(images=[frame], use_gpu=False, visualization=False)
#     for result in results:
#         if len(result['data'])>0:
#             #print(result['data'][0]['confidence'])
#             face = frame[result['data'][0]['top']:result['data'][0]['bottom'], result['data'][0]['left']:result['data'][0]['right']]
#             cv2.rectangle(frame,(result['data'][0]['left'], result['data'][0]['top']), (result['data'][0]['right'], result['data'][0]['bottom']),(0,255,0),2)
#     cv2.imshow("face", face)
#     cv2.imshow("result", frame)
#     cv2.waitKey(10)

import face_recognition
import cv2
import numpy as np
import pandas as pd
import pickle
from socket_client import sock_client
import socket
import os
import sys
import struct
from PIL import Image, ImageFont, ImageDraw

# cv2.namedWindow('face_recognition',cv2.CAP_DSHOW)
video_capture = cv2.VideoCapture(0)

pkl_file = open('facedata.pkl', 'rb')
all_known_face_encodings = pickle.load(pkl_file)
pkl_file.close()


know_name = pd.read_csv('./person_name.csv')
known_face_names = list(know_name.iloc[:, 1])

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


while True:
    save = True
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

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
        area = (right-left)*(bottom-top)
        if area>20000 and save :
            face=frame[top:bottom,left:right]
            cv2.imwrite("./detection_result.jpg",face)
            save=False
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    sock_client()
    # Display the resulting image
    cv2.imshow('Video', frame)
    cv2.waitKey(500)

