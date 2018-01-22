import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5011
BUFFER_SIZE = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr

while 1:
    num = conn.recv(BUFFER_SIZE)
    num2 = int(num) # still have an error here when I want to change type of variable

    print "Number, Receive from Client is ", num2 
    
#---------------------------------------------------------------
    def fac(n): # factorial function
        num2 = 1
        while n >= 1:
            num2 = num2 * n
            n = n - 1
        return num2

    numRtn = fac(num2)
    print "Result: ", numRtn
    numRtn2 = str(numRtn)
    conn.send(numRtn2) #echo
conn.close
    
