from socket_server import recv_reply

if __name__ == '__main__':
    while True:
        recv_reply()


















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
