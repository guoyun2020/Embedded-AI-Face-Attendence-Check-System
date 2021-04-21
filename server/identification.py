import face_recognition
import cv2
import numpy as np
import pandas as pd
import pickle


def identification(face):
    pkl_file = open('facedata.pkl', 'rb')
    all_known_face_encodings = pickle.load(pkl_file)
    pkl_file.close()
    know_name = pd.read_csv('./person_name.csv')
    known_face_names = list(know_name.iloc[:, 1])
    name = "Unknown"
    face_locations = face_recognition.face_locations(face)
    face_encodings = face_recognition.face_encodings(face, face_locations)
    for face_encoding in face_encodings:
        min_dis = 10000.0  # 初始化为最大值
        # See if the face is a match for the known face(s)

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
               # print(min_dis)
                if min_dis>0.45:
                    name = "Unknown"

    return name
