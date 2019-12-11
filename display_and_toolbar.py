# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:07:35 2019

@author: User
"""

import tkinter as tk  
#from test_GUI import *
from homepage import *
from weather import *
from alarm import *
from musicList import MusicList
from musicButtonControl import *
from weather_page import *
from FMpage import *
from Calendarpage import *
from PIL import ImageTk,Image
import pygame
import time
import threading

now_page = 0
count=0
#Animation parameter
song = list()
song_point = 0
run_time = 0
song_animation_start = 0

class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("大賢四代目")
        #self.root.attributes('-type', 'dock')
        self.root_height = 322
        self.root_width = int(self.root_height/5.1*7.6)
        self.root.geometry(str(self.root_width)+"x"+str(self.root_height))
        
        #Big frame
        self.big_frame = tk.Frame(self.root)#, highlightcolor="green", highlightthickness=5
        self.big_frame.pack(side = 'left', fill=tk.BOTH,expand = True)
        
        
        #tool frame
        self.tool_frame = tk.Frame(self.big_frame)#, highlightcolor="green", highlightthickness=5
        self.tool_frame.pack(side = 'left', fill=tk.Y)
        
        #main frame
        self.main_frame = tk.Frame(self.big_frame)#, borderwidth=2, relief="groove")#, highlightcolor="green", highlightthickness=5
        self.main_frame.pack(anchor = tk.N, fill=tk.BOTH,expand = True)
                
        self.main_frame.config(bg = 'black')
        self.tool_frame.config(bg = 'black')
        self.big_frame.config(bg = 'black')
        
        self.weather = Weather("Taipei")
        self.homepage = Homepage(self.root, self.main_frame,self.root_height,self.weather)             
        self.musicList = MusicList(self.root,self.main_frame,self.root_height)
        self.musicButtonControl = MusicButtonControl(self.root,self.main_frame,self.root_height,self.musicList)
        self.alarm = Alarm(self.root, self.main_frame,self.root_height,self.musicList)
        self.FMpage = FMpage(self.root, self.main_frame, self.root_height)  
        self.weather_page = weather_page(self.root, self.main_frame,self.root_height,self.weather)
        self.CalendarPage = CalendarPage(self.root, self.main_frame, self.root_height)        
        self.toolbar = Toolbar(self.root, self.tool_frame, self.homepage, self.alarm, self.musicButtonControl, self.FMpage, self.weather_page, self.CalendarPage, self.root_height)
    

class Toolbar():
    def __init__(self, root, tool_frame, homepage, alarm, musicButtonControl, FMpage, weather_page, CalendarPage, root_height):   
        #set button x,y 
        self.button_X = 0
        self.root_height = root_height
        self.root = root
        self.homepage = homepage
        self.alarm = alarm
        self.musicButtonControl = musicButtonControl
        self.FMpage = FMpage
        self.weather_page = weather_page
        self.CalendarPage = CalendarPage
        self.tool_frame=tool_frame
        
        self.alarm_image=ImageTk.PhotoImage(Image.open('picture/alarm.jpg'))
        self.fm_image=ImageTk.PhotoImage(Image.open('picture/fm.jpg'))
        self.home_image=ImageTk.PhotoImage(Image.open('picture/home.jpg'))
        self.schedule_image=ImageTk.PhotoImage(Image.open('picture/schedule.jpg'))
        self.music_image=ImageTk.PhotoImage(Image.open('picture/music.jpg'))
        self.weather_image=ImageTk.PhotoImage(Image.open('picture/weatherpage.jpg'))

        
        #toolbar button
        self.Main_page=tk.Button(self.root, image = self.home_image, command=lambda: self.switch_page(0), width=45, bg = 'black', relief = 'flat', activebackground = 'black')
        self.FM_page=tk.Button(self.root, image = self.fm_image, command=lambda: self.switch_page(1), width=45, bg = 'black', relief = 'flat', activebackground = 'black')
        self.Music_page=tk.Button(self.root, image = self.music_image, command=lambda: self.switch_page(2), width=45, bg = 'black', relief = 'flat', activebackground = 'black')
        self.Alarm_page=tk.Button(self.root, image = self.alarm_image, command=lambda: self.switch_page(3), width=45, bg = 'black', relief = 'flat', activebackground = 'black')
        self.Scedule_page=tk.Button(self.root, image = self.schedule_image, command=lambda: self.switch_page(4), width=45, bg = 'black', relief = 'flat', activebackground = 'black')
        self.Weather_page=tk.Button(self.root, image = self.weather_image, command=lambda: self.switch_page(5), width=45, bg = 'black', relief = 'flat', activebackground = 'black')
        self.Game_page=tk.Button(self.root, text="Game", command=lambda: self.switch_page(6), width=6, height=2)
        self.Setting_page=tk.Button(self.root, text="Setting", command=lambda: self.switch_page(7), width=6, height=2)
        self.show_button=tk.Button(self.tool_frame, text="<", command=self.clickOK, bg = 'black',foreground = 'white', relief = 'flat', activebackground = 'black')
        self.test_label=tk.Label(root, text="<", font=("Arial",12))
        
        
        #buuton position
        '''self.Main_page.place(x=self.button_X,y = 1)
        self.FM_page.place(x=self.button_X,y = self.root_height/8+1)
        self.Music_page.place(x=self.button_X,y = self.root_height*2/8+1)
        self.Alarm_page.place(x=self.button_X,y = self.root_height*3/8+1)
        self.Scedule_page.place(x=self.button_X,y = self.root_height*4/8+1)
        self.Weather_page.place(x=self.button_X,y = self.root_height*5/8+1)
        self.Game_page.place(x=self.button_X,y = self.root_height*6/8+1)
        self.Setting_page.place(x=self.button_X,y = self.root_height*7/8+1)
        self.show_button.place(x=self.button_X+52,y = self.root_height*3.5/8+1)'''
        
        self.refresh()
        self.toolBar_Animation()
    
    def toolBar_Animation(self):
            th=threading.Thread(target=self.Animation)
            th.setDaemon(True)
            th.start()
            
    def Animation(self):
        global count
        global randomPlay
        song = list()
        song_point = 0
        run_time = 0
        song_animation_start = 0
        alarm_ID = 0
        temp_sel_musicList = "總清單"
        start_alarm=0
        while(1):
            #hide or show toolbar 
            if(count%2 == 1):
                self.hide()
            else:
                self.show()
    
            if(now_page==0):#homepage animation
                self.homepage.time()
                if(run_time == 0):
                    self.homepage.refresh_weather()                 
            
            elif(now_page == 1):
               self.FMpage.FM.FM_code = self.FMpage.FMlist.curselection()
               self.FMpage.FMtime()
                
            elif(now_page==2):
                self.musicButtonControl.switch()                    
                if temp_sel_musicList != (self.musicButtonControl.comboExample.get()):
                    temp_sel_musicList = (self.musicButtonControl.comboExample.get())
                    if(temp_sel_musicList == "總清單"):
                        self.musicButtonControl.switch_list(1)
                    elif(temp_sel_musicList == "播放清單1"):
                        self.musicButtonControl.switch_list(2)
                    elif(temp_sel_musicList == "播放清單2"):
                        self.musicButtonControl.switch_list(3)
                    elif(temp_sel_musicList == "播放清單3"):
                        self.musicButtonControl.switch_list(4)
                    elif(temp_sel_musicList == "播放清單4"):
                        self.musicButtonControl.switch_list(5)
                    elif(temp_sel_musicList == "播放清單5"):
                        self.musicButtonControl.switch_list(6)
                
            elif(now_page==3):#alarm animation
                s1 = "".join(self.alarm.alarm_song[self.alarm.now_detail_alarmID])
                if(not(alarm_ID==self.alarm.now_detail_alarmID and song == s1)):
                    self.alarm.now_song.config(text=s1)
                    song = s1
                    song_animation_start = 0
                    song_point = 0
                    alarm_ID = self.alarm.now_detail_alarmID
                elif(song_animation_start==0):
                    if(run_time%200==0):
                        song_animation_start = 1
                elif(run_time%20==0):
                    self.alarm.now_song.config(text=s1[song_point:len(s1)])
                    song_point+=1
                    if(song_point==len(s1)+1):
                        song_point=0
                        song_animation_start = 0
                self.alarm.FMtime()          
            
            elif(now_page == 4):
             self.CalendarPage.time()
             if self.CalendarPage.selmonth != int(self.CalendarPage.vMonth.get()):
                 self.CalendarPage.selmonth = int(self.CalendarPage.vMonth.get())
                 self.CalendarPage.updateDate()
            
            m = 0
            if(start_alarm or run_time == 199):
                if self.alarm.setting_zone == 0:
                    flag = m
                    flag = self.alarm.Alarming()
                    if flag == 0:
                        m = flag
                
                if self.alarm.ring_state == 1:
                    self.alarm.ring_label.config(text=" "+"".join(self.alarm.alarm_Name[flag])+" 正在響鈴")
                    self.switch_page(8)
                elif self.alarm.ring_state == 2:
                    print("123")
                    self.alarm.ring_frame.pack_forget()
                    self.switch_page(now_page)
                    self.alarm.ring_state = 0
                start_alarm = 1
                
            
            #self.test()   
            
            run_time=(run_time+1)%200 
            time.sleep(0.005)
            #label.config(text="GG")
        
    def switch_page(self, page_ID):
        global now_page
        if(now_page < 0):   
            now_page += 1
            return
        if(now_page == 0):
            self.homepage.hide_homepage()
        elif(now_page == 1):
            self.FMpage.hide_FMpage()
        elif(now_page==2):
            #self.musicList.hide_musiclist()
            self.musicButtonControl.hide_musicbuttoncontrol()
        elif(now_page == 3):
            self.alarm.hide_alarm()     
        elif(now_page == 4):
            self.CalendarPage.close_setting()
            self.CalendarPage.hide_calendarpage()       
        elif(now_page == 5):
            self.weather_page.hide_weather_page()
            
        if(page_ID == 0):
            self.homepage.show_homepage()
        elif(page_ID == 1):
            self.FMpage.show_FMpage()
        elif(page_ID == 2):
            #self.musicList.show_musiclist()
            self.musicButtonControl.show_musicbuttoncontrol()
        elif(page_ID == 3):
            self.alarm.show_alarm()
        elif(page_ID == 5):
            self.weather_page.show_weather_page()  
        elif(page_ID == 4):
            self.CalendarPage.show_calendarpage()      
        elif(page_ID == 8):
            self.alarm.ring_frame.pack(side = "top",pady = (100,0))
          
        if not page_ID == 8:
            now_page = page_ID
            
            
    def clickOK(self):
        global count
        count+=1
        #label.config(text="Click OK " + str(count) + " times")
        
    def refresh(self):
        self.Main_page.place(x=self.button_X,y = 1)
        self.FM_page.place(x=self.button_X,y = self.root_height/6+1)
        self.Music_page.place(x=self.button_X,y = self.root_height*2/6+1)
        self.Alarm_page.place(x=self.button_X,y = self.root_height*3/6+1)
        self.Scedule_page.place(x=self.button_X,y = self.root_height*4/6+1)
        self.Weather_page.place(x=self.button_X,y = self.root_height*5/6+1)
        #self.Game_page.place(x=self.button_X,y = self.root_height*6/8+1)
        #self.Setting_page.place(x=self.button_X,y = self.root_height*7/8+1)
        self.show_button.pack(side='left', padx = (self.button_X+52,0))        
        
    def hide(self):        
        if(self.button_X>-52):  
            self.button_X-=1
        #self.button_X = -52          
        self.show_button.config(text=">")
        self.refresh()
    
    def show(self): 
        if(self.button_X<0):
            self.button_X+=1
        #self.button_X = 0      
        self.show_button.config(text="<")
        self.refresh()
        
    def test(self):
        #global run_time, song_point, song_animation_start
        global now_page
        self.test_label.config(text=(self.alarm.ring_state))
        self.test_label.place(x=200,y=200)
        
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        