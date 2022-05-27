# ball server

# this file is reading the information comming from the serial port USB
# the arduino rf rx is connected there and receiving the joystick movement
# the information is then passed to the "ball-server.py" that 
# will dispence the information to all slaves

import serial
import socket

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.050)

host = '127.0.0.1'
port = 60000


while True:
    while ser.in_waiting:
        got = ser.readline().decode()
        print(got)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            text = str(got).encode()
            s.send(text)

