# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 00:25:36 2019

@author: Lin
"""

import tkinter as tk
import pygame
import time
import os

temp_path = "music"
#temp_path = "/home/pi/Desktop/clock/clock_app_project-master/music"

class MusicList(tk.Frame):
    def __init__(self,root,master, root_height):
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.master=master
        
        self.MusicList2 = temp_path+"/MusicList2"
        if not os.path.isdir(self.MusicList2):
            os.mkdir(self.MusicList2)
        self.MusicList3 = temp_path+"/MusicList3"
        if not os.path.isdir(self.MusicList3):
            os.mkdir(self.MusicList3)
        self.MusicList4 = temp_path+"/MusicList4"
        if not os.path.isdir(self.MusicList4):
            os.mkdir(self.MusicList4)
        self.MusicList5 = temp_path+"/MusicList5"
        if not os.path.isdir(self.MusicList5):
            os.mkdir(self.MusicList5)
        self.MusicList6 = temp_path+"/MusicList6"
        if not os.path.isdir(self.MusicList6):
            os.mkdir(self.MusicList6)
        
    def loadMusic(self):
        pygame.init()
        pygame.mixer.init()
        
    '''def MusicPath(self,musicAbsPath):
        path= musicAbsPath
                #print("-----", path)
        return path'''
        
    def MusicPath(self,page):
        if(page==1):
            path= temp_path#"\home\pi\/Music"
        if(page==2):
            path= self.MusicList2#"\home\pi\/Music"
        if(page==3):
            path= self.MusicList3#"\home\pi\/Music"
        if(page==4):
            path= self.MusicList4#"\home\pi\/Music"
        if(page==5):
            path= self.MusicList5#"\home\pi\/Music"
        if(page==6):
            path= self.MusicList6#"\home\pi\/Music
        return path    
    
    def playMusic(self,songname):
        #global stop,pause
        #stop=0
        #pause=0
        path= temp_path
        musicAbsPath= path +"/"+songname
        if (pygame.mixer.music.load(musicAbsPath)==False):
            print('error')
        else:
            print(musicAbsPath) 
            self.play()
    
    def play(self):
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()

    def pauseMusic(self):
        pygame.mixer.music.pause()
        
    def unpauseMusic(self):
        pygame.mixer.music.unpause()
            
    def stopMusic(self):
        time.sleep(0.05)
        pygame.mixer.music.pause()
    