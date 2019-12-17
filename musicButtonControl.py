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
from PIL import ImageTk,Image
import shutil


randomPlay=0
pause=0
page=1
add=0
touch=0
stop=0



class MusicButtonControl(tk.Frame):
    def __init__(self,root,master, root_height,otherMusicList):
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.master=master
        self.fk = tk.Frame(self.master,bg = 'black')
        self.fk.pack(side=tk.TOP,fill=tk.BOTH)
        self.frame= tk.Frame(self.master,bg = 'black')
        self.frame.pack(side= tk.TOP,fill=tk.X)
        self.frame0= tk.Frame(self.master,bg = 'black')
        self.frame0.pack(side=tk.TOP,fill=tk.X)
        self.frame1= tk.Frame(self.master,bg = 'black')
        self.frame1.pack(side=tk.TOP,fill=tk.X)
        self.musiclist_top= tk.Frame(self.frame1,bg = 'black')
        self.musiclist_top.pack(side=tk.TOP,fill=tk.X)
        self.musiclist_bottom= tk.Frame(self.frame1,bg = 'black')
        self.musiclist_bottom.pack(side=tk.TOP)
        self.addnewmusic= tk.Frame(self.frame1)
        self.sel_musicList = 0
        self.m= tk.Frame(self.frame1, borderwidth=5, relief="groove",bg = 'black')
        self.m.pack(side=tk.TOP, pady = (0,5))
        
        #圖片
        self.play_image=ImageTk.PhotoImage(Image.open('picture/play.jpg'))
        self.pause_image=ImageTk.PhotoImage(Image.open('picture/pause.jpg'))
        self.stop_image=ImageTk.PhotoImage(Image.open('picture/stop.jpg'))
        self.previous_image=ImageTk.PhotoImage(Image.open('picture/lastsong.jpg'))
        self.next_image=ImageTk.PhotoImage(Image.open('picture/nextsong.jpg'))
        self.circle_image=ImageTk.PhotoImage(Image.open('picture/restart.jpg'))
        self.random_image=ImageTk.PhotoImage(Image.open('picture/random.jpg'))
        self.pipe_image=ImageTk.PhotoImage(Image.open('picture/pipe.jpg'))
        
        self.lv= tk.StringVar()
        self.listBox= tk.Listbox(self.m,selectmode=tk.BROWSE, font=("Arial",14),width=25,height=4,bg="light grey",listvariable=self.lv)
        self.listBox.pack(side=tk.TOP)
        self.otherMusicList= otherMusicList
                                 
        self.addnewmusic.pack(side=tk.LEFT,fill=tk.X)
        self.ADD_FRAME= tk.Frame(self.musiclist_top,bg = 'black')
        self.ADD_FRAME.pack(side=tk.TOP, pady = (10,5))
        self.comboExample = ttk.Combobox(self.ADD_FRAME, values=["總清單", "播放清單1", "播放清單2", "播放清單3", "播放清單4", "播放清單5"], width = 15,background = "gray")
        self.comboExample.current(0)
        self.comboExample.pack(side='left', padx=(0,30))
        self.buttonaddmusic=tk.Button(self.ADD_FRAME,text="增加音樂",command=self.addNewMusic,width=6,height=1,bg='black', foreground="white")
        self.buttondelete=tk.Button(self.ADD_FRAME,text="刪除音樂",command=self.deleteMusic,width=6,height=1,bg='black', foreground="white")
        self.buttondelete.pack(side=tk.LEFT, padx=(25,0))
                                    
        self.addMusicName()
        # 加載音樂列表
        #self.otherMusicList= otherMusicList
        self.loadMusic()
        print("======音樂加載完成")
    
        pygame.mixer.music.set_volume(0)
        
        self.decorate_line = tk.Label(self.frame0, image = self.pipe_image, bg='black', foreground="white")
        self.decorate_line.pack(anchor = tk.N, pady = (0,5))
        #self.buttonPlay= tk.Button(self.frame,text="播放",command=self.playMusic,width=5.height=2,bg='#FFEC8B') 
        self.buttonPlay= tk.Button(self.frame,image=self.play_image,command=self.playMusic,width=20,height=20,bg='black', foreground="white")
        self.buttonPause= tk.Button(self.frame,image=self.pause_image,command=self.pauseMusic,width=20,height=20,bg='black', foreground="white")     
        self.buttonStop= tk.Button(self.frame,image=self.stop_image,command=self.stopMusic,width=20,height=20,bg='black', foreground="white")    
        self.buttonPrevious= tk.Button(self.frame,image=self.previous_image,command=self.previousMusic,width=20,height=20,bg='black', foreground="white")
        self.buttonNext= tk.Button(self.frame,image=self.next_image,command=self.nextMusic,width=20,height=20,bg='black', foreground="white")
        self.scalevolume= tk.Scale(self.frame0,from_=0, to=100, orient=tk.HORIZONTAL,length = 200,showvalue=1, command=self.plus,bg='black', foreground="white")                           
        
        self.buttonPrevious.pack(side=tk.LEFT)
        self.buttonPlay.pack(side=tk.LEFT, padx = (25,0))
        self.buttonPause.pack(side=tk.LEFT, padx = (25,0))
        self.buttonStop.pack(side=tk.LEFT, padx = (25,0))
        self.buttonNext.pack(side=tk.LEFT, padx = (25,0))
        #self.buttonLess.pack(side=tk.LEFT)
        
        big_button_Style = ttk.Style ()
        big_button_Style.configure("big.TButton", font = ('Arial','10'))
                
        #self.musiclist1= ttk.Button(self.musiclist_top,text="總清單",command=lambda: self.switch_list(1),width=10,  style = "big.TButton")
        #self.musiclist2= ttk.Button(self.musiclist_top,text="播放清單2",command=lambda: self.switch_list(2),width=10,  style = "big.TButton")
        #self.musiclist3= ttk.Button(self.musiclist_top,text="播放清單3",command=lambda: self.switch_list(3),width=10,  style = "big.TButton")
        #self.musiclist4= ttk.Button(self.musiclist_bottom,text="播放清單4",command=lambda: self.switch_list(4),width=10,  style = "big.TButton")
        #self.musiclist5= ttk.Button(self.musiclist_bottom,text="播放清單5",command=lambda: self.switch_list(5),width=10,  style = "big.TButton")
        #self.musiclist6= ttk.Button(self.musiclist_bottom,text="播放清單6",command=lambda: self.switch_list(6),width=10,  style = "big.TButton")
        
        #self.musiclist1.pack(side='left', padx=20)
        #self.musiclist2.pack(side='left', padx=20)
        #self.musiclist3.pack(side='left', padx=20)
        #self.musiclist4.pack(side='left', padx=20)
        #self.musiclist5.pack(side='left', padx=20)
        #self.musiclist6.pack(side='left', padx=20)
        
        
        
            
                                      
        #var_mode = tk.IntVar()
        self.randomplay=tk.Button(self.frame0,image =self.random_image,command =self.randomplay,width=20,height=20,bg='black', foreground="white")
        self.inturnplay=tk.Button(self.frame0,image =self.circle_image,command =self.inturnplay,width=20,height=20,bg='black', foreground="white")
        self.inturnplay.pack(side=tk.LEFT)
        self.scalevolume.pack(side=tk.LEFT)       
        self.randomplay.pack(side=tk.LEFT)
        
       
            
        self.hide_musicbuttoncontrol()

    def loadMusic(self):
        self.otherMusicList.loadMusic()

    def getCurrentMusicPath(self):
        path=self.otherMusicList.MusicPath(page)
        # self.listBox.select_set(0)
        for item in range(self.listBox.size()):
            musicAbsPath= path +"/"+self.listBox.get(item)
            if self.listBox.selection_includes(item):
                path= musicAbsPath
                #print("-----", path)
                return path
            
    def getCurrentMusic(self):
        path=self.otherMusicList.MusicPath(page)
        # self.listBox.select_set(0)
        for item in range(self.listBox.size()):
            musicAbsPath= self.listBox.get(item)
            if self.listBox.selection_includes(item):
                path= musicAbsPath
                #print("-----", path)
                return path
                
    def plus(self,val):
        volume=int(val)/100
        pygame.mixer.music.set_volume(volume)
    
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
        path=r"music"#"\home\pi\/Music"
        path1=self.otherMusicList.MusicPath(page)
        self.listBox.delete(0,tk.END )
      
        musicNameList= os.listdir(path)
        musicNameList1= os.listdir(path1)
        for musicName in musicNameList:
            path2= os.path.join(path, musicName)
            path1list= os.path.splitext(path2)
            if path1list[-1]== ".mp3":
                print(path1list)
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
                
                
    def deleteMusicitem(self):
        if(page==1):
            for i in range(2,7):
                #print(self.getCurrentMusic())
                path1=self.otherMusicList.MusicPath(i)
                musicNameList1= os.listdir(path1)
                for musicName2 in musicNameList1:
                    path3= os.path.join(path1, musicName2)
                    path1list1= os.path.splitext(path3)
                    if path1list1[-1]== ".mp3":
                        if (self.getCurrentMusic()==musicName2):
                            #print(self.getCurrentMusic())
                            musicAbsPath= path1 +"/"+musicName2
                            os.remove(musicAbsPath)
            os.remove(self.getCurrentMusicPath())
            #print(self.getCurrentMusicPath())
            self.refreshMusiclist()
        else:
            os.remove(self.getCurrentMusicPath())
            print(self.getCurrentMusicPath())
            self.refreshMusiclist() 
                
    def refreshMusiclist(self):
        path=self.otherMusicList.MusicPath(page)
        self.listBox.delete(0,tk.END )
                
        musicNameList= os.listdir(path)
        for musicName in musicNameList:
            path1= os.path.join(path, musicName)
            print(path1)
            path1list= os.path.splitext(path1)
            if path1list[-1]== ".mp3":
                self.listBox.insert(tk.END, musicName)
                
                
    def playMusic(self):
        global stop,pause
        stop=0
        pause=0
        if self.getCurrentMusicPath()==None:
            path=self.otherMusicList.MusicPath(page)
            music=random.randint(0, self.listBox.size())
            musicAbs1Path= path +"/"+self.listBox.get(music)
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
        global randomPlay,stop
        for event in pygame.event.get():
            if pygame.mixer.music.get_busy( ):
                self.switch()
            else:
                if(stop!=1):
                    if (randomPlay==1):
                        self.randomNext()
                    else:
                        self.nextMusic()
            
    def controladdbutton(self):
        global page
        if(page!=1):
            self.buttonaddmusic.pack(side=tk.LEFT)
            self.buttondelete.pack(side=tk.LEFT, padx=(15,0))
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
        global stop
        stop=1;
        self.otherMusicList.stopMusic()
        

    def previousMusic(self):
        path=self.otherMusicList.MusicPath(page)
        currentMusicPath= self.getCurrentMusicPath()
        for musicpathIndex in range(self.listBox.size()):
            musicAbs1Path= path +"/"+self.listBox.get(musicpathIndex)
            if currentMusicPath== musicAbs1Path:
                ismusic= musicpathIndex
                ismusic-= 1
                if ismusic < 0:
                    pygame.mixer.music.load(path+ "/"+self.listBox.get(0))
                    pygame.mixer.music.play()
                    break
                break
        musicAbsPath= path +"/"+self.listBox.get(ismusic)
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
            musicAbs1Path= path +"/"+self.listBox.get(musicpathIndex)
            if currentMusicPath== musicAbs1Path:
                ismusic= musicpathIndex
                ismusic+= 1 
                if ismusic >= self.listBox.size():
                    ismusic=0
                    break 
                break
        musicAbsPath= path +"/"+self.listBox.get(ismusic)
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
        musicAbs1Path= path +"/"+self.listBox.get(music)
        pygame.mixer.music.load(musicAbs1Path)
        print(musicAbs1Path)
        self.play()
        
    def randomplay(self):
        global randomPlay
        randomPlay=1
        self.randomplay.config(bg='white',foreground="black")
        self.inturnplay.config(bg='black',foreground="white")
        
    def inturnplay(self):
        global randomPlay
        randomPlay=0
        self.inturnplay.config(bg='white',foreground="black")
        self.randomplay.config(bg='black',foreground="white")
        
    def show_musicbuttoncontrol(self):
        self.frame1.pack(side=tk.TOP,fill = tk.X)
        self.frame.pack(side=tk.TOP, pady = (15,0))
        self.frame0.pack(side=tk.TOP)
        self.ADD_FRAME.pack(side=tk.TOP, pady = (10,5))
        
    def hide_musicbuttoncontrol(self):
        self.frame.pack_forget()
        self.frame0.pack_forget()
        self.frame1.pack_forget()
    
    
    
    def addNewMusic(self):
        
        
        self.ADD_FRAME.pack_forget()
        self.frame.pack_forget()
        self.frame0.pack_forget()
        #self.musiclist1.pack_forget()
        #self.musiclist2.pack_forget()
        #self.musiclist3.pack_forget()
        #self.musiclist4.pack_forget()
        #self.musiclist5.pack_forget()
        #self.musiclist6.pack_forget()
        self.listBox.pack_forget()
        self.listBox.pack(side=tk.TOP)
        self.addMusicNameitem()
        self.a = tk.Frame(self.frame1,bg = 'black')
        if (self.listBox.size()!=0):
            self.addmusic=tk.Button(self.a,text="新增",command=self.AddMusic,width=8,height=2,bg='black',foreground = 'white')
            self.addmusic.pack(side=tk.LEFT)
        self.exit=tk.Button(self.a,text="關閉",command=self.Exit,width=8,height=2,bg='black',foreground = 'white')
        self.exit.pack(side=tk.LEFT,padx = (20,0))
        self.a.pack(side=tk.TOP,pady = (30,0))
 
    def deleteMusic(self):
        
        
        self.ADD_FRAME.pack_forget()
        self.frame.pack_forget()
        self.frame0.pack_forget()
        #self.musiclist1.pack_forget()
        #self.musiclist2.pack_forget()
        #self.musiclist3.pack_forget()
        #self.musiclist4.pack_forget()
        #self.musiclist5.pack_forget()
        #self.musiclist6.pack_forget()
        self.listBox.pack_forget()
        self.listBox.pack(side=tk.TOP)
        self.refreshMusiclist()
        self.a = tk.Frame(self.frame1,bg = 'black')
        if (self.listBox.size()!=0):
            self.addmusic=tk.Button(self.a,text="刪除",command=self.deleteMusicitem,width=8,height=2,bg='black',foreground = 'white')
            self.addmusic.pack(side=tk.LEFT)
        self.exit=tk.Button(self.a,text="關閉",command=self.Exit,width=8,height=2,bg='black',foreground = 'white')
        self.exit.pack(side=tk.LEFT, padx = (20,0))
        self.a.pack(side=tk.TOP, pady = (30,0))
       
    def AddMusic(self):
        global touch
        touch+=1
        path=self.otherMusicList.MusicPath(page)
        shutil.copy(self.getCurrentMusicPath1(), path)
        if(touch==1):
            self.test_label=tk.Label(self.frame1, text="成功加入", font=("Arial",20))
            self.test_label.pack(side=tk.LEFT)
        self.addMusicNameitem()
        if (self.listBox.size()==0):
            self.addmusic.pack_forget()
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
                musicAbsPath= path +"/"+self.listBox.get(item)
                if self.listBox.selection_includes(item):
                    path= musicAbsPath
                    #print("-----", path)
                    return path
                
    def Exit(self):
        global touch
        if(touch>0):
            self.test_label.pack_forget()
        touch=0
        self.a.pack_forget()
        self.hide_musicbuttoncontrol()
        self.show_musicbuttoncontrol()
        self.refreshMusiclist()
        #self.musiclist1.pack(side='left', padx=20)
        #self.musiclist2.pack(side='left', padx=20)
        #self.musiclist3.pack(side='left', padx=20)
        #self.musiclist4.pack(side='left', padx=20)
        #self.musiclist5.pack(side='left', padx=20)
        #self.musiclist6.pack(side='left', padx=20)
        #self.addnewmusic.pack(side=tk.BOTTOM)
        self.addmusic.pack_forget()
            
        
        
        
    
        
    
                
    
        
    



