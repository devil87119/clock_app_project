# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 00:25:36 2019

@author: Lin
"""

import tkinter as tk
import pygame
import time
import os



class MusicList(tk.Frame):
    def __init__(self,root,master, root_height):
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.master=master
        
        MusicList2 = "music/MusicList2"
        if not os.path.isdir(MusicList2):
            os.mkdir(MusicList2)
        MusicList3 = "music/MusicList3"
        if not os.path.isdir(MusicList3):
            os.mkdir(MusicList3)
        MusicList4 = "music/MusicList4"
        if not os.path.isdir(MusicList4):
            os.mkdir(MusicList4)
        MusicList5 = "music/MusicList5"
        if not os.path.isdir(MusicList5):
            os.mkdir(MusicList5)
        MusicList6 = "music/MusicList6"
        if not os.path.isdir(MusicList6):
            os.mkdir(MusicList6)
        
    def loadMusic(self):
        pygame.init()
        pygame.mixer.init()
        
    '''def MusicPath(self,musicAbsPath):
        path= musicAbsPath
                #print("-----", path)
        return path'''
        
    def MusicPath(self,page):
        if(page==1):
            path= r"music"#"\home\pi\/Music"
        if(page==2):
            path= r"music/MusicList2"#"\home\pi\/Music"
        if(page==3):
            path= r"music/MusicList3"#"\home\pi\/Music"
        if(page==4):
            path= r"music/MusicList4"#"\home\pi\/Music"
        if(page==5):
            path= r"music/MusicList5"#"\home\pi\/Music"
        if(page==6):
            path= r"music/MusicList6"#"\home\pi\/Music
        return path    
    
    def playMusic(self,songname):
        #global stop,pause
        #stop=0
        #pause=0
        path= r"music"
        musicAbsPath= path +"\\"+songname
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
    