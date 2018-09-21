#!/usr/bin/env python3
import socket
import datetime

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    exit(1)

s.listen()

try:
    while 1:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(now)
        _str = 'HTTP/1.0 200 OK\n\n%s' % now
        conn.sendall(_str.encode())
        conn.close()
except Exception as e:
    print(e)
    pass

s.close()
