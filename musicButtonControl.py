# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:59:56 2019

@author: Lin
"""

import tkinter as tk
from tkinter import ttk
import pygame
import os
import random
import time
import shutil


randomPlay=0
pause=0
page=1
add=0
touch=0


class MusicButtonControl(tk.Frame):
    def __init__(self,root,master, root_height,otherMusicList):
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.master=master
        self.frame= tk.Frame(master)
        self.frame.pack(side=tk.TOP,fill=tk.Y)
        self.frame0= tk.Frame(master)
        self.frame0.pack(side=tk.TOP,fill=tk.Y)
        self.frame1= tk.Frame(master)
        self.frame1.pack(side=tk.TOP,fill=tk.Y)
        self.musiclist_top= tk.Frame(self.frame1)
        self.musiclist_top.pack(side=tk.TOP,fill=tk.Y)
        self.musiclist_bottom= tk.Frame(self.frame1)
        self.musiclist_bottom.pack(side=tk.TOP,fill=tk.Y)
        self.addnewmusic= tk.Frame(self.frame1)
        self.addnewmusic.pack(side=tk.BOTTOM,fill=tk.Y)
        
        self.lv= tk.StringVar()
        self.listBox= tk.Listbox(self.frame1,selectmode=tk.BROWSE,width=20,height=15,bg="#FFFACD",listvariable=self.lv)
        self.listBox.pack(side=tk.LEFT,fill=tk.X)
        self.otherMusicList= otherMusicList
                                 
        self.buttonaddmusic=tk.Button(self.addnewmusic,text="增加音樂",command=self.addNewMusic,width=8,height=2,bg='#FFEC8B')
        self.buttondelete=tk.Button(self.addnewmusic,text="刪除",command=self.deleteMusic,width=8,height=2,bg='#FFEC8B')
        self.buttondelete.pack(side=tk.RIGHT,fill=tk.X)
                                    
        self.addMusicName()
        # 加載音樂列表
        #self.otherMusicList= otherMusicList
        self.loadMusic()
        print("======音樂加載完成")

     
        self.buttonPlay= tk.Button(self.frame,text="播放",command=self.playMusic,width=8,height=2,bg='#FFEC8B')        
        self.buttonPause= tk.Button(self.frame,text="暂停/繼續",command=self.pauseMusic,width=8,height=2,bg='#FFEC8B')     
        self.buttonStop= tk.Button(self.frame,text="停止",command=self.stopMusic,width=8,height=2,bg='#FFEC8B')    
        self.buttonPrevious= tk.Button(self.frame,text="上一曲",command=self.previousMusic,width=8,height=2,bg='#FFEC8B')
        self.buttonNext= tk.Button(self.frame,text="下一曲",command=self.nextMusic,width=8,height=2,bg='#FFEC8B')
        
        self.buttonPlay.pack(side=tk.LEFT,fill=tk.X)
        self.buttonPause.pack(side=tk.LEFT,fill=tk.X)
        self.buttonStop.pack(side=tk.LEFT,fill=tk.X)
        self.buttonPrevious.pack(side=tk.LEFT,fill=tk.X)
        self.buttonNext.pack(side=tk.LEFT,fill=tk.X)
        
        big_button_Style = ttk.Style ()
        big_button_Style.configure("big.TButton", font = ('Arial','10'))
        self.musiclist1= ttk.Button(self.musiclist_top,text="總清單",command=lambda: self.switch_list(1),width=10,  style = "big.TButton")
        self.musiclist2= ttk.Button(self.musiclist_top,text="播放清單2",command=lambda: self.switch_list(2),width=10,  style = "big.TButton")
        self.musiclist3= ttk.Button(self.musiclist_top,text="播放清單3",command=lambda: self.switch_list(3),width=10,  style = "big.TButton")
        self.musiclist4= ttk.Button(self.musiclist_bottom,text="播放清單4",command=lambda: self.switch_list(4),width=10,  style = "big.TButton")
        self.musiclist5= ttk.Button(self.musiclist_bottom,text="播放清單5",command=lambda: self.switch_list(5),width=10,  style = "big.TButton")
        self.musiclist6= ttk.Button(self.musiclist_bottom,text="播放清單6",command=lambda: self.switch_list(6),width=10,  style = "big.TButton")
        
        self.musiclist1.pack(side='left', padx=20)
        self.musiclist2.pack(side='left', padx=20)
        self.musiclist3.pack(side='left', padx=20)
        self.musiclist4.pack(side='left', padx=20)
        self.musiclist5.pack(side='left', padx=20)
        self.musiclist6.pack(side='left', padx=20)   
                                      
        var_mode = tk.IntVar()
        self.randomplay=tk.Radiobutton(self.frame0,variable = var_mode,value = 1,text ="隨機播放",command =self.randomplay )
        self.randomplay.pack(side=tk.LEFT,fill=tk.X)
        self.inturnplay=tk.Radiobutton(self.frame0,variable = var_mode,value = 2,text ="循序播放",command =self.inturnplay )
        self.inturnplay.pack(side=tk.LEFT,fill=tk.X)
            
        self.hide_musicbuttoncontrol()

    def loadMusic(self):
        self.otherMusicList.loadMusic()

    def getCurrentMusicPath(self):
        path=self.otherMusicList.MusicPath(page)
        # self.listBox.select_set(0)
        for item in range(self.listBox.size()):
            musicAbsPath= path +"\\"+self.listBox.get(item)
            if self.listBox.selection_includes(item):
                path= musicAbsPath
                #print("-----", path)
                return path
                

    # 添加音樂曲目
    def addMusicName(self):
        
        path= r"music"#"\home\pi\/Music"
        self.listBox.delete(0,tk.END )
      
        musicNameList= os.listdir(path)
        for musicName in musicNameList:
            path1= os.path.join(path, musicName)
            path1list= os.path.splitext(path1)
            if path1list[-1]== ".mp3":
                self.listBox.insert(tk.END, musicName)
                
    def addMusicNameitem(self):
        
        global add
        path= r"music"#"\home\pi\/Music"
        path1=self.otherMusicList.MusicPath(page)
        self.listBox.delete(0,tk.END )
      
        musicNameList= os.listdir(path)
        musicNameList1= os.listdir(path1)
        for musicName in musicNameList:
            path2= os.path.join(path, musicName)
            path1list= os.path.splitext(path2)
            if path1list[-1]== ".mp3":
                #print(path1list)
                for musicName2 in musicNameList1:
                    path3= os.path.join(path1, musicName2)
                    path1list1= os.path.splitext(path3)
                    if path1list1[-1]== ".mp3":
                        if (musicName==musicName2):
                            add=1
                            break
                        else:
                            add=0
                            continue
                if (add==0):
                    self.listBox.insert(tk.END, musicName)
                
                
    def deleteMusic(self):
        os.remove(self.getCurrentMusicPath())
        self.refreshMusiclist()      
                
    def refreshMusiclist(self):
        path=self.otherMusicList.MusicPath(page)
        self.listBox.delete(0,tk.END )
                
        musicNameList= os.listdir(path)
        for musicName in musicNameList:
            path1= os.path.join(path, musicName)
            path1list= os.path.splitext(path1)
            if path1list[-1]== ".mp3":
                self.listBox.insert(tk.END, musicName)
                
                
    def playMusic(self):
        global stop
        stop=0
        if self.getCurrentMusicPath()==None:
            path= r"music"#'/home/pi/Music/'
            music=random.randint(0, self.listBox.size())
            musicAbs1Path= path +"\\"+self.listBox.get(music)
            pygame.mixer.music.load(musicAbs1Path)
            print(musicAbs1Path)
        else:
            pygame.mixer.music.load(self.getCurrentMusicPath())
        print(self.getCurrentMusicPath())
        self.play()
    
    def play(self): 
        self.otherMusicList.play()
        
    def switch_list(self,musiclist_ID):
        global page
        global path
        if(musiclist_ID==1):
            page=1
            self.controladdbutton()
            self.refreshMusiclist()
        if(musiclist_ID==2):
            page=2
            self.controladdbutton()
            self.refreshMusiclist()
        if(musiclist_ID==3):
            page=3
            self.controladdbutton()
            self.refreshMusiclist()
        if(musiclist_ID==4):
            page=4
            self.controladdbutton()
            self.refreshMusiclist()
        if(musiclist_ID==5):
            page=5
            self.controladdbutton()
            self.refreshMusiclist()
        if(musiclist_ID==6):
            page=6
            self.controladdbutton()
            self.refreshMusiclist()
    
    def switch(self):#偵測音樂是否結束，結束播放下一首
        global randomPlay
        for event in pygame.event.get():
            if pygame.mixer.music.get_busy( ):
                self.switch()
            else:
                if (randomPlay==1):
                    self.randomNext()
                else:
                    self.nextMusic()
            
    def controladdbutton(self):
        global page
        if(page!=1):
            self.buttonaddmusic.pack(side=tk.RIGHT,fill=tk.X)
        else:
            self.buttonaddmusic.pack_forget()

    def pauseMusic(self):
        global pause
        pause+=1
        if(pause%2 == 1):
            self.otherMusicList.pauseMusic()
        else:
            self.otherMusicList.unpauseMusic()


    def stopMusic(self):
        self.otherMusicList.stopMusic()
        

    def previousMusic(self):
        path=self.otherMusicList.MusicPath(page)
        currentMusicPath= self.getCurrentMusicPath()
        for musicpathIndex in range(self.listBox.size()):
            musicAbs1Path= path +"\\"+self.listBox.get(musicpathIndex)
            if currentMusicPath== musicAbs1Path:
                ismusic= musicpathIndex
                ismusic-= 1
                if ismusic < 0:
                    pygame.mixer.music.load(path+ "\\"+self.listBox.get(0))
                    pygame.mixer.music.play()
                    break
                break
        musicAbsPath= path +"\\"+self.listBox.get(ismusic)
        pygame.mixer.music.load(musicAbsPath)
        # 顯示正在播放的歌曲，並取消上一首歌曲
        self.listBox.select_clear(musicpathIndex)
        self.listBox.select_set(ismusic)
        self.play()
            

    def nextMusic(self):
        
        path=self.otherMusicList.MusicPath(page)
        currentMusicPath= self.getCurrentMusicPath()
        print(currentMusicPath)
        for musicpathIndex in range(self.listBox.size()):
            ismusic=0
            musicAbs1Path= path +"\\"+self.listBox.get(musicpathIndex)
            if currentMusicPath== musicAbs1Path:
                ismusic= musicpathIndex
                ismusic+= 1 
                if ismusic >= self.listBox.size():
                    ismusic=0
                    break 
                break
        musicAbsPath= path +"\\"+self.listBox.get(ismusic)
        print(musicAbsPath)
        pygame.mixer.music.load(musicAbsPath)
        # 顯示正在播放的歌曲，並取消上一首歌曲
        self.listBox.select_clear(musicpathIndex)
        self.listBox.select_set(ismusic)
        print(self.getCurrentMusicPath())
        self.play()
        
    def randomNext(self):
        path=self.otherMusicList.MusicPath(page)
        music=random.randint(0, self.listBox.size())
        musicAbs1Path= path +"\\"+self.listBox.get(music)
        pygame.mixer.music.load(musicAbs1Path)
        print(musicAbs1Path)
        self.play()
        
    def randomplay(self):
        global randomPlay
        randomPlay=1
        
    def inturnplay(self):
        global randomPlay
        randomPlay=0
        
    def show_musicbuttoncontrol(self):
        self.frame.pack(side=tk.TOP,fill=tk.Y)
        self.frame0.pack(side=tk.TOP,fill=tk.Y)
        self.frame1.pack(side=tk.TOP,fill=tk.Y)
        
    def hide_musicbuttoncontrol(self):
        self.frame.pack_forget()
        self.frame0.pack_forget()
        self.frame1.pack_forget()
    
    
    
    def addNewMusic(self):
        
        
        self.frame.pack_forget()
        self.frame0.pack_forget()
        self.addnewmusic.pack_forget()
        self.musiclist_top.pack_forget()
        self.musiclist_bottom.pack_forget()
        self.musiclist1.pack_forget()
        self.musiclist2.pack_forget()
        self.musiclist3.pack_forget()
        self.musiclist4.pack_forget()
        self.musiclist5.pack_forget()
        self.musiclist6.pack_forget()
        self.listBox.pack_forget()
        self.listBox.pack(side=tk.LEFT,fill=tk.X)
        self.addMusicNameitem()
        if (self.listBox.size()!=0):
            self.addmusic=tk.Button(self.frame1,text="新增",command=self.AddMusic,width=8,height=2,bg='#FFEC8B')
            self.addmusic.pack(side=tk.LEFT,fill=tk.X)
        self.exit=tk.Button(self.frame1,text="關閉",command=self.Exit,width=8,height=2,bg='#FFEC8B')
        self.exit.pack(side=tk.LEFT,fill=tk.X)
        
    def AddMusic(self):
        global touch
        touch+=1
        path=self.otherMusicList.MusicPath(page)
        shutil.copy(self.getCurrentMusicPath1(), path)
        self.test_label=tk.Label(self.frame1, text="成功加入", font=("Arial",20))
        self.test_label.place(x = 150, y = 30, height=25)
        self.addMusicNameitem()
        '''if(touch%2==1):
            if(touch>1):
                self.test_label.pack_forget()
            self.test_label=tk.Label(self.frame1, text="成功", font=("Arial",20))
            self.test_label.pack(side=tk.LEFT,fill=tk.X)
        else:
            self.test_label.pack_forget()
            self.test_label=tk.Label(self.frame1, text="success", font=("Arial",20))
            self.test_label.pack(side=tk.LEFT,fill=tk.X)'''
            
                    
    def getCurrentMusicPath1(self):
            
            path= r"music"#"\home\pi\/Music"
            for item in range(self.listBox.size()):
                musicAbsPath= path +"\\"+self.listBox.get(item)
                if self.listBox.selection_includes(item):
                    path= musicAbsPath
                    #print("-----", path)
                    return path
                
    def Exit(self):
        if(touch>0):
            self.test_label.place_forget()
        self.listBox.pack_forget()
        self.frame1.pack_forget()
        self.frame.pack(side=tk.TOP,fill=tk.Y)
        self.frame0.pack(side=tk.TOP,fill=tk.Y)
        self.frame1.pack(side=tk.TOP,fill=tk.Y)
        self.musiclist_top.pack(side=tk.TOP,fill=tk.Y)
        self.musiclist_bottom.pack(side=tk.TOP,fill=tk.Y)
        self.listBox.pack(side=tk.LEFT,fill=tk.X)
        self.refreshMusiclist()
        self.musiclist1.pack(side='left', padx=20)
        self.musiclist2.pack(side='left', padx=20)
        self.musiclist3.pack(side='left', padx=20)
        self.musiclist4.pack(side='left', padx=20)
        self.musiclist5.pack(side='left', padx=20)
        self.musiclist6.pack(side='left', padx=20)
        self.addnewmusic.pack(side=tk.BOTTOM,fill=tk.Y)
        self.addmusic.pack_forget()
        self.addmusic.pack_forget()
        self.exit.pack_forget()
            
        
        
        
    
        
    
                
    
        
    



