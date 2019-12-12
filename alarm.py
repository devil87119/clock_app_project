# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:52:48 2019

@author: 楊秉翰
"""

import tkinter as tk
from tkinter import ttk 
import time
import os

class Alarm:
    def __init__(self, root, main_frame, root_height, musiclist):
        #page size
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.main_frame = main_frame
        self.musiclist = musiclist
        
        #alarm attribute
        self.alarm_activate = dict()#0 : 關閉,  1: 啟動
        self.detail_hour = dict()#設定鬧鐘時間
        self.detail_min = dict()#設定鬧鐘時間
        self.detail_sec = dict()#設定鬧鐘時間
        self.alarm_song = dict()#設定歌曲
        self.alarm_ring_time = [10, 30, 60, 120]#響鈴時間
        self.alarm_repeat = [0, 3, 5, 10000]#重複次數
        self.alarm_RingTime = dict()
        self.alarm_Repeat = dict()
        self.alarm_Name = dict()
        self.first = 0
        self.N_ringing = dict()#正在響鈴
        self.setting_zone = 0#正在設定
        
        
        self.gui_style = ttk.Style()
        self.gui_style.configure('black.TFrame', foreground='white', background = 'black')
        self.gui_style.configure('black.TLabel', foreground='white', background = 'black')
        
        self.R_style = ttk.Style()
        self.R_style.configure('Radio_style.TRadiobutton', foreground='white', background = 'black')
        
        for i in range(6):
            self.N_ringing[i] = 0
        
        self.alarm_temp_hr = dict()#站存鬧鈴時間
        self.alarm_temp_min = dict()
        self.alarm_temp_sec = dict()
        self.alarm_temp_hr[0]=0
        self.alarm_temp_min[0]=0
        self.alarm_temp_sec[0]=0
        self.now_detail_alarmID = 0
                
        self.setting_frame= ttk.Frame(self.main_frame, style = 'black.TFrame')
        self.setting_frame.pack(side='top', fill=tk.BOTH)
        
        self.N_alarm = 0
        #alarm 1~6 frame
        self.alarm_frame = ttk.Frame(self.setting_frame, style = 'black.TFrame')
        
        #alarm 1~6 frame
        self.alarm_top_frame = ttk.Frame(self.alarm_frame, style = 'black.TFrame')        
        self.alarm_top_frame.pack(anchor=tk.S)
        
        #alarm 1~6 frame
        self.alarm_low_frame = ttk.Frame(self.alarm_frame, style = 'black.TFrame')        
        self.alarm_low_frame.pack(anchor=tk.S, pady=(0,0))
        
        #alarm 1~6 init
        big_button_Style = ttk.Style ()
        big_button_Style.configure("big.TButton", font = ('Arial','10'))
        big_button_Style.map('big.TButton', foreground = [('pressed','SlateBlue3'),('active', 'black'),('!disabled','white')], background = [('pressed','red'),('active', 'red'),('!disabled','red')]) 
        self.Alarm1=tk.Button(self.alarm_top_frame, text="Alarm 1", command=lambda: self.switch(0), width=10, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.Alarm2=tk.Button(self.alarm_top_frame, text="Alarm 2", command=lambda: self.switch(1), width=10, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.Alarm3=tk.Button(self.alarm_top_frame, text="Alarm 3", command=lambda: self.switch(2), width=10, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.Alarm4=tk.Button(self.alarm_top_frame, text="Alarm 4", command=lambda: self.switch(3), width=10, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.Alarm5=tk.Button(self.alarm_low_frame, text="Alarm 5", command=lambda: self.switch(4), width=10, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.Alarm6=tk.Button(self.alarm_low_frame, text="Alarm 6", command=lambda: self.switch(5), width=10, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        
        #place alarm 1~6 init        
        self.Alarm1.pack(side='left', padx=10,pady=(10,0))
        self.Alarm2.pack(side='left', padx=10,pady=(10,0))#(x=self.root_width/4*2,y = self.root_height/8*6)
        self.Alarm3.pack(side='left', padx=10,pady=(10,0))#(x=self.root_width/4*3,y = self.root_height/8*6)
        self.Alarm4.pack(side='left', padx=10,pady=(10,0))#(x=self.root_width/4,y = self.root_height/8*7)
        #self.Alarm5.pack(side='left', padx=20)#(x=self.root_width/4*2,y = self.root_height/8*7)
        #self.Alarm6.pack(side='left', padx=20)#(x=self.root_width/4*3,y = self.root_height/8*7)
        
        self.init_alarm()
        
        #time
        self.time_label=tk.Label(self.root, text=time.strftime("%H:%M:%S", time.localtime()), font=("Arial",10), background = 'black', foreground = 'white')
        self.time_label.place(y = 2, x = self.root_width - 60 )
        
        #detail of alarm
        ttk.Style().configure('Font.TLabelframe.Label', font = '25')#, foreground = "red"
        self.detail_frame = ttk.Frame(self.setting_frame, borderwidth=2, relief="groove", style = 'black.TFrame')#, highlightcolor="green", highlightthickness=5
        self.detail_frame.pack(anchor=tk.NW,pady=(2, 0),padx=(10,10))
        self.alarm_frame.pack(anchor=tk.CENTER,pady=(2, 0))
        
        #left detial frame
        self.left_frame = ttk.Frame(self.detail_frame, style = 'black.TFrame')        
        self.left_frame.pack(side = 'left')
        
        #Right detial frame
        self.right_frame = ttk.Frame(self.detail_frame, style = 'black.TFrame')        
        self.right_frame.pack(side = 'top', padx = (10,0))
        
        #on off frame
        self.activate_frame = ttk.Frame(self.left_frame, style = 'black.TFrame')        
        self.activate_frame.pack(anchor=tk.NW, padx = 10,pady=(2,0), expand = True, fill = tk.X) 
        
        #alarm name
        self.Alarm_name_label = ttk.Label(self.activate_frame, text = "".join(self.alarm_Name[0]), font=("Arial",14 ), style = 'black.TLabel')        
        self.Alarm_name_label.pack(side ="left",pady = (0,0))
                                       
        #ON/OFF   
        self.on = tk.IntVar()
        self.on.set(self.alarm_activate[0]) 
        self.ON_OFF_1 = ttk.Radiobutton(self.activate_frame, text="ON", variable=self.on, value=0, command=lambda: self.set_ONOFF(0), style = 'Radio_style.TRadiobutton')
        self.ON_OFF_2 = ttk.Radiobutton(self.activate_frame, text="OFF", variable=self.on, value=1, command=lambda: self.set_ONOFF(1), style = 'Radio_style.TRadiobutton')
        self.ON_OFF_2.pack(side ="right")
        self.ON_OFF_1.pack(side ="right")
        
        #time_frame
        self.time_frame = ttk.Frame(self.left_frame, style = 'black.TFrame')        
        self.time_frame.pack(anchor=tk.NW, pady = (0,0))
        
        
        #time top button frame
        self.time_plus_frame = ttk.Frame(self.time_frame, style = 'black.TFrame')        
        self.time_plus_frame.pack(side='left')
        
        #plus time
        little_button_Style = ttk.Style ()
        little_button_Style.configure("little.TButton", font = ('Sans','10'))
        self.alarm_plus_hour = tk.Button(self.time_plus_frame, text="+", command=lambda: self.adjust_alarm(0,1), width=2, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.alarm_plus_hour.pack(anchor=tk.NW)
        self.alarm_minus_hour = tk.Button(self.time_plus_frame, text="-", command=lambda: self.adjust_alarm(0,-1), width=2, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.alarm_minus_hour.pack(anchor=tk.NW)                
        
        #set alarm time         
        self.alarm_set_hour = tk.Label(self.time_frame, text=str(self.detail_hour[0]).zfill(2)+" : "+str(self.detail_min[0]).zfill(2), font=("Arial",36), bg = 'black', foreground = 'white')
        self.alarm_set_hour.pack(side='left')        
        
        #time bottom button frame
        self.time_minus_frame = ttk.Frame(self.time_frame, style = 'black.TFrame')        
        self.time_minus_frame.pack(side='left')
        
        #minus time
        self.alarm_plus_hour = tk.Button(self.time_minus_frame, text="+", command=lambda: self.adjust_alarm(1,1), width=2, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.alarm_plus_hour.pack(anchor=tk.NW, padx = 0)        
        self.alarm_minus_hour = tk.Button(self.time_minus_frame, text="-", command=lambda: self.adjust_alarm(1,-1), width=2, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.alarm_minus_hour.pack(anchor=tk.NW, padx = 0)
        
        #鬧鐘持續時間
        self.ringing_time_label = ttk.Label(self.left_frame, text = "鬧鐘持續時間", font=("Arial",10), style = 'black.TLabel')        
        self.ringing_time_label.pack(anchor=tk.NW, pady = (0,0))
        
        #ringing time frame
        self.ring_time_frame = ttk.Frame(self.left_frame, style = 'black.TFrame')        
        self.ring_time_frame.pack(anchor=tk.NW, padx = 10)                
        
        #ringing time option
        self.v = tk.IntVar()
        self.v.set(self.alarm_RingTime[0]) 
        self.ringtime_1 = ttk.Radiobutton(self.ring_time_frame, text=str(self.alarm_ring_time[0])+"s", variable=self.v, value=0, command=lambda: self.set_ring_time(0), style = 'Radio_style.TRadiobutton')
        self.ringtime_2 = ttk.Radiobutton(self.ring_time_frame, text=str(self.alarm_ring_time[1])+"s", variable=self.v, value=1, command=lambda: self.set_ring_time(1), style = 'Radio_style.TRadiobutton')
        self.ringtime_3 = ttk.Radiobutton(self.ring_time_frame, text="1m", variable=self.v, value=2, command=lambda: self.set_ring_time(2), style = 'Radio_style.TRadiobutton')
        self.ringtime_4 = ttk.Radiobutton(self.ring_time_frame, text="2m", variable=self.v, value=3, command=lambda: self.set_ring_time(3), style = 'Radio_style.TRadiobutton')
        self.ringtime_1.pack(side='left')
        self.ringtime_2.pack(side='left')
        self.ringtime_3.pack(side='left')
        self.ringtime_4.pack(side='left')
        
        #鬧鐘重複次數
        self.alarm_repeat_label = ttk.Label(self.left_frame, text = "鬧鐘重複次數", font=("Arial",10), style = 'black.TLabel')        
        self.alarm_repeat_label.pack(anchor=tk.NW, pady = (1,0))  
        
        #repeat time frame
        self.repeat_frame = ttk.Frame(self.left_frame, style = 'black.TFrame')        
        self.repeat_frame.pack(anchor=tk.NW, padx = 10)              
        
        #repeat time option
        self.w0 = tk.IntVar()
        self.w1 = tk.IntVar()
        self.w2 = tk.IntVar()
        self.w3 = tk.IntVar()
        self.w4 = tk.IntVar()
        self.w5 = tk.IntVar()
        self.w6 = tk.IntVar()
        self.week_code = self.alarm_Repeat[0]
        self.w0.set(self.week_code//64)
        self.week_code%=64
        self.w1.set(self.week_code//32) 
        self.week_code%=32
        self.w2.set(self.week_code//16) 
        self.week_code%=16
        self.w3.set(self.week_code//8) 
        self.week_code%=8
        self.w4.set(self.week_code//4) 
        self.week_code%=4
        self.w5.set(self.week_code//2) 
        self.week_code%=2
        self.w6.set(self.week_code//1) 
        self.week_frame = ttk.Frame(self.left_frame, style = 'black.TFrame')
        self.repeattime_1 = ttk.Checkbutton(self.repeat_frame, text=" 日 ", variable=self.w0, onvalue=1, offvalue=0, command=lambda: self.set_repeat_time(0), style = 'Radio_style.TRadiobutton')
        self.repeattime_2 = ttk.Checkbutton(self.repeat_frame, text=" 一 ", variable=self.w1, onvalue=1, offvalue=0, command=lambda: self.set_repeat_time(1), style = 'Radio_style.TRadiobutton')
        self.repeattime_3 = ttk.Checkbutton(self.repeat_frame, text=" 二 ", variable=self.w2, onvalue=1, offvalue=0, command=lambda: self.set_repeat_time(2), style = 'Radio_style.TRadiobutton')
        self.repeattime_4 = ttk.Checkbutton(self.repeat_frame, text=" 三 ", variable=self.w3, onvalue=1, offvalue=0, command=lambda: self.set_repeat_time(3), style = 'Radio_style.TRadiobutton')
        self.repeattime_5 = ttk.Checkbutton(self.week_frame, text=" 四 ", variable=self.w4, onvalue=1, offvalue=0, command=lambda: self.set_repeat_time(4), style = 'Radio_style.TRadiobutton')
        self.repeattime_6 = ttk.Checkbutton(self.week_frame, text=" 五 ", variable=self.w5, onvalue=1, offvalue=0, command=lambda: self.set_repeat_time(5), style = 'Radio_style.TRadiobutton')
        self.repeattime_7 = ttk.Checkbutton(self.week_frame, text=" 六 ", variable=self.w6, onvalue=1, offvalue=0, command=lambda: self.set_repeat_time(6), style = 'Radio_style.TRadiobutton')
        self.repeattime_1.pack(side='left')
        self.repeattime_2.pack(side='left')
        self.repeattime_3.pack(side='left')
        self.repeattime_4.pack(side='left')
        self.week_frame.pack(anchor = tk.NW,padx = (25,0))
        self.repeattime_5.pack(side='left')
        self.repeattime_6.pack(side='left')
        self.repeattime_7.pack(side='left')
        
        #鬧鐘歌曲
        self.alarm_song_label = ttk.Label(self.left_frame, text = "鬧鐘鈴聲", font=("Arial",10), style = 'black.TLabel')        
        self.alarm_song_label.pack(anchor=tk.NW, pady = (2,0))  
        self.now_song = ttk.Label(self.left_frame, text="".join(self.alarm_song[0]), width = 25, background = 'white')
        self.now_song.pack(anchor=tk.NW, padx = (10,0),pady = (0,2))
        
        #鬧鐘清單
        self.alarm_song_label = ttk.Label(self.right_frame, text = "鬧鐘歌曲清單", font=("Arial",10), style = 'black.TLabel')       
        self.alarm_song_label.pack(anchor=tk.NW, pady = (5,0))  
        self.song_frame = ttk.Frame(self.right_frame, height = 100, style = 'black.TFrame')
        self.scroll_frame = ttk.Frame(self.song_frame, height = 100, style = 'black.TFrame')
        self.scroll_frame.pack(side='right',expand=True,fill = tk.Y)
        self.song_frame.pack(anchor=tk.NW)       
        self.alarm_song_label.pack(anchor=tk.NW, pady = (5,0))  
        self.lv= tk.StringVar()
        self.listBox= tk.Listbox(self.song_frame,selectmode=tk.BROWSE,listvariable=self.lv, width = 30, height = 10)
        self.listBox.pack(anchor=tk.NW, padx = (10,0))
        
        # 创建Scrollbar组件，设置该组件与self.lb的纵向滚动关联
        scroll = tk.Scrollbar( self.scroll_frame, command=self.listBox.yview)
        scroll.pack(side='left', fill=tk.Y,pady=0,padx=(0,0))
        # 设置self.lb的纵向滚动影响scroll滚动条
        self.listBox.configure(yscrollcommand=scroll.set)
        # 为双击事件绑定事件处理方法
        self.listBox.bind('<Double-1>', self.change_ring)
        
        #function frame
        self.function_frame = ttk.Frame(self.right_frame, style = 'black.TFrame')        
        self.function_frame.pack(anchor=tk.NE, padx = 0, fill=tk.X)   
        self.cancel=tk.Button(self.function_frame, text="取消離開", command=self.hide_setting, width=8, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.save=tk.Button(self.function_frame, text="保存", command=self.save, width=4, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.save.pack(side = "right")
        self.cancel.pack(side = "right")
        self.alarm_tool_label = ttk.Label(self.function_frame, text = "未修改", font=("Arial",10), style = 'black.TLabel')       
        self.alarm_tool_label.pack(side="left", padx = (10,0))
        
        #table frame        
        self.table_frame = tk.Frame(self.main_frame,bg = 'black') 
        self.table_frame.pack(side = "top")
        
        
        #head_frame
        self.head_frame = tk.Frame(self.table_frame,bg = 'black') 
        self.head_frame.pack(side = "top", pady = (50,30))
        
        #every_alarm_frame 1
        self.A1 = tk.Frame(self.head_frame, relief="groove" , borderwidth=2, background = 'black' ) 
        self.A1.pack(side = "left", padx = (0,10))
        self.A1_sm_frame = tk.Frame(self.A1, background = 'black') 
        self.A1_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A1_label = ttk.Label(self.A1_sm_frame, text = "".join(self.alarm_Name[0]), font=("Arial",10), style = 'black.TLabel')
        self.A1_label.pack(side = "left")        
        self.A1_ON_OFF_1 = ttk.Label(self.A1_sm_frame, text="ON" if self.alarm_activate[0] == 0 else "OFF", font=("Arial",12), style = 'black.TLabel')
        self.A1_ON_OFF_1.pack(side ="right")
        self.A1_2_frame = tk.Frame(self.A1, background = 'black') 
        self.A1_2_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A1_time_label= ttk.Label(self.A1_2_frame, text=str(self.detail_hour[0]).zfill(2)+" : "+str(self.detail_min[0]).zfill(2), font=("Arial",16), style = 'black.TLabel')
        self.A1_time_label.pack(side = 'left') 
        self.A1_week_label= ttk.Label(self.A1_2_frame, text="", font=("Arial",10), style = 'black.TLabel')
        self.A1_week_label.pack(side = 'right')
        self.A1_song = ttk.Label(self.A1, text="".join(self.alarm_song[0]), width = 25, background = 'white')
        self.A1_song.pack(anchor=tk.NW)
        
        #every_alarm_frame 2
        self.A2 = tk.Frame(self.head_frame, relief="groove" , borderwidth=2, background = 'black' ) 
        self.A2.pack(side = "left")
        self.A2_sm_frame = tk.Frame(self.A2, background = 'black') 
        self.A2_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A2_label = ttk.Label(self.A2_sm_frame, style = 'black.TLabel', text = "".join(self.alarm_Name[1]), font=("Arial",10))
        self.A2_label.pack(side = "left")        
        self.A2_ON_OFF_1 = ttk.Label(self.A2_sm_frame, style = 'black.TLabel', text="ON" if self.alarm_activate[1] == 0 else "OFF", font=("Arial",12))
        self.A2_ON_OFF_1.pack(side ="right")
        self.A2_2_frame = tk.Frame(self.A2, background = 'black') 
        self.A2_2_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A2_time_label= ttk.Label(self.A2_2_frame, style = 'black.TLabel', text=str(self.detail_hour[1]).zfill(2)+" : "+str(self.detail_min[1]).zfill(2), font=("Arial",16))
        self.A2_time_label.pack(side = 'left') 
        self.A2_week_label= ttk.Label(self.A2_2_frame, style = 'black.TLabel', text="", font=("Arial",10))
        self.A2_week_label.pack(side = 'right') 
        self.A2_song = ttk.Label(self.A2, text="".join(self.alarm_song[1]), width = 25, background = 'white')
        self.A2_song.pack(anchor=tk.NW)
        
        #mid_frame
        self.mid_frame = tk.Frame(self.table_frame,bg = 'black') 
        self.mid_frame.pack(side = "top", pady = (0,10))
        
        #every_alarm_frame 3
        self.A3 = tk.Frame(self.mid_frame, relief="groove" , borderwidth=2, background = 'black' ) 
        self.A3.pack(side = "left", padx = (0,10))
        self.A3_sm_frame = tk.Frame(self.A3, background = 'black') 
        self.A3_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A3_label = ttk.Label(self.A3_sm_frame, style = 'black.TLabel', text = "".join(self.alarm_Name[2]), font=("Arial",10))
        self.A3_label.pack(side = "left")        
        self.A3_ON_OFF_1 = ttk.Label(self.A3_sm_frame, style = 'black.TLabel', text="ON" if self.alarm_activate[2] == 0 else "OFF", font=("Arial",12))
        self.A3_ON_OFF_1.pack(side ="right")
        self.A3_2_frame = tk.Frame(self.A3, background = 'black') 
        self.A3_2_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A3_time_label= ttk.Label(self.A3_2_frame, style = 'black.TLabel', text=str(self.detail_hour[2]).zfill(2)+" : "+str(self.detail_min[2]).zfill(2), font=("Arial",16))
        self.A3_time_label.pack(side = 'left') 
        self.A3_week_label= ttk.Label(self.A3_2_frame, style = 'black.TLabel', text="", font=("Arial",10))
        self.A3_week_label.pack(side = 'right')  
        self.A3_song = ttk.Label(self.A3, text="".join(self.alarm_song[2]), width = 25, background = 'white')
        self.A3_song.pack(anchor=tk.NW)
        
        #every_alarm_frame 4
        self.A4 = tk.Frame(self.mid_frame, relief="groove" , borderwidth=2, background = 'black' ) 
        self.A4.pack(side = "left")
        self.A4_sm_frame = tk.Frame(self.A4, background = 'black') 
        self.A4_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A4_label = ttk.Label(self.A4_sm_frame, style = 'black.TLabel', text = "".join(self.alarm_Name[3]), font=("Arial",10))
        self.A4_label.pack(side = "left")        
        self.A4_ON_OFF_1 = ttk.Label(self.A4_sm_frame, style = 'black.TLabel', text="ON" if self.alarm_activate[3] == 0 else "OFF", font=("Arial",12))
        self.A4_ON_OFF_1.pack(side ="right")
        self.A4_2_frame = tk.Frame(self.A4, background = 'black') 
        self.A4_2_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A4_time_label= ttk.Label(self.A4_2_frame, style = 'black.TLabel', text=str(self.detail_hour[3]).zfill(2)+" : "+str(self.detail_min[3]).zfill(2), font=("Arial",16))
        self.A4_time_label.pack(side = 'left') 
        self.A4_week_label= ttk.Label(self.A4_2_frame, style = 'black.TLabel', text="", font=("Arial",10))
        self.A4_week_label.pack(side = 'right')
        self.A4_song = ttk.Label(self.A4, text="".join(self.alarm_song[3]), width = 25, background = 'white')
        self.A4_song.pack(anchor=tk.NW)
        
        
        #mid_frame
        self.ft_frame = tk.Frame(self.table_frame,bg = 'black') 
        #self.ft_frame.pack(side = "top")
        
        #every_alarm_frame 5
        self.A5 = tk.Frame(self.ft_frame, relief="groove" , borderwidth=2, background = 'black' ) 
        self.A5.pack(side = "left", padx = (0,10))
        self.A5_sm_frame = tk.Frame(self.A5, background = 'black') 
        self.A5_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A5_label = ttk.Label(self.A5_sm_frame, style = 'black.TLabel', text = "".join(self.alarm_Name[4]), font=("Arial",10))
        self.A5_label.pack(side = "left")        
        self.A5_ON_OFF_1 = ttk.Label(self.A5_sm_frame, style = 'black.TLabel', text="ON" if self.alarm_activate[4] == 0 else "OFF", font=("Arial",12))
        self.A5_ON_OFF_1.pack(side ="right")
        self.A5_2_frame = tk.Frame(self.A5, background = 'black') 
        self.A5_2_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A5_time_label= ttk.Label(self.A5_2_frame, style = 'black.TLabel', text=str(self.detail_hour[4]).zfill(2)+" : "+str(self.detail_min[4]).zfill(2), font=("Arial",16))
        self.A5_time_label.pack(side = 'left') 
        self.A5_week_label= ttk.Label(self.A5_2_frame, style = 'black.TLabel', text="", font=("Arial",10))
        self.A5_week_label.pack(side = 'right')   
        self.A5_song = ttk.Label(self.A5, text="".join(self.alarm_song[4]), width = 25, background = 'white')
        self.A5_song.pack(anchor=tk.NW)
        
        #every_alarm_frame 6 
        self.A6 = tk.Frame(self.ft_frame, relief="groove" , borderwidth=2, background = 'black' ) 
        self.A6.pack(side = "left")
        self.A6_sm_frame = tk.Frame(self.A6, background = 'black') 
        self.A6_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A6_label = ttk.Label(self.A6_sm_frame, style = 'black.TLabel', text = "".join(self.alarm_Name[5]), font=("Arial",10))
        self.A6_label.pack(side = "left")        
        self.A6_ON_OFF_1 = ttk.Label(self.A6_sm_frame, style = 'black.TLabel', text="ON" if self.alarm_activate[5] == 0 else "OFF", font=("Arial",12))
        self.A6_ON_OFF_1.pack(side ="right")
        self.A6_2_frame = tk.Frame(self.A6, background = 'black') 
        self.A6_2_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A6_time_label= ttk.Label(self.A6_2_frame, style = 'black.TLabel', text=str(self.detail_hour[5]).zfill(2)+" : "+str(self.detail_min[5]).zfill(2), font=("Arial",16))
        self.A6_time_label.pack(side = 'left') 
        self.A6_week_label= ttk.Label(self.A6_2_frame, style = 'black.TLabel', text="", font=("Arial",10))
        self.A6_week_label.pack(side = 'right')
        self.A6_song = ttk.Label(self.A6, text="".join(self.alarm_song[5]), width = 25, background = 'white')
        self.A6_song.pack(anchor=tk.NW)
        
        self.set=tk.Button(self.table_frame, text="設定", command=self.show_setting, width=15, bg = 'black', foreground = 'white', activebackground = 'black',highlightbackground = 'white')
        self.set.pack(anchor = tk.SE, pady = (25,10), padx = (0,25))
        
        self.ring_state = 0
        self.ring_frame = tk.Frame(self.main_frame)
        self.ring_label = ttk.Label(self.ring_frame, text="", font=("Arial",16))
        self.ring_label.pack(anchor = tk.N, pady = (10,0),padx = (20,20))
        self.ring_stop_button= ttk.Button(self.ring_frame,text="關閉",command=self.stop_music,width=8, style = "big.TButton")#,bg='#FFEC8B'
        self.ring_stop_button.pack(anchor = tk.N, pady = (20,10))
        
        self.refreshMusiclist()
        
        self.setting_frame.pack_forget()
        self.hide_alarm()
        
    def stop_music(self):
        self.ring_state = 2
        self.musiclist.stopMusic()
        
    def init_alarm(self):
        point = 0
        fp = open('alarm/alarm_init.txt', "r",encoding="utf-8")
        line = fp.readline()
        while line:
            if(point < 6):
                self.alarm_activate[point] = int(line.replace('\n', ''))
            elif(point < 12):
                a = line.replace('\n', '')
                b = a.split()
                self.detail_hour[point-6] = int(b[0])
                self.detail_min[point-6] = int(b[1])
            elif(point < 18):
                self.alarm_song[point-12] = list(line.replace('\n', ''))
            elif(point < 24):
                self.alarm_RingTime[point-18] = int(line.replace('\n', ''))
            elif(point < 30):
                self.alarm_Repeat[point-24] = int(line.replace('\n', ''))
            elif(point < 36):
                self.alarm_Name[point-30] = list(line.replace('\n', ''))
            #print line
            line = fp.readline()
            point+=1
        fp.close()
        if(not(self.first == 0)):
            self.cancel_hint()
        self.first = 1
        
    def cancel_hint(self):
        self.alarm_tool_label.config(text = "已取消")     
        self.switch(self.N_alarm)
        
    def save(self):
        point = 0
        fp = open('alarm/alarm_init.txt', "w+",encoding="utf-8")
        for i in range(0,36):
            if(point < 6):
                fp.writelines(str(self.alarm_activate[point]))
                fp.writelines("\n")
            elif(point < 12):
                fp.writelines(str(self.detail_hour[point-6]).zfill(2)+" "+str(self.detail_min[point-6]).zfill(2))
                fp.writelines("\n")
            elif(point < 18):
                fp.writelines((self.alarm_song[point-12]))
                fp.writelines("\n")
            elif(point < 24):
                fp.writelines(str(self.alarm_RingTime[point-18]))
                fp.writelines("\n")
            elif(point < 30):
                fp.writelines(str(self.alarm_Repeat[point-24]))
                fp.writelines("\n")
            elif(point < 36):
                fp.writelines((self.alarm_Name[point-30]))
                fp.writelines("\n")
            point+=1
        fp.close()
        self.alarm_tool_label.config(text = "已保存")
        self.hide_setting()
        #self.Alarm1.config(text=self.alarm_activate[0])
        
    def switch(self,alarm_ID):
        self.Alarm_name_label.config(text="".join(self.alarm_Name[alarm_ID]))
        self.alarm_set_hour.config(text=str(self.detail_hour[alarm_ID]).zfill(2)+" : "+str(self.detail_min[alarm_ID]).zfill(2))
        self.now_detail_alarmID = alarm_ID
        self.v.set(self.alarm_RingTime[self.now_detail_alarmID])
        self.ringtime_1.config(variable=self.v)
        self.ringtime_2.config(variable=self.v)
        self.ringtime_3.config(variable=self.v)
        self.ringtime_4.config(variable=self.v)
        
        
        self.week_code = self.alarm_Repeat[self.now_detail_alarmID]
        self.w0.set(self.week_code//64) 
        self.week_code%=64
        self.w1.set(self.week_code//32) 
        self.week_code%=32
        self.w2.set(self.week_code//16) 
        self.week_code%=16
        self.w3.set(self.week_code//8) 
        self.week_code%=8
        self.w4.set(self.week_code//4) 
        self.week_code%=4
        self.w5.set(self.week_code//2) 
        self.week_code%=2
        self.w6.set(self.week_code//1) 
        self.repeattime_1.config(variable=self.w0)
        self.repeattime_2.config(variable=self.w1)
        self.repeattime_3.config(variable=self.w2)
        self.repeattime_4.config(variable=self.w3)  
        self.repeattime_5.config(variable=self.w4)  
        self.repeattime_6.config(variable=self.w5)  
        self.repeattime_7.config(variable=self.w6)        
        
        self.on.set(self.alarm_activate[self.now_detail_alarmID])
        self.ON_OFF_1.config(variable=self.on)
        self.ON_OFF_2.config(variable=self.on)         
        
        self.N_alarm = alarm_ID
        
        #self.now_song.config(text="".join(self.alarm_song[alarm_ID]))
    
    def show_alarm(self):
        self.table_frame.pack(side = "top",expand = True, fill = tk.BOTH)
        self.time_label.place(y = 2, x = self.root_width - 60 )
        self.refresh()
        self.setting_zone = 0
        
    def hide_alarm(self):
        self.table_frame.pack_forget()
        self.time_label.place_forget()
        self.setting_frame.pack_forget()
        self.setting_zone = 0
        
    def adjust_alarm(self, pos, num):#hour or min, +1 or -1
        ID = self.now_detail_alarmID
        if(pos == 0):
            self.detail_hour[ID] = self.detail_hour[ID] + num
            if(self.detail_hour[ID]<0 or self.detail_hour[ID]>23):
                self.detail_hour[ID] = self.detail_hour[ID]%24
        if(pos == 1):              
            self.detail_min[ID] = self.detail_min[ID] + num
            if(self.detail_min[ID]<0 or self.detail_min[ID]>59):
                self.detail_min[ID] = self.detail_min[ID]%60
        self.alarm_set_hour.config(text=str(self.detail_hour[ID]).zfill(2)+" : "+str(self.detail_min[ID]).zfill(2))
        self.alarm_tool_label.config(text = "已修改  未保存")
        
    def set_ring_time(self, option):
        self.alarm_RingTime[self.now_detail_alarmID] = option
        self.alarm_tool_label.config(text = "已修改  未保存")
        
    def set_repeat_time(self, option):
        a = 1
        for i in range(6,option,-1):
            a*=2
        if option == 0:
            if not self.w0.get():
                a*=-1
        if option == 1:
            if not self.w1.get():
                a*=-1
        if option == 2:
            if not self.w2.get():
                a*=-1
        if option == 3:
            if not self.w3.get():
                a*=-1
        if option == 4:
            if not self.w4.get():
                a*=-1
        if option == 5:
            if not self.w5.get():
                a*=-1
        if option == 6:
            if not self.w6.get():
                a*=-1        
        self.alarm_Repeat[self.now_detail_alarmID] += a    
        self.alarm_tool_label.config(text = "已修改  未保存")
        
        
    def getCurrentMusicPath(self):
        path=self.musiclist.MusicPath(1)
        # self.listBox.select_set(0)
        for item in range(self.listBox.size()):
            musicAbsPath= path +"\\"+self.listBox.get(item)
            if self.listBox.selection_includes(item):
                path= musicAbsPath
                #print("-----", path)
                return path            
        
    def refreshMusiclist(self):
        path=self.musiclist.MusicPath(1)
        self.listBox.delete(0,tk.END )
                
        musicNameList= os.listdir(path)
        for musicName in musicNameList:
            path1= os.path.join(path, musicName)
            path1list= os.path.splitext(path1) 
            if path1list[-1]== ".mp3":
                self.listBox.insert(tk.END, musicName)
        for i in range(self.listBox.size()):
            if(i%2==0):
                self.listBox.itemconfig(i, bg='#AAAAAA')
            else:
                self.listBox.itemconfig(i, bg='#DDDDDD')
            #self.listBox.itemconfig(0, foreground="purple")
                
    def change_ring(self, event):        
        a = self.listBox.curselection()
        self.now_song.config(text = self.listBox.get(a))
        self.alarm_song[self.N_alarm] = self.listBox.get(a)
        self.alarm_tool_label.config(text = "已修改  未保存")
        
    def set_ONOFF(self, a):
        self.alarm_activate[self.N_alarm] = a
        self.alarm_tool_label.config(text = "已修改  未保存")
        
    def FMtime(self):
        self.time_label.config(text=time.strftime("%H:%M:%S", time.localtime()))
        
    def show_setting(self):
        self.table_frame.pack_forget()
        self.setting_frame.pack(side='top', fill=tk.BOTH)
        self.setting_zone = 1
        
    def hide_setting(self):
        self.setting_frame.pack_forget()
        self.table_frame.pack(side = "top",expand = True, fill = tk.BOTH)
        self.refresh()
        self.init_alarm()
        self.setting_zone = 0
        
    def refresh(self):
        self.A1_label.config(text = "".join(self.alarm_Name[0]))
        self.A2_label.config(text = "".join(self.alarm_Name[1]))
        self.A3_label.config(text = "".join(self.alarm_Name[2]))
        self.A4_label.config(text = "".join(self.alarm_Name[3]))
        self.A5_label.config(text = "".join(self.alarm_Name[4]))
        self.A6_label.config(text = "".join(self.alarm_Name[5]))
        
        temp = ""
        temp = self.rf_week(temp,0)
        self.A1_week_label.config(text = temp)
        temp = ""
        temp = self.rf_week(temp,1)
        self.A2_week_label.config(text = temp)
        temp = ""
        temp = self.rf_week(temp,2)
        self.A3_week_label.config(text = temp)
        temp = ""
        temp = self.rf_week(temp,3)
        self.A4_week_label.config(text = temp)
        temp = ""
        temp = self.rf_week(temp,4)
        self.A5_week_label.config(text = temp)
        temp = ""
        temp = self.rf_week(temp,5)
        self.A6_week_label.config(text = temp)
        
        self.A1_time_label.config(text=str(self.detail_hour[0]).zfill(2)+" : "+str(self.detail_min[0]).zfill(2))
        self.A2_time_label.config(text=str(self.detail_hour[1]).zfill(2)+" : "+str(self.detail_min[1]).zfill(2))
        self.A3_time_label.config(text=str(self.detail_hour[2]).zfill(2)+" : "+str(self.detail_min[2]).zfill(2))
        self.A4_time_label.config(text=str(self.detail_hour[3]).zfill(2)+" : "+str(self.detail_min[3]).zfill(2))
        self.A5_time_label.config(text=str(self.detail_hour[4]).zfill(2)+" : "+str(self.detail_min[4]).zfill(2))
        self.A6_time_label.config(text=str(self.detail_hour[5]).zfill(2)+" : "+str(self.detail_min[5]).zfill(2))
            
        self.A1_ON_OFF_1.config(text="ON" if self.alarm_activate[0] == 0 else "OFF")
        self.A2_ON_OFF_1.config(text="ON" if self.alarm_activate[1] == 0 else "OFF")
        self.A3_ON_OFF_1.config(text="ON" if self.alarm_activate[2] == 0 else "OFF")
        self.A4_ON_OFF_1.config(text="ON" if self.alarm_activate[3] == 0 else "OFF")
        self.A5_ON_OFF_1.config(text="ON" if self.alarm_activate[4] == 0 else "OFF")
        self.A6_ON_OFF_1.config(text="ON" if self.alarm_activate[5] == 0 else "OFF")
        
        self.A1_song.config(text="".join(self.alarm_song[0]))
        self.A2_song.config(text="".join(self.alarm_song[1]))
        self.A3_song.config(text="".join(self.alarm_song[2]))
        self.A4_song.config(text="".join(self.alarm_song[3]))
        self.A5_song.config(text="".join(self.alarm_song[4]))
        self.A6_song.config(text="".join(self.alarm_song[5]))
                
    def rf_week(self, temp, A):
        a = self.alarm_Repeat[A]
        if a == 127:
            return "每天"
        if a == 0:
            return "無"
        w0=(a//64) 
        a%=64
        w1=(a//32) 
        a%=32
        w2=(a//16) 
        a%=16
        w3=(a//8) 
        a%=8
        w4=(a//4) 
        a%=4
        w5=(a//2) 
        a%=2
        w6=(a//1) 
        if w0:
            temp+="日"
        if w1:
            temp+="一"
        if w2:
            temp+="二"
        if w3:
            temp+="三"
        if w4:
            temp+="四"
        if w5:
            temp+="五"
        if w6:
            temp+="六"
        return temp
        
    def Alarming(self):
        N_hour = time.strftime("%H", time.localtime())
        N_min = time.strftime("%M", time.localtime())
        N_sec = time.strftime("%S", time.localtime())
        N_week = time.strftime("%a", time.localtime())
        
        
        for i in range(6):
            if self.alarm_activate[i] == 1:
                continue
            if N_week == "Sun":
                if not self.w0.get():
                    continue
            if N_week == "Mon":
                if not self.w1.get():
                    continue
            if N_week == "Tue":
                if not self.w2.get():
                    continue
            if N_week == "Wed":
                if not self.w3.get():
                    continue
            if N_week == "Thu":
                if not self.w4.get():
                    continue
            if N_week == "Fri":
                if not self.w5.get():
                    continue
            if N_week == "Sat":
                if not self.w6.get():
                    continue
            if N_hour == str(self.detail_hour[i]).zfill(2) and N_min == str(self.detail_min[i]).zfill(2)and N_sec =="00" and self.N_ringing[i] == 0:
                self.musiclist.playMusic("".join(self.alarm_song[i]))
                self.detail_sec[i] = time.strftime("%S", time.localtime())
                self.N_ringing[i] = 1
                self.alarm_temp_sec[i]=(int(self.detail_sec[i])+int(self.alarm_ring_time[self.alarm_RingTime[i]]))%60
                self.alarm_temp_min[i]=int(self.detail_min[i])+(int(self.detail_sec[i])+int(self.alarm_ring_time[self.alarm_RingTime[i]]))//60
                self.alarm_temp_hr[i]=self.detail_hour[i]+(self.alarm_temp_min[i])//60                
                self.alarm_temp_hr[i]%=24
                self.alarm_temp_min[i]%=60
                self.ring_state = 1
                print("ring")
                return i
            elif self.N_ringing[i] == 1:
                if N_hour == str(self.alarm_temp_hr[i]).zfill(2) and N_min == str(self.alarm_temp_min[i]).zfill(2) and N_sec == str(self.alarm_temp_sec[i]).zfill(2):
                    self.N_ringing[i] = 0
                    self.musiclist.stopMusic()                    
                    self.ring_state = 2
                    return 2
        
        return 0
            
        
        
        
        
        
        
        
        
        
