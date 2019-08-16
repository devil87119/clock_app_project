# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:07:35 2019

@author: User
"""

import tkinter as tk  
import homepage
import weather2

class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("大賢四代目")
        self.root_height = 326
        self.root_width = int(self.root_height/5.1*7.6)
        self.root.geometry(str(self.root_width)+"x"+str(self.root_height))
        self.toolbar = Toolbar(self.root,self.root_height)
        self.weather = Weather()
        self.homepage = Homepage(self.root,self.root_height,self.weather)
   

class Toolbar():
    def __init__(self, root, root_height):
        #toolbar button
        self.Main_page=tk.Button(root, text="MAIN", command=clickOK, width=6, height=2)
        self.FM_page=tk.Button(root, text="FM", command=clickOK, width=6, height=2)
        self.Music_page=tk.Button(root, text="Music", command=clickOK, width=6, height=2)
        self.Alarm_page=tk.Button(root, text="Alarm", command=clickOK, width=6, height=2)
        self.Scedule_page=tk.Button(root, text="Scedule", command=clickOK, width=6, height=2)
        self.Weather_page=tk.Button(root, text="Weather", command=clickOK, width=6, height=2)
        self.Game_page=tk.Button(root, text="Game", command=clickOK, width=6, height=2)
        self.Setting_page=tk.Button(root, text="Setting", command=clickOK, width=6, height=2)
        
        #set button x,y 
        self.button_X = 0
        self.root_height = root_height
        
        #buuton position
        self.Main_page.place(x=self.button_X,y = 1)
        self.FM_page.place(x=self.button_X,y = self.root_height/8+1)
        self.Music_page.place(x=self.button_X,y = self.root_height*2/8+1)
        self.Alarm_page.place(x=self.button_X,y = self.root_height*3/8+1)
        self.Scedule_page.place(x=self.button_X,y = self.root_height*4/8+1)
        self.Weather_page.place(x=self.button_X,y = self.root_height*5/8+1)
        self.Game_page.place(x=self.button_X,y = self.root_height*6/8+1)
        self.Setting_page.place(x=self.button_X,y = self.root_height*7/8+1)
        
    def refresh(self):
        self.Main_page.place(x=self.button_X,y = 1)
        self.FM_page.place(x=self.button_X,y = self.root_height/8+1)
        self.Music_page.place(x=self.button_X,y = self.root_height*2/8+1)
        self.Alarm_page.place(x=self.button_X,y = self.root_height*3/8+1)
        self.Scedule_page.place(x=self.button_X,y = self.root_height*4/8+1)
        self.Weather_page.place(x=self.button_X,y = self.root_height*5/8+1)
        self.Game_page.place(x=self.button_X,y = self.root_height*6/8+1)
        self.Setting_page.place(x=self.button_X,y = self.root_height*7/8+1)
        
        
    def hide(self):        
        if(self.button_X>-52):
           self.button_X-=1
        #self.button_X = -52
        self.refresh()
    
    def show(self): 
        if(self.button_X<0):
            self.button_X+=1
        #self.button_X = 0
        self.refresh()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        