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
        self.alarm_song = dict()#設定歌曲
        self.alarm_ring_time = [10, 30, 60, 120]#響鈴時間
        self.alarm_repeat = [0, 3, 5, 10000]#重複次數
        self.alarm_RingTime = dict()
        self.alarm_Repeat = dict()
        self.alarm_Name = dict()
        self.first = 0
        
        self.alarm_temp = dict()#站存鬧鈴時間
        self.now_detail_alarmID = 0
                
        self.setting_frame= ttk.Frame(self.main_frame)
        self.setting_frame.pack(side='top', fill=tk.BOTH)
        
        self.N_alarm = 0
        #alarm 1~6 frame
        self.alarm_frame = ttk.Frame(self.setting_frame)
        
        #alarm 1~6 frame
        self.alarm_top_frame = ttk.Frame(self.alarm_frame)        
        self.alarm_top_frame.pack(anchor=tk.S)
        
        #alarm 1~6 frame
        self.alarm_low_frame = ttk.Frame(self.alarm_frame)        
        self.alarm_low_frame.pack(anchor=tk.S, pady=(0,0))
        
        #alarm 1~6 init
        big_button_Style = ttk.Style ()
        big_button_Style.configure("big.TButton", font = ('Arial','10'))
        self.Alarm1=ttk.Button(self.alarm_top_frame, text="Alarm 1", command=lambda: self.switch(0), width=10, style = "big.TButton")
        self.Alarm2=ttk.Button(self.alarm_top_frame, text="Alarm 2", command=lambda: self.switch(1), width=10, style = "big.TButton")
        self.Alarm3=ttk.Button(self.alarm_top_frame, text="Alarm 3", command=lambda: self.switch(2), width=10, style = "big.TButton")
        self.Alarm4=ttk.Button(self.alarm_low_frame, text="Alarm 4", command=lambda: self.switch(3), width=10, style = "big.TButton")
        self.Alarm5=ttk.Button(self.alarm_low_frame, text="Alarm 5", command=lambda: self.switch(4), width=10, style = "big.TButton")
        self.Alarm6=ttk.Button(self.alarm_low_frame, text="Alarm 6", command=lambda: self.switch(5), width=10, style = "big.TButton")
        
        #place alarm 1~6 init        
        self.Alarm1.pack(side='left', padx=20,pady=(0,10))
        self.Alarm2.pack(side='left', padx=20,pady=(0,10))#(x=self.root_width/4*2,y = self.root_height/8*6)
        self.Alarm3.pack(side='left', padx=20,pady=(0,10))#(x=self.root_width/4*3,y = self.root_height/8*6)
        self.Alarm4.pack(side='left', padx=20)#(x=self.root_width/4,y = self.root_height/8*7)
        self.Alarm5.pack(side='left', padx=20)#(x=self.root_width/4*2,y = self.root_height/8*7)
        self.Alarm6.pack(side='left', padx=20)#(x=self.root_width/4*3,y = self.root_height/8*7)
        
        self.init_alarm()
        
        #time
        self.time_label=tk.Label(self.root, text=time.strftime("%H:%M:%S", time.localtime()), font=("Arial",10))
        self.time_label.place(y = 2, x = self.root_width - 60 )
        
        #detail of alarm
        ttk.Style().configure('Font.TLabelframe.Label', font = '25')#, foreground = "red"
        self.detail_frame = ttk.LabelFrame(self.setting_frame, text = "".join(self.alarm_Name[0]), borderwidth=2, relief="groove", style = "Font.TLabelframe")#, highlightcolor="green", highlightthickness=5
        self.detail_frame.pack(anchor=tk.NW,pady=(10, 0),padx=(10,10))
        self.alarm_frame.pack(anchor=tk.CENTER,pady=(5, 0))
        
        #left detial frame
        self.left_frame = ttk.Frame(self.detail_frame, borderwidth=2, relief="groove")        
        self.left_frame.pack(side = 'left')
        
        #Right detial frame
        self.right_frame = ttk.Frame(self.detail_frame, borderwidth=2, relief="groove")        
        self.right_frame.pack(side = 'top', padx = (10,0))
        
        
        #on off frame 
        self.ON_OFF_label = ttk.Label(self.left_frame, text = "ON/OFF ", font=("Arial",10))        
        #self.ON_OFF_label.pack(anchor=tk.NW, pady = (0,0))
        self.activate_frame = ttk.Frame(self.left_frame)        
        self.activate_frame.pack(anchor=tk.NW, padx = 10,pady=(5,0))  
        
        #ON/OFF   
        self.on = tk.IntVar()
        self.on.set(self.alarm_activate[0]) 
        self.ON_OFF_1 = ttk.Radiobutton(self.activate_frame, text="ON", variable=self.on, value=0, command=lambda: self.set_ONOFF(0))
        self.ON_OFF_2 = ttk.Radiobutton(self.activate_frame, text="OFF", variable=self.on, value=1, command=lambda: self.set_ONOFF(1))
        self.ON_OFF_1.pack(side ="left")
        self.ON_OFF_2.pack(side ="left")
        
        #time_frame
        self.time_frame = ttk.Frame(self.left_frame)        
        self.time_frame.pack(anchor=tk.NW, pady = (0,0))
        
        
        #time top button frame
        self.time_plus_frame = ttk.Frame(self.time_frame)        
        self.time_plus_frame.pack(side='left')
        
        #plus time
        little_button_Style = ttk.Style ()
        little_button_Style.configure("little.TButton", font = ('Sans','10'))
        self.alarm_plus_hour = ttk.Button(self.time_plus_frame, text="+", command=lambda: self.adjust_alarm(0,1), width=2, style = "little.TButton")
        self.alarm_plus_hour.pack(anchor=tk.NW)
        self.alarm_minus_hour = ttk.Button(self.time_plus_frame, text="-", command=lambda: self.adjust_alarm(0,-1), width=2, style = "little.TButton")
        self.alarm_minus_hour.pack(anchor=tk.NW)                
        
        #set alarm time         
        self.alarm_set_hour = tk.Label(self.time_frame, text=str(self.detail_hour[0]).zfill(2)+" : "+str(self.detail_min[0]).zfill(2), font=("Arial",36))
        self.alarm_set_hour.pack(side='left')        
        
        #time bottom button frame
        self.time_minus_frame = ttk.Frame(self.time_frame)        
        self.time_minus_frame.pack(side='left')
        
        #minus time
        self.alarm_plus_hour = ttk.Button(self.time_minus_frame, text="+", command=lambda: self.adjust_alarm(1,1), width=2, style = "little.TButton")
        self.alarm_plus_hour.pack(anchor=tk.NW, padx = 0)        
        self.alarm_minus_hour = ttk.Button(self.time_minus_frame, text="-", command=lambda: self.adjust_alarm(1,-1), width=2, style = "little.TButton")
        self.alarm_minus_hour.pack(anchor=tk.NW, padx = 0)
        
        #鬧鐘持續時間
        self.ringing_time_label = ttk.Label(self.left_frame, text = "鬧鐘持續時間", font=("Arial",10))        
        self.ringing_time_label.pack(anchor=tk.NW, pady = (1,0))
        
        #ringing time frame
        self.ring_time_frame = ttk.Frame(self.left_frame)        
        self.ring_time_frame.pack(anchor=tk.NW, padx = 10)                
        
        #ringing time option
        self.v = tk.IntVar()
        self.v.set(self.alarm_RingTime[0]) 
        self.ringtime_1 = ttk.Radiobutton(self.ring_time_frame, text=str(self.alarm_ring_time[0])+"s", variable=self.v, value=0, command=lambda: self.set_ring_time(0))
        self.ringtime_2 = ttk.Radiobutton(self.ring_time_frame, text=str(self.alarm_ring_time[1])+"s", variable=self.v, value=1, command=lambda: self.set_ring_time(1))
        self.ringtime_3 = ttk.Radiobutton(self.ring_time_frame, text="1m", variable=self.v, value=2, command=lambda: self.set_ring_time(2))
        self.ringtime_4 = ttk.Radiobutton(self.ring_time_frame, text="2m", variable=self.v, value=3, command=lambda: self.set_ring_time(3))
        self.ringtime_1.pack(side='left')
        self.ringtime_2.pack(side='left')
        self.ringtime_3.pack(side='left')
        self.ringtime_4.pack(side='left')
        
        #鬧鐘重複次數
        self.alarm_repeat_label = ttk.Label(self.left_frame, text = "鬧鐘重複次數", font=("Arial",10))        
        self.alarm_repeat_label.pack(anchor=tk.NW, pady = (2,0))  
        
        #repeat time frame
        self.repeat_frame = ttk.Frame(self.left_frame)        
        self.repeat_frame.pack(anchor=tk.NW, padx = 10)              
        
        #repeat time option
        self.v1 = tk.IntVar()
        self.v1.set(self.alarm_Repeat[0]) 
        self.repeattime_1 = ttk.Radiobutton(self.repeat_frame, text=" 無 ", variable=self.v1, value=0, command=lambda: self.set_repeat_time(0))
        self.repeattime_2 = ttk.Radiobutton(self.repeat_frame, text=str(self.alarm_repeat[1])+"次", variable=self.v1, value=1, command=lambda: self.set_repeat_time(1))
        self.repeattime_3 = ttk.Radiobutton(self.repeat_frame, text=str(self.alarm_repeat[2])+"次", variable=self.v1, value=2, command=lambda: self.set_repeat_time(2))
        self.repeattime_4 = ttk.Radiobutton(self.repeat_frame, text=" ∞", variable=self.v1, value=3, command=lambda: self.set_repeat_time(3))
        self.repeattime_1.pack(side='left')
        self.repeattime_2.pack(side='left')
        self.repeattime_3.pack(side='left')
        self.repeattime_4.pack(side='left')
        
        #鬧鐘歌曲
        self.alarm_song_label = ttk.Label(self.left_frame, text = "鬧鐘鈴聲", font=("Arial",10))        
        self.alarm_song_label.pack(anchor=tk.NW, pady = (2,0))  
        self.now_song = ttk.Label(self.left_frame, text="".join(self.alarm_song[0]), width = 25, background = 'white')
        self.now_song.pack(anchor=tk.NW, padx = (10,0),pady = (0,2))
        
        #鬧鐘清單
        self.alarm_song_label = ttk.Label(self.right_frame, text = "鬧鐘歌曲清單", font=("Arial",10))       
        self.alarm_song_label.pack(anchor=tk.NW, pady = (5,0))  
        self.song_frame = tk.Frame(self.right_frame, height = 100)
        self.scroll_frame = tk.Frame(self.song_frame, height = 100)
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
        self.function_frame = ttk.Frame(self.right_frame)        
        self.function_frame.pack(anchor=tk.NE, padx = 0, fill=tk.X)   
        self.cancel=ttk.Button(self.function_frame, text="取消離開", command=self.hide_setting, width=8, style = "big.TButton")
        self.save=ttk.Button(self.function_frame, text="保存", command=self.save, width=4, style = "big.TButton")
        self.save.pack(side = "right")
        self.cancel.pack(side = "right")
        self.alarm_tool_label = ttk.Label(self.function_frame, text = "未修改", font=("Arial",10))       
        self.alarm_tool_label.pack(side="left", padx = (10,0))
        
        #table frame        
        self.table_frame = tk.Frame(self.main_frame, relief="groove", borderwidth=2) 
        self.table_frame.pack(side = "top")
        
        
        #head_frame
        self.head_frame = tk.Frame(self.table_frame) 
        self.head_frame.pack(side = "top", pady = (20,10))
        
        #every_alarm_frame 1
        self.A1 = tk.Frame(self.head_frame, relief="groove" , borderwidth=2 ) 
        self.A1.pack(side = "left", padx = (0,10))
        self.A1_sm_frame = tk.Frame(self.A1) 
        self.A1_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A1_label = ttk.Label(self.A1_sm_frame, text = "".join(self.alarm_Name[0]), font=("Arial",10))
        self.A1_label.pack(side = "left")        
        self.A1_ON_OFF_1 = ttk.Label(self.A1_sm_frame, text="ON" if self.alarm_activate[0] == 0 else "OFF", font=("Arial",12))
        self.A1_ON_OFF_1.pack(side ="right")
        self.A1_time_label= ttk.Label(self.A1, text=str(self.detail_hour[0]).zfill(2)+" : "+str(self.detail_min[0]).zfill(2), font=("Arial",16))
        self.A1_time_label.pack(anchor = tk.NW)    
        self.A1_song = ttk.Label(self.A1, text="".join(self.alarm_song[0]), width = 25, background = 'white')
        self.A1_song.pack(anchor=tk.NW)
        
        #every_alarm_frame 2
        self.A2 = tk.Frame(self.head_frame, relief="groove" , borderwidth=2 ) 
        self.A2.pack(side = "left")
        self.A2_sm_frame = tk.Frame(self.A2) 
        self.A2_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A2_label = ttk.Label(self.A2_sm_frame, text = "".join(self.alarm_Name[1]), font=("Arial",10))
        self.A2_label.pack(side = "left")        
        self.A2_ON_OFF_1 = ttk.Label(self.A2_sm_frame, text="ON" if self.alarm_activate[1] == 0 else "OFF", font=("Arial",12))
        self.A2_ON_OFF_1.pack(side ="right")
        self.A2_time_label= ttk.Label(self.A2, text=str(self.detail_hour[1]).zfill(2)+" : "+str(self.detail_min[1]).zfill(2), font=("Arial",16))
        self.A2_time_label.pack(anchor = tk.NW) 
        self.A2_song = ttk.Label(self.A2, text="".join(self.alarm_song[1]), width = 25, background = 'white')
        self.A2_song.pack(anchor=tk.NW)
        
        #mid_frame
        self.mid_frame = tk.Frame(self.table_frame) 
        self.mid_frame.pack(side = "top", pady = (0,10))
        
        #every_alarm_frame 3
        self.A3 = tk.Frame(self.mid_frame, relief="groove" , borderwidth=2 ) 
        self.A3.pack(side = "left", padx = (0,10))
        self.A3_sm_frame = tk.Frame(self.A3) 
        self.A3_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A3_label = ttk.Label(self.A3_sm_frame, text = "".join(self.alarm_Name[2]), font=("Arial",10))
        self.A3_label.pack(side = "left")        
        self.A3_ON_OFF_1 = ttk.Label(self.A3_sm_frame, text="ON" if self.alarm_activate[2] == 0 else "OFF", font=("Arial",12))
        self.A3_ON_OFF_1.pack(side ="right")
        self.A3_time_label= ttk.Label(self.A3, text=str(self.detail_hour[2]).zfill(2)+" : "+str(self.detail_min[2]).zfill(2), font=("Arial",16))
        self.A3_time_label.pack(anchor = tk.NW)    
        self.A3_song = ttk.Label(self.A3, text="".join(self.alarm_song[2]), width = 25, background = 'white')
        self.A3_song.pack(anchor=tk.NW)
        
        #every_alarm_frame 4
        self.A4 = tk.Frame(self.mid_frame, relief="groove" , borderwidth=2 ) 
        self.A4.pack(side = "left")
        self.A4_sm_frame = tk.Frame(self.A4) 
        self.A4_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A4_label = ttk.Label(self.A4_sm_frame, text = "".join(self.alarm_Name[3]), font=("Arial",10))
        self.A4_label.pack(side = "left")        
        self.A4_ON_OFF_1 = ttk.Label(self.A4_sm_frame, text="ON" if self.alarm_activate[3] == 0 else "OFF", font=("Arial",12))
        self.A4_ON_OFF_1.pack(side ="right")
        self.A4_time_label= ttk.Label(self.A4, text=str(self.detail_hour[3]).zfill(2)+" : "+str(self.detail_min[3]).zfill(2), font=("Arial",16))
        self.A4_time_label.pack(anchor = tk.NW) 
        self.A4_song = ttk.Label(self.A4, text="".join(self.alarm_song[3]), width = 25, background = 'white')
        self.A4_song.pack(anchor=tk.NW)
        
        
        #mid_frame
        self.ft_frame = tk.Frame(self.table_frame) 
        self.ft_frame.pack(side = "top")
        
        #every_alarm_frame 5
        self.A5 = tk.Frame(self.ft_frame, relief="groove" , borderwidth=2 ) 
        self.A5.pack(side = "left", padx = (0,10))
        self.A5_sm_frame = tk.Frame(self.A5) 
        self.A5_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A5_label = ttk.Label(self.A5_sm_frame, text = "".join(self.alarm_Name[4]), font=("Arial",10))
        self.A5_label.pack(side = "left")        
        self.A5_ON_OFF_1 = ttk.Label(self.A5_sm_frame, text="ON" if self.alarm_activate[4] == 0 else "OFF", font=("Arial",12))
        self.A5_ON_OFF_1.pack(side ="right")
        self.A5_time_label= ttk.Label(self.A5, text=str(self.detail_hour[4]).zfill(2)+" : "+str(self.detail_min[4]).zfill(2), font=("Arial",16))
        self.A5_time_label.pack(anchor = tk.NW)    
        self.A5_song = ttk.Label(self.A5, text="".join(self.alarm_song[4]), width = 25, background = 'white')
        self.A5_song.pack(anchor=tk.NW)
        
        #every_alarm_frame 6 
        self.A6 = tk.Frame(self.ft_frame, relief="groove" , borderwidth=2 ) 
        self.A6.pack(side = "left")
        self.A6_sm_frame = tk.Frame(self.A6) 
        self.A6_sm_frame.pack(anchor = tk.NW, fill = tk.X)
        self.A6_label = ttk.Label(self.A6_sm_frame, text = "".join(self.alarm_Name[5]), font=("Arial",10))
        self.A6_label.pack(side = "left")        
        self.A6_ON_OFF_1 = ttk.Label(self.A6_sm_frame, text="ON" if self.alarm_activate[5] == 0 else "OFF", font=("Arial",12))
        self.A6_ON_OFF_1.pack(side ="right")
        self.A6_time_label= ttk.Label(self.A6, text=str(self.detail_hour[5]).zfill(2)+" : "+str(self.detail_min[5]).zfill(2), font=("Arial",16))
        self.A6_time_label.pack(anchor = tk.NW) 
        self.A6_song = ttk.Label(self.A6, text="".join(self.alarm_song[5]), width = 25, background = 'white')
        self.A6_song.pack(anchor=tk.NW)
        
        self.set=ttk.Button(self.table_frame, text="設定", command=self.show_setting, width=10, style = "big.TButton")
        self.set.pack(anchor = tk.SE)
        
        self.refreshMusiclist()
        
        self.setting_frame.pack_forget()
        self.hide_alarm()
        
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
        #self.Alarm1.config(text=self.alarm_activate[0])
        
    def switch(self,alarm_ID):
        self.detail_frame.config(text="".join(self.alarm_Name[alarm_ID]), style = "Font.TLabelframe")
        self.alarm_set_hour.config(text=str(self.detail_hour[alarm_ID]).zfill(2)+" : "+str(self.detail_min[alarm_ID]).zfill(2))
        self.now_detail_alarmID = alarm_ID
        self.v.set(self.alarm_RingTime[self.now_detail_alarmID])
        self.ringtime_1.config(variable=self.v)
        self.ringtime_2.config(variable=self.v)
        self.ringtime_3.config(variable=self.v)
        self.ringtime_4.config(variable=self.v)
        
        self.v1.set(self.alarm_Repeat[self.now_detail_alarmID])
        self.repeattime_1.config(variable=self.v1)
        self.repeattime_2.config(variable=self.v1)
        self.repeattime_3.config(variable=self.v1)
        self.repeattime_4.config(variable=self.v1)        
        
        self.on.set(self.alarm_activate[self.now_detail_alarmID])
        self.ON_OFF_1.config(variable=self.on)
        self.ON_OFF_2.config(variable=self.on)         
        
        self.N_alarm = alarm_ID
        
        #self.now_song.config(text="".join(self.alarm_song[alarm_ID]))
    
    def show_alarm(self):
        self.table_frame.pack(side = "top")
        self.time_label.place(y = 2, x = self.root_width - 60 )
        self.A1_ON_OFF_1.config(text="ON" if self.alarm_activate[0] == 0 else "OFF")
        self.A2_ON_OFF_1.config(text="ON" if self.alarm_activate[1] == 0 else "OFF")
        self.A3_ON_OFF_1.config(text="ON" if self.alarm_activate[2] == 0 else "OFF")
        self.A4_ON_OFF_1.config(text="ON" if self.alarm_activate[3] == 0 else "OFF")
        self.A5_ON_OFF_1.config(text="ON" if self.alarm_activate[4] == 0 else "OFF")
        self.A6_ON_OFF_1.config(text="ON" if self.alarm_activate[5] == 0 else "OFF")
        
    def hide_alarm(self):
        self.table_frame.pack_forget()
        self.time_label.place_forget()
        self.setting_frame.pack_forget()
        
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
        self.alarm_Repeat[self.now_detail_alarmID] = option
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
                self.listBox.itemconfig(i, bg='yellow')
            else:
                self.listBox.itemconfig(i, bg='light goldenrod')
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
        
    def hide_setting(self):
        self.setting_frame.pack_forget()
        self.table_frame.pack(side = "top")
        self.A1_ON_OFF_1.config(text="ON" if self.alarm_activate[0] == 0 else "OFF")
        self.A2_ON_OFF_1.config(text="ON" if self.alarm_activate[1] == 0 else "OFF")
        self.A3_ON_OFF_1.config(text="ON" if self.alarm_activate[2] == 0 else "OFF")
        self.A4_ON_OFF_1.config(text="ON" if self.alarm_activate[3] == 0 else "OFF")
        self.A5_ON_OFF_1.config(text="ON" if self.alarm_activate[4] == 0 else "OFF")
        self.A6_ON_OFF_1.config(text="ON" if self.alarm_activate[5] == 0 else "OFF")
        self.init_alarm()
        

        
        
        
        
        
        
        
        
        
        
