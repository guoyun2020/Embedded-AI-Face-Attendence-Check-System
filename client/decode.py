import face_recognition
import cv2
import os
import pickle
import pandas as pd

face_names = []
face_codings = []

bok = pd.read_csv('./person_name.csv')
person_list = os.listdir("face/")
# print(os.listdir("face/" + str(0)))
face_codes = []
person_codes = []
single_codes = []
for i in range(len(person_list)):
    image_num = os.listdir("face/" + str(i))
    person_codes = []
    for j in image_num:
        image_path = "face/" + str(i) + "/" + str(j)
        face_img = face_recognition.load_image_file(image_path)
        single_codes = face_recognition.face_encodings(face_img)
        if len(single_codes) != 0:
            person_codes.append(single_codes[0])
    face_codes.append(person_codes)

output = open('facedata.pkl', 'wb')
pickle.dump(face_codes, output)
output.close()
