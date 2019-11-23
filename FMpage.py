# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:02:28 2019

@author: 士賢
"""
import tkinter as tk
import tkinter as ttk
import time
from tkinter import *
from FMlist import *




class FMpage():
    def __init__(self, root, main_frame, root_height):
        #page size
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.FM = FM()
        self.main_frame = main_frame
        
        #Label of time
        self.time_label=tk.Label(self.main_frame, text=time.strftime("%H:%M:%S", time.localtime()), font=("Arial",10))
        self.time_label.pack(anchor=tk.NE)
        #set button x,y 
        self.button_X = 0
        
        self.buttonmap = tk.Frame(self.main_frame)
        self.map = tk.Frame(self.buttonmap)
        self.buttonmap.pack(pady=50)
        self.map.pack(side='bottom')
      

        #FM list
        self.m = StringVar()
        self.FMlist= tk.Listbox(self.buttonmap,width=49,height=5,listvariable=self.m)
        self.FMlist.pack(side='left',fill=tk.X,pady=50)
        for item in range(20): 
            self.FM.FM_name_code=item
            self.FMlist.insert(tk.END, str(self.FM.print_FM_Name()))
        # 创建Scrollbar组件，设置该组件与self.lb的纵向滚动关联
        scroll = tk.Scrollbar( self.buttonmap, command=self.FMlist.yview)
        scroll.pack(side='left', fill=tk.Y,pady=50)
        # 设置self.lb的纵向滚动影响scroll滚动条
        self.FMlist.configure(yscrollcommand=scroll.set)
        # 为双击事件绑定事件处理方法
        self.FMlist.bind('<Double-1>', self.click)
         #tool button
        self.play=tk.Button(self.map, text="PLAY",command=self.FM.play_FM ,width=6, height=2).pack(side='right')
        self.stop=tk.Button(self.map, text="STOP",command=self.FM.stop_FM , width=6, height=2).pack(side='left',padx=50)
        self.hide_FMpage()
        
    def click(self, event):
        # 获取Listbox当前选中项
        self.FM.FM_code = self.FMlist.curselection()
        
    def FMtime(self):
        self.time_label.config(text=time.strftime("%H:%M:%S", time.localtime()))
        #self.date_label.config(text=time.strftime("%a %b %d", time.localtime()))
        
    def hide_FMpage(self):
        self.time_label.pack_forget()
        #self.date_label.place_forget()
        self.buttonmap.pack_forget()

    
    def show_FMpage(self):
        self.time_label.pack(anchor = tk.NE)
        self.buttonmap.pack(anchor = tk.NW)
        

       

    

 

        



