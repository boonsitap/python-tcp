import sys
import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORT = 5053
fname = 'test.jpg'

print "Image: ", fname

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()
    fln = "E:/image_from_client" #create folder name
    if not os.path.exists(fln):
        os.makedirs(fln)

    fp = open(fln + fname , "w")
    sImg = conn.recv(1024)
    while sImg:
        fp.write(sImg)
        sImg = conn.recv(1024)
    print "Data Uploaded successfully"
s.close()
