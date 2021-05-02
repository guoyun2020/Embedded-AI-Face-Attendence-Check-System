import cv2
import numpy as np


def displayInfo(name):
    if name != "Unknown":
        path = "./img/"+name + ".png"
        # print(path)
        img = cv2.imdecode(np.fromfile(path,dtype=np.uint8),-1)
        img=cv2.resize(img, (250,330), cv2.INTER_AREA)
        text = "Sign in successfully!"
        cv2.putText(img, text, (40, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
        cv2.imshow("img", img)
        cv2.waitKey(10)
    else:
        path = "./img/" + name + ".png"
        # print(path)
        img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
        img = cv2.resize(img, (250, 330), cv2.INTER_AREA)
        cv2.imshow("img", img)
        cv2.waitKey(10)
        #cv2.destroyAllWindows()


