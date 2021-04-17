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
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            min_dis = 10000.0  # 初始化为最大值
            name = known_face_names[0]
            # See if the face is a match for the known face(s)
            name = "Unknown"
            for i in range(len(all_known_face_encodings)):
                # name = "Unknown"
                face_dis = face_recognition.face_distance(all_known_face_encodings[i], face_encoding)
                # If a match was found in known_face_encodings, just use the first one.
                # min_dis = min(np.mean(face_dis),min_dis)
                if face_dis.shape[0] != 0:
                    face_mean = np.mean(face_dis)
                    if face_mean != 0 and face_mean < min_dis:
                        min_dis = face_mean
                        name = known_face_names[i]

            if min_dis > 0.63:  # 阈值可调
                name = "unknow"
            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # font = ImageFont.truetype(r'C:\Windows\Fonts\simfang.ttf',40)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

        # print(name)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    cv2.waitKey(10)
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
