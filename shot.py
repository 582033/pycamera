#!/usr/bin/env python
#-*-coding:utf8-*-
import os, sys, time, math
import pygame, pygame.camera, pygame.font
from pygame.locals import *


class pycamera():
    def __init__(self, savepath, savename):
        #摄像头支持的最大分辨率
        self.picture_resolution = (1280, 720)
        self.devicePath = "/dev/video0"

        self.savepath = savepath
        self.savename = './%s.jpg' % (savename)

        pygame.init()
        pygame.camera.init()
        pygame.font.init()

    #创建带时间的图片背景
    def _create_date_img(self):
        now = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
        font = pygame.font.SysFont("wenquanyimicrohei", 28)
        image = font.render(now, True, (255, 255, 255))
        #pygame.image.save(image, IMG)
        return image

    #对生成的图片进行位置移动
    def _scp(self):
        #os.system('scp %s root@yjinag.cn:/var/www/cake/other/ > /dev/null' % (IMG))
        os.system('cp %s %s > /dev/null' % (self.savename, self.savepath))

    #监测本地pygame可以调用的字体
    def show_fonts_list():
        print pygame.font.get_fonts()

    def output(self):
        image = self._create_date_img()
        cam = pygame.camera.Camera(self.devicePath, (self.picture_resolution[0], self.picture_resolution[1]))
        cam.start()
        cam_image = cam.get_image()
        #时间坐标
        date_x = math.floor(self.picture_resolution[0] * 0.75)
        date_y = math.floor(self.picture_resolution[1] * 0.9)
        cam_image.blit(image, (date_x, date_y))
        pygame.image.save(cam_image, self.savename)
        cam.stop()
        self._scp()

if __name__=="__main__":
    #pycamera(图片存放地址, 图片名称)
    pycamera = pycamera('/opt/www/', 'shot')
    #pycamera.show_fonts_list()
    counter = 0
    while True:
        pycamera.output()
        counter += 1
        print counter
        time.sleep(0.1)
