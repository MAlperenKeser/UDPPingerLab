import socket
from socket import AF_INET, SOCK_DGRAM
import time

print ('sending packets')

serverName = '127.0.0.1'
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
sequence_number = 1
rtt = []

for i in range(10):
    start = time.time()
    message = ('PING %d %d' % (sequence_number, start))
    clientSocket.sendto(message.encode(), (serverName, 12000))
    try:
        message, address = clientSocket.recvfrom(1024)
        elapsed = (time.time() - start)
        rtt.append(elapsed)
        print (message)
        print ('Round Trip Time is:' + str(elapsed) + ' seconds')
    except socket.timeout:
        print (message)
        print ('Request timed out')
    sequence_number += 1

mean = sum(rtt, 0.0) / len(rtt)
print ('')
print ('Average RTT is:' + str(mean)+ ' seconds')
print ('Packet loss rate is:' + str((sequence_number - len(rtt)) * 10) + ' percent')
clientSocket.close()