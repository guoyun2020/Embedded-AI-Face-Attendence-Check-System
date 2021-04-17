import socket
import os
import sys
import struct


def sock_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.43.205', 2000))
    except socket.error as msg:
        print(msg)
        print(sys.exit(1))

    while True:
        filepath = 'D:\\360MoveData\\Users\\Hoshino Naoki\\Desktop\\test.jpg'
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
        s.close()
        break


if __name__ == '__main__':
    sock_client()
