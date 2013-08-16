#!/user/bin/python
#-*-coding:utf8-*- 
import os, sys, time
import pygame, pygame.camera, pygame.font
from pygame.locals import *

resolution = (640, 480)
devicePath = "/dev/video0"
IMG = './shot.jpg'
now = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))

pygame.init()
def create_date_img(): #{{{
    pygame.font.init()
    font = pygame.font.SysFont("ubuntu", 20)
    image = font.render(now, True, (255, 255, 255))
    #pygame.image.save(image, IMG)
    return image
#}}}
def scp(source_path, obj_path): #{{{
    os.system('scp ./shot.jpg www-data@582033.vicp.net:~/cake/other/ > /dev/null &')
#}}}
def output(): #{{{
    pygame.camera.init()
    image = create_date_img()
    cam = pygame.camera.Camera(devicePath, (resolution[0],resolution[1]))
    cam.start()
    cam_image = cam.get_image()
    cam_image.blit(image, (460, 450))
    pygame.image.save(cam_image, IMG)
    cam.stop()
    scp(IMG, '/var/www/cake/other/')
#}}}
def sleep(): #{{{
    while True:
        output()
        time.sleep(10)
#}}}
sleep()
