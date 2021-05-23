import cv2
import numpy as np

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 15]


def displayInfo(name, s):
    if name != "Unknown":
        path = "./img/" + name + ".png"
        # print(path)
        img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
        img = cv2.resize(img, (200, 280), cv2.INTER_AREA)
        while True:
            result, imgencode = cv2.imencode('.jpg', img, encode_param)
            # 建立矩阵
            data = np.array(imgencode)
            # 将numpy矩阵转换成字符形式，以便在网络中传输
            stringData = data.tostring()

            # 先发送要发送的数据的长度
            # ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串
            s.send(str.encode(str(len(stringData)).ljust(16)))
            # 发送数据
            s.send(stringData)
            break
        #
        # text = "Sign in successfully!"
        # cv2.putText(img, text, (40, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
        # cv2.imshow("img", img)
        # cv2.waitKey(10)
    else:
        path = "./img/" + name + ".png"
        # print(path)
        img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
        img = cv2.resize(img, (200, 280), cv2.INTER_AREA)
        while True:
            result, imgencode = cv2.imencode('.jpg', img, encode_param)
            # 建立矩阵
            data = np.array(imgencode)
            # 将numpy矩阵转换成字符形式，以便在网络中传输
            stringData = data.tostring()

            # 先发送要发送的数据的长度
            # ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串
            s.send(str.encode(str(len(stringData)).ljust(16)))
            # 发送数据
            s.send(stringData)
            break
        # cv2.imshow("img", img)
        # cv2.waitKey(10)
        # cv2.destroyAllWindows()
