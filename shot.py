#!/user/bin/python
#-*-coding:utf8-*- 
import os, sys, time
import pygame, pygame.camera, pygame.font
from pygame.locals import *

resolution = (640, 480)
devicePath = "/dev/video0"
IMG = './shot.jpg'

pygame.init()
def create_date_img(): #{{{
    now = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
    pygame.font.init()
    font = pygame.font.SysFont("wenquanyizenhei", 20)
    image = font.render(now, True, (255, 255, 255))
    #pygame.image.save(image, IMG)
    return image
#}}}
def scp(source_path, obj_path): #{{{
    os.system('scp %s www-data@42.96.185.104:~/cake/other/ > /dev/null' % (IMG))
    print ''
#}}}
def output(): #{{{
    pygame.camera.init()
    image = create_date_img()
    cam = pygame.camera.Camera(devicePath, (resolution[0],resolution[1]))
    cam.start()
    cam_image = cam.get_image()
    cam_image.blit(image, (440, 450))
    pygame.image.save(cam_image, IMG)
    cam.stop()
    scp(IMG, '/var/www/cake/other/')
#}}}
def sleep(): #{{{
    counter = 0
    while True:
        output()
        counter += 1
        print counter
        time.sleep(1)
#}}}
def print_all_fonts():#{{{
    pygame.font.init()
    print pygame.font.get_fonts()
#}}}
#print_all_fonts()
sleep()


