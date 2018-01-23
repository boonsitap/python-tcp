import sys
import socket
import os


TCP_IP = '127.0.0.1'
TCP_PORT = 5053
fname = "test.jpg"

print "TCP target IP: ", TCP_IP
print "TCP target port: ", TCP_PORT
print "Image: ", fname

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#-------------------------------------------------------------------
src_dir = "E:/Network System Programing/hw1/tcp" #path of source directory
for fp in os.listdir(src_dir):
    fp = os.path.join(src_dir, fp)
    with open(fname, "r") as file_object:
        reader = file_object.read(1024)
        while reader:
            s.send(reader)
            reader = file_object.read(1024)
    file_object.close()

print "Data sent successfully"

