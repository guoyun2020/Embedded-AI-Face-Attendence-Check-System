import socket
import os
import sys
import struct


def sock_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.5.103', 2000))
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))

    while True:
        filepath = './detection_result.jpg'
        fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(filepath).st_size)
        s.send(fhead)
        print('client filepath: {0}'.format(filepath))

        fp = open(filepath, 'rb')
        while 1:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(filepath))
                break
            s.send(data)
        data=s.recv(1024)
        print('签到成功:', data.decode('utf-8'))  # 输出我接收的信息
        break

