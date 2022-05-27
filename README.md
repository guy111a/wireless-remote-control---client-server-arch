# wireless-remote-control  client-server-arch
Weekend project .. incorporating c++ on arduinos and python for the rest.


This weekend project is all about learning how to use sockets.

So what's in there..?

A joystick breaker board s attached to an arduino nano, being able to move in 2 axes and also e pressed as a button.
From  the other hand, there is a RF 433 mhz module.

the joystick is producing an integer varying according the movements, 2 of them, one for the x axes and the other for the y.
the code is generating a string of chars, buffered tgether and then being transmitted thrugh the air ..

On the other side ( if the air :) ) there is the receiver of the same 433 mhz RF module, picking up the magic of transmittion passing the stream of data to arduino uno that is building back the string of chars, buffers them and separating to chars, castig them to integers and .. passing them thuogh the serial link tot he python script.

There actually 3 python scripts involved. (Architecture map of the system is attached)

1. The 1st script, awates the data coming through the serial link (USB) and when there is information stream, initiates a TCP socket that is connected to a server waiting for information. establishes a link and passes the information, then closes the link.
2. The 2nd script, a server that is waiting with a TCP socket for incoming connetions and information regarding the movement of the joystick. when such information is arriving, the server initiate a UDP socket and sending the information that had arrived into the socket. (Why UDP & TCP later on).
3. The last script is the Ball game. This script draws a board and a ball in the ceter. also creating a UDP socket that is silently waiting for incoming data. should such data arrive, the ball will move according to the movement of the joystick.


A bit about the technologies used in the project.
1. RF - As a model airplanes & drone pilot, There is some magic in my eyes, to see how you move a bit the stick of the controller and the plane hundres of meters away is obeying and the coltrol plates are moving and causing the plane to change the course.
2. Arduino - It is so much fun creating thigs that are actually exists in reality when i can the LED blinks or the Servo motor moves the way i programmed it to move. very satisfying.
3. Python - Fell in ove with this programming lanuage several years ago, so easy to acomplish whatever i want.
4. Sockets - didn't have much chance to play with this even though i work with Client/Servers every day.
5. Graphics on python, also a thing i did not have much chance to work with.


Regarding the UDP & TCP choices, this was done in order to have a chance to practive and understand the diferences btween them.
TCP - two way communication 
UDP - one way communication


Hardware in this project:
1. RF 433 mhz Transmitter 
2. RF 433 mhz receiver ( the same modules i used in my electric skeateboard project for the controller )
3. Arduino nano
4. Arduino uno
5. Joystick breaker board for arduino
6. 3 Computers for testing the Socket parts. (Win11, MacOS, Linux(wsl2 & RPI4)

* I may connect the system to drive the Tank project that is currentky awates parts to arrive, so keep checking this project.

