# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:07:35 2019

@author: User
"""

import tkinter as tk  
#from test_GUI import *
from homepage import *
from weather2 import *
from alarm import *
import time
import threading

now_page = 0
count=0
Pages = [1, 0, 0, 0, 0, 0, 0, 0]

class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("大賢四代目")
        self.root_height = 326
        self.root_width = int(self.root_height/5.1*7.6)
        self.root.geometry(str(self.root_width)+"x"+str(self.root_height))
        self.weather = Weather()
        self.homepage = Homepage(self.root,self.root_height,self.weather)
        self.alarm = Alarm(self.root,self.root_height)
        self.toolbar = Toolbar(self.root,self.homepage, self.alarm, self.root_height)
    

class Toolbar():
    def __init__(self, root, homepage, alarm, root_height):   
        #set button x,y 
        self.button_X = 0
        self.root_height = root_height
        self.root = root
        self.homepage = homepage
        self.alarm = alarm
    
        #toolbar button
        self.Main_page=tk.Button(root, text="MAIN", command=lambda: self.switch_page(0), width=6, height=2)
        self.FM_page=tk.Button(root, text="FM", command=lambda: self.switch_page(1), width=6, height=2)
        self.Music_page=tk.Button(root, text="Music", command=lambda: self.switch_page(2), width=6, height=2)
        self.Alarm_page=tk.Button(root, text="Alarm", command=lambda: self.switch_page(3), width=6, height=2)
        self.Scedule_page=tk.Button(root, text="Scedule", command=lambda: self.switch_page(4), width=6, height=2)
        self.Weather_page=tk.Button(root, text="Weather", command=lambda: self.switch_page(5), width=6, height=2)
        self.Game_page=tk.Button(root, text="Game", command=lambda: self.switch_page(6), width=6, height=2)
        self.Setting_page=tk.Button(root, text="Setting", command=lambda: self.switch_page(7), width=6, height=2)
        self.show_button=tk.Button(root, text="<", command=self.clickOK)
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
        
        self.toolBar_Animation()
    
    def toolBar_Animation(self):
            th=threading.Thread(target=self.Animation)
            th.setDaemon(True)
            th.start()
            
    def Animation(self):
        global count
        while(1):
            #hide or show toolbar 
            if(count%2 == 1):
                self.hide()
            else:
                self.show()
            
            self.homepage.time()
            self.homepage.refresh_weather() 

            #self.test()                    
            
            time.sleep(0.005)
            #label.config(text="GG")
        
    def switch_page(self, page_ID):
        global now_page
        if(now_page < 0):   
            now_page += 1
            return
        if(now_page == 0):
            self.homepage.hide_homepage()
        if(now_page == 3):
            self.alarm.hide_alarm()
            
        if(page_ID == 0):
            self.homepage.show_homepage()
        if(page_ID == 3):
            self.alarm.show_alarm()
            
        now_page = page_ID
            
            
    def clickOK(self):
        global count
        count+=1
        #label.config(text="Click OK " + str(count) + " times")
        
    def refresh(self):
        self.Main_page.place(x=self.button_X,y = 1)
        self.FM_page.place(x=self.button_X,y = self.root_height/8+1)
        self.Music_page.place(x=self.button_X,y = self.root_height*2/8+1)
        self.Alarm_page.place(x=self.button_X,y = self.root_height*3/8+1)
        self.Scedule_page.place(x=self.button_X,y = self.root_height*4/8+1)
        self.Weather_page.place(x=self.button_X,y = self.root_height*5/8+1)
        self.Game_page.place(x=self.button_X,y = self.root_height*6/8+1)
        self.Setting_page.place(x=self.button_X,y = self.root_height*7/8+1)
        self.show_button.place(x=self.button_X+52,y = self.root_height*3.5/8+6)
        
        
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
        self.test_label.config(text=str(count)+"+"+str(now_page))
        self.test_label.pack(side='bottom')
        
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        