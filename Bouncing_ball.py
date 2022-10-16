import pygame
import random
pygame.init()
window= pygame.display.set_mode((800,800))

ball_x=400-12
ball_y=400-12
ball_Xmove=0.5
ball_Ymove=0.6
pixel=25
while True:
    window.fill((255,0,0))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
    if ball_x+pixel>=800 or ball_x <=0:
            ball_Xmove*=-1
    if ball_y+pixel>=800 or ball_y <=0:
            ball_Ymove*=-1
    ball_x +=ball_Xmove
    ball_y +=ball_Ymove

    pygame.draw.circle(window,(234,255,45),(int(ball_x),int(ball_y)),65)
    pygame.display.update()
