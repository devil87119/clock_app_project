# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:26:24 2019

@author: 阿新
"""
import tkinter as tk
from weather import *
from tkinter import ttk
from PIL import ImageTk,Image

class weather_page:
    def __init__(self, root, main_frame, root_height,weather):
        #page size
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.main_frame = main_frame
        self.s="基隆市"
        self.c=""
        self.weather=weather
        
        
        self.weather_frame = tk.Frame(self.main_frame)
        self.weather_frame.pack()
        
        #canvas
        self.canvasWidth=int(self.root_height/5.1*7.6)
        self.canvasHeight=root_height
        
        self.lock = 0

        #Canvas image
        '''
        self.canvas=tk.Canvas(self.weather_frame,width=200,height=100)
        self.image = ImageTk.PhotoImage(Image.open("picture/city.jpg"))
        self.canvas.create_image(0, 0, anchor=tk.NW,image=self.image)
        self.canvas.place(x=100,y=100)
'''
        #city combo box
        self.on_hit=False
        self.on_hit2=False
        self.choose_the_city=False
        self.detail_frame = tk.Frame(self.weather_frame,width=self.root_width/2,height=self.root_height, relief="groove", borderwidth = 2)#, highlightcolor="green", highlightthickness=5
        self.detail_frame.pack(side="left",expand = True,fill=tk.BOTH)
        self.detail_frame2 = tk.Frame(self.weather_frame,width=100,height=self.root_height,relief="groove", borderwidth = 2)#, highlightcolor="green", highlightthickness=5
        self.detail_frame2.pack(side="left",expand = True,fill=tk.BOTH)

        self.city_list=ttk.Combobox(self.detail_frame,values=["基隆市", "臺北市", "新北市" , "桃園市", "新竹市", 
                                      "新竹縣","苗栗縣" , "臺中市" , "彰化縣", "南投縣",
                                      "雲林縣" , "嘉義市" ,"嘉義縣", "宜蘭縣", "花蓮縣" , 
                                      "臺東縣", "臺南市" , "高雄市","屏東縣", "連江縣", 
                                      "金門縣", "澎湖縣"],state='新北市')
        self.city_list.bind("<<ComboboxSelected>>",self.go)

        #self.city_list.place(x=48.5,y=16.3,width=15,height=20) 
        self.city_list.pack(anchor=tk.NW,padx=(10,10))
        
        self.city_comfirm=ttk.Button(self.detail_frame,text='查詢目前城市天氣',width=15,command=self.weather_detail)
        #self.city_comfirm.place()
        self.city_comfirm.pack(anchor=tk.NW,padx=(10,10))
        
        self.city_set=ttk.Button(self.detail_frame,text='選擇',width=15,command=self.city_chosed)
        self.city_set.pack(anchor=tk.NW,padx=(10,10))
        
        self.var = ""
        self.weather_detail=tk.Label(self.detail_frame2,text=self.var,font=('Arial',12),width=15,height=10)
        #self.weather_detail.place(x=360,y=61)
        self.weather_detail.pack()
       

        self.hide_weather_page()
    def go(self,*args):   #处理事件，*args表示可变参数
        self.c=self.city_list.get()
        self.weather.detail_change_city(self.c)
        self.choose_the_city=True
    def weather_detail(self):
        if self.choose_the_city==True:
            self.weather_detail.config(text = self.city_list.get()+"\n\n"+
                "今晚明晨:"+"\n"+self.weather.print_night_temperature2()+"\n"+
                "明日白天:"+"\n"+self.weather.print_day_temperature2()+"\n"+
                "今晚明晨降雨機率:"+"\n"+self.weather.print_night_rain_percent2()+"\n"+
                "明日白天降雨機率:"+"\n"+self.weather.print_day_rain_percent2()
                )
            self.choose_the_city=False
        else:
           self.weather_detail.config(text = "請選擇城市!")
            
        #print (self.city_list.get())
    def city_chosed(self):
        self.s=self.city_list.get()
        self.weather.change_city(self.s)
            
    def hide_weather_page(self):
        #self.canvas.place_forget()
        '''
        self.weather_detail.place_forget()
        self.city_comfirm.place_forget()
        self.city_list.place_forget()
        '''
        '''
        self.detail_frame.pack_forget()
        self.detail_frame2.pack_forget()
        
'''
        self.weather_frame.pack_forget()
    def show_weather_page(self):
        #self.main_frame.pack(fill = tk.BOTH)
        #self.canvas.place(x=0,y=0)
        '''
        self.weather_detail.place(x=360,y=61)
        self.city_comfirm.place(x=40,y=46)
        self.city_list.place(x=48.5,y=16.3,width=100,height=20)
        '''
        '''
        self.detail_frame.pack(side="left")
        self.detail_frame2.pack(side="right")
'''
        self.weather_frame.pack(side = "top",expand = True,fill=tk.BOTH)





