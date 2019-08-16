# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:33:24 2019

@author: User
"""
import tkinter as tk
import time
import weather2

class Homepage():
    def __init__(self, root, root_height, weather):
        #page size
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.weather = weather
        
        #Label of time
        self.time_label=tk.Label(self.root, text=time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), font=("Arial",20))
        self.time_label.place(x=self.root_width//5,y = self.root_height//6)
        
        #Label of city_name
        self.cityName_label=tk.Label(self.root, text=weather.print_city(), font=("Arial",12))
        self.cityName_label.place(x=self.root_width//5,y = self.root_height//6*4)
        
        #Label of city day raining rate
        self.cityDayRainingRate_label=tk.Label(self.root, text=weather.print_day_rain_percent(), font=("Arial",12))
        self.cityDayRainingRate_label.place(x=self.root_width//5*4,y = self.root_height//6*4)
        
    def time(self):
        self.time_label.config(text=time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))