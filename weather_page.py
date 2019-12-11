# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:26:24 2019

@author: 阿新
"""
import tkinter as tk
from weather import *
from tkinter import ttk
from PIL import ImageTk,Image
from googletrans import Translator



                                      

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
        
        
        self.weather_frame = tk.Frame(self.main_frame,bg="black")
        self.weather_frame.pack()
        
        
        
        #canvas
        self.canvasWidth=int(self.root_height/5.1*7.6)
        self.canvasHeight=root_height
        
        self.lock = 0

        #Canvas image
        '''
        self.canvas=tk.Canvas(self.weather_frame,width=self.canvasWidth,height=self.canvasHeight)
        self.image = ImageTk.PhotoImage(Image.open("picture/world1.jpg"))
        self.canvas.create_image(0, 0, anchor=tk.NW,image=self.image)
        self.canvas.place(x=0,y=70)
        '''
        #button_image
        self.button_image=ImageTk.PhotoImage(Image.open('picture/button2.jpg'))
        #self.button_image.zoom(30,15)
        #city combo box
        self.on_hit=False
        self.on_hit2=False
        self.choose_the_city=False
        self.detail_frame = tk.Frame(self.weather_frame,width=self.root_width/2,height=self.root_height, relief="groove", borderwidth = 2,bg="black")#, highlightcolor="green", highlightthickness=5
        self.detail_frame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.1, anchor='n')
        self.detail_frame2 = tk.Frame(self.weather_frame,width=100,height=self.root_height,relief="groove", borderwidth = 2,bg="black")#, highlightcolor="green", highlightthickness=5
        self.detail_frame2.place(relx=0.5, rely=0.3, relwidth=0.9, relheight=0.4, anchor='n')
        
        self.city_dic={ "基隆市" : "Keelung", "臺北市" : "Taipei", "新北市" : "New Taipei", 
               "桃園市" : "Taoyuan", "新竹市" : "Hsinchu", "新竹縣" : "Hsinchu",
               "苗栗縣" : "Miaoli", "臺中市" : "Taichung", "彰化縣" : "Changhua", 
               "南投縣" : "Nantou", "雲林縣" :"Yunlin", "嘉義市" :"Chiayi", 
               "嘉義縣" :"Yilan", "宜蘭縣" :"Yilan", "花蓮縣" :"Hualien",
               "臺東縣" :"Taitung", "臺南市" :"Tainan", "高雄市" :"Kaohsiung",
               "屏東縣" :"Pingtung", "連江縣" :"Lianjiang", "金門縣" :"Jincheng", 
               "澎湖縣" :"Ma-kung","北京":"Beijing","東京":"Tokyo","首爾":"Seoul",
               "波士頓":"Boston","加拿大":"Canada","美國":"usa"}

        self.city_list=ttk.Combobox(self.detail_frame,values=[ "基隆市" , "臺北市" , "新北市" , "桃園市" , 
                                                              "新竹市" , "新竹縣" ,"苗栗縣" , "臺中市", "彰化縣",
                                                              "南投縣" , "雲林縣" , "嘉義市" ,"嘉義縣" , "宜蘭縣" ,
                                                              "花蓮縣" , "臺東縣" , "臺南市" , "高雄市" ,
                                                              "屏東縣" , "連江縣" , "金門縣" , "澎湖縣","北京",
                                                              "東京","首爾","波士頓","加拿大","美國"])
        self.city_list.current(0)
        self.city_list.bind("<<ComboboxSelected>>",self.go)

        #self.city_list.place(x=48.5,y=16.3,width=15,height=20) 
        self.city_list.place(relwidth=0.4, relheight=1.0)
        
        self.city_comfirm=tk.Button(self.detail_frame,text='查詢目前城市天氣',command=self.weather_detail,bg='black', foreground="white")
        #self.city_comfirm.place()
        self.city_comfirm.place(relx=0.4, relheight=1.0, relwidth=0.3)
        
        #self.city_set=ttk.Button(self.detail_frame,text='選擇',width=15,image=self.button_image,command=self.city_chosed)
        self.city_set=tk.Button(self.detail_frame,text='更改現居城市',width=15,command=self.city_chosed,bg='black', foreground="white")
        self.city_set.place(relx=0.7, relheight=1.0, relwidth=0.3)
        
        self.var = ""
        self.the_weather_detail=tk.Label(self.detail_frame2,text=self.var,font=('Arial',12),width=30,height=10,background='black', foreground="white")
        #self.weather_detail.place(x=360,y=61)
        self.the_weather_detail.pack(side="left")
        
        self.choose_the_city = True
        
       
        self.weather_detail()
        self.hide_weather_page()
        
        '''
        self.canvas=tk.Canvas(self.weather_frame,width=self.canvasWidth,height=self.canvasHeight)
        self.image = ImageTk.PhotoImage(Image.open("picture/world1.jpg"))
        self.canvas.create_image(0, 0, anchor=tk.NW,image=self.image)
        self.canvas.place(x=0,y=70)
        '''
       

    

    def trans_to_ch(self,en):
        self.en_translator=Translator()
        self.english=self.en_translator.translate(en,dest='zh-TW').text
        return self.english
    def go(self,*args):   #处理事件，*args表示可变参数
        self.c=self.city_dic[self.city_list.get()]
        self.weather.detail_change_city(self.c)
        self.choose_the_city=True
    def weather_detail(self):
        if self.choose_the_city==True:
            self.the_weather_detail.config(text = self.city_list.get()+"\n\n"+
               "天氣概況:"+self.trans_to_ch(self.weather.print_weather_description()['weather'][0]['description'])+"\n"+
               "溫度:"+str(self.weather.print_weather_description()['main']['temp_min'])+"~"+str(self.weather.print_weather_description()['main']['temp_max'])+"℃"+"\n"+
               "濕度:"+str(self.weather.print_weather_description()['main']['humidity'])
                )
            #icon
            self.weather_icon = tk.Canvas(self.detail_frame2, bg="white", bd=0, highlightthickness=0)
            self.icon_name = self.weather.icon_name2()
            self.size = int(self.detail_frame2.winfo_height())
            print(self.icon_name+"\n"+str(self.size))
            self.img = ImageTk.PhotoImage(Image.open('picture/'+self.icon_name+'.png'))
            self.weather_icon.delete("all")
            self.weather_icon.create_image(0,0, anchor='nw', image=self.img)
            self.weather_icon.place(relx=.75, rely=0.2, relwidth=0.15, relheight=0.4)
            self.choose_the_city=False
        else:
           self.the_weather_detail.config(text = "請選擇城市!")
            
        #print (self.city_list.get())
    def city_chosed(self):
        self.s=self.city_dic[self.city_list.get()]
        self.weather.change_city(self.s)
            
    def hide_weather_page(self):
        self.weather_frame.pack_forget()
        
    def show_weather_page(self):
        self.weather_frame.pack(side = "top",expand = True,fill=tk.BOTH)





