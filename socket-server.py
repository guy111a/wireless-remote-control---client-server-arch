
# this file is receiving the joystick information and forwarding to each of the slaves
# the slaves will draw the panel and will show the movement of the ball in the 
#display according to the joystick movements.


import socket
import threading 


host = '0.0.0.0'
port = 60000
udpPort = 60001
udpHost = ''

slaves = ['10.0.0.18', '10.0.0.21', '10.0.0.14', '10.0.0.22']

def handle(client):
    while True:
        data = client.recv(1024).decode()
        print(f'> {data}')
        for s in slaves:
            print(f'sending to {s}')
            udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udpSocket.sendto(data.encode('ascii'), (s, udpPort))
        break
    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)

    while True:
        con, addr = s.accept()
        print(f'{addr} connected')

        thread = threading.Thread(target = handle, args = (con, ))
        thread.start()
