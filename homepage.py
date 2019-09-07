# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:33:24 2019

@author: User
"""
import tkinter as tk
from tkinter import ttk
import time
from weather2 import *

class Homepage():
    def __init__(self, root, root_height, weather):
        #page size
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.weather = weather
        self.homepage_pos = 0
        
        #Label of time
        self.time_label=tk.Label(self.root, text=time.strftime("%H:%M:%S", time.localtime()), font=("Arial",48))
        self.time_label.place(x=self.root_width//5,y = self.root_height//6)
        self.date_label=tk.Label(self.root, text=time.strftime("%a %b %d %Y", time.localtime()), font=("Arial",12))
        self.date_label.place(x=self.root_width//5,y = self.root_height//6+70)
        
        #Label of city_name
        self.cityName_label=ttk.Label(self.root, text=weather.print_city(), font=("Arial",12))
        self.cityName_label.place(x=self.root_width//5,y = self.root_height//6*4)
        
        #Label of city day raining rate
        self.cityDayRainingRate_label=tk.Label(self.root, text="降雨機率\n"+weather.print_day_rain_percent(), font=("Arial",12))
        self.cityDayRainingRate_label.place(x=self.root_width//5*4,y = self.root_height//6*4)
        
    def time(self):
        self.time_label.config(text=time.strftime("%H:%M:%S", time.localtime()))
        self.date_label.config(text=time.strftime("%a %b %d %Y", time.localtime()))
        
    def refresh_weather(self):
        self.cityName_label.config(text=self.weather.print_city())
        self.cityDayRainingRate_label.config(text="降雨機率\n"+self.weather.print_day_rain_percent())
        
    def hide_homepage(self):
        self.time_label.place_forget()
        self.date_label.place_forget()
        self.cityName_label.place_forget()
        self.cityDayRainingRate_label.place_forget()
    
    def show_homepage(self):
        self.time_label.place(x=self.root_width//5,y = self.root_height//6)
        self.date_label.place(x=self.root_width//5,y = self.root_height//6+70)
        self.cityName_label.place(x=self.root_width//5,y = self.root_height//6*4)
        self.cityDayRainingRate_label.place(x=self.root_width//5*4,y = self.root_height//6*4)
        