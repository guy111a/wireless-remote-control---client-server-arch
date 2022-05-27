# slave ball 

# UDP slave


import socket
import pygame

port = 60001

pygame.init()

screenWidth = 800
screenHeight = 600
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("JoyStick ... ")
origLocationX = 400
origLocationY = 300
radius = 25

window.fill((200, 200, 200))
locationX = origLocationX
locationY = origLocationY

print('main game loop')

while True:
    window.fill((200, 200, 200))
    pygame.draw.circle(window, (255, 0, 0), (locationX, locationY), radius, 4)
    pygame.display.flip()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('', port))
        print(f"waiting on port {port}.. ")
        data, addr = s.recvfrom(1024)

        got = data.decode()
        x, y = got.split(",")
        print(f'{x},{y}')

        if locationX > screenWidth-60:
            locationX = screenWidth-60
        if locationX < 60:
            locationX = 60
        if locationY > screenHeight - 60:
            locationY = screenHeight - 60
        if locationY < 60:
            locationY = 60

        locationX += int(x)*-1
        locationY += int(y)*-1

pygame.display.quit()
pygame.quit()

