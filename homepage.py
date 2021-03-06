# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:33:24 2019

@author: User
"""
import tkinter as tk
from tkinter import ttk
import time
from weather import *
from PIL import ImageTk,Image

class Homepage():
    def __init__(self, root, main_frame, root_height, weather, CalendarPage):
        #page size
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.weather = weather
        self.homepage_pos = 0
        self.main_frame=main_frame
        self.CalendarPage = CalendarPage
        
        #time frame
        self.time_frame = tk.Frame(self.main_frame,bg = 'black')#, highlightcolor="green", highlightthickness=5
        self.time_frame.pack(anchor = tk.N, pady=(20,0))
        
        self.time2_frame = tk.Frame(self.time_frame,bg = 'black')#, highlightcolor="green", highlightthickness=5
                    
        #Label of time
        self.time_label=tk.Label(self.time_frame, text=time.strftime("%H:%M", time.localtime()), font=("Arial",100),background='black', foreground="white")#:%S
        self.time_label.pack(anchor = tk.N, padx = (0, 20))
        self.time2_frame.pack(anchor = tk.NW, padx=(20,0))
        self.date_label=tk.Label(self.time2_frame, text=time.strftime("%a  %b %d %Y", time.localtime()), font=("Arial",15),background='black', foreground="white")
        self.date_label.pack(side = 'left', padx = (20,0))
        
        self.play_image=ImageTk.PhotoImage(Image.open('picture/play.jpg'))
        self.message_icon = tk.Button(self.time2_frame,image=self.play_image,command=self.CalendarPage.play_daily_event, bg = 'black', relief = 'flat', activebackground = 'black', highlightbackground='black' )
        self.message_icon.pack(side = 'left', padx = (50,0))
        #weather frame
        self.weather_frame = tk.Frame(self.main_frame,bg = 'black')#, highlightcolor="green", highlightthickness=5
        self.weather_frame.pack(anchor = tk.S, fill = tk.X, pady = (20,0))
            
        
        #weather frame
        self.a = tk.Frame(self.weather_frame,bg = 'black')#, highlightcolor="green", highlightthickness=5
        self.a.pack(side = 'left', padx = (50,0))
            
        
        #Label of city_name
        self.cityName_label=tk.Label(self.a, text=weather.print_city(), font=("Arial",18),background='black', foreground="white")
        self.cityName_label.pack(anchor = tk.NW)
        
         #Label of city temp
        self.cityTemp_label=tk.Label(self.a, text=weather.print_night_temperature()+"℃", font=("Arial",18),background='black', foreground="white")
        self.cityTemp_label.pack(anchor = tk.NW, padx = (0,0))
        #icon        
        self.icon_name = self.weather.icon_name()
        self.img=ImageTk.PhotoImage(Image.open('picture/'+self.icon_name+'.jpg'))
        self.cityDayRainingRate_label=tk.Label(self.weather_frame, image=self.img,background='black', foreground="white")
        self.cityDayRainingRate_label.pack(side = 'right', padx = (50,70))
        
       
        
        self.Ncity = ""
        
        
    def time(self):
        self.time_label.config(text=time.strftime("%H:%M", time.localtime()))#:%S
        self.date_label.config(text=time.strftime("%a %b %d %Y", time.localtime()))
        
    def refresh_weather(self):
        if not(self.Ncity==self.weather.print_city()):
            self.cityName_label.config(text=self.weather.print_city())
            self.cityDayRainingRate_label.config(text="濕度\n"+self.weather.print_day_rain_percent()+"%")
        
    def hide_homepage(self):
        self.time_frame.pack_forget()
        self.weather_frame.pack_forget()
    
    def show_homepage(self):
        self.time_frame.pack(anchor = tk.N, pady=(20,0))
        self.weather_frame.pack(anchor = tk.S, fill = tk.X, pady = (20,0))
        