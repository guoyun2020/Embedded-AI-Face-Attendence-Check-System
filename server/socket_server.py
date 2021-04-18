import socket
import os
import sys
import struct
from identification import identification

def recv_reply():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.5.103', 2000))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print("Wait")

    while True:
        sock, addr = s.accept()
        deal_data(sock, addr)
        send_msg = identification().encode('utf-8')
        sock.send(send_msg)
        break

    print('识别结果:' + identification())
    sock.close()
    s.close()



def deal_data(sock, addr):
    print("Accept connection from {0}".format(addr))

    while True:
        fileinfo_size = struct.calcsize('128sq')
        buf = sock.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.decode().strip('\x00')
            new_filename = os.path.join('./', 'new_' + fn)
            recvd_size = 0
            fp = open(new_filename, 'wb')

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = sock.recv(1024)
                    recvd_size += len(data)
                else:
                    data = sock.recv(1024)
                    recvd_size = filesize
                fp.write(data)
            fp.close()

        break


