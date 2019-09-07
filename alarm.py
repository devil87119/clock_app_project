# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:52:48 2019

@author: 楊秉翰
"""

import tkinter as tk
from tkinter import ttk 
import time

class Alarm:
    def __init__(self, root, root_height):
        #page size
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        
        #alarm attribute
        self.alarm_activate = [0, 0, 0, 0, 0, 0]#0 : 關閉,  1: 啟動
        self.detail_hour = dict()#設定鬧鐘時間
        self.detail_min = dict()#設定鬧鐘時間
        self.alarm_song = dict()#設定歌曲
        self.alarm_ring_time = [10, 30, 60, 120]#響鈴時間
        self.alarm_repeat = [0, 3, 5, 10000]#重複次數
        self.alarm_RingTime = dict()
        self.alarm_Repeat = dict()
        self.alarm_Name = dict()
        
        self.alarm_temp = dict()#站存鬧鈴時間
        self.now_detail_alarmID = 0
                
        #alarm 1~6 frame
        self.alarm_frame = ttk.Frame(self.root)
        self.alarm_frame.pack(side='bottom', fill=tk.Y)
        
        #alarm 1~6 frame
        self.alarm_top_frame = ttk.Frame(self.alarm_frame)        
        self.alarm_top_frame.pack(anchor=tk.S)
        
        #alarm 1~6 frame
        self.alarm_low_frame = ttk.Frame(self.alarm_frame)        
        self.alarm_low_frame.pack(anchor=tk.S, pady=10)
        
        #alarm 1~6 init
        big_button_Style = ttk.Style ()
        big_button_Style.configure("big.TButton", font = ('Arial','10'))
        self.Alarm1=ttk.Button(self.alarm_top_frame, text="Alarm 1", command=self.save, width=10, style = "big.TButton")
        self.Alarm2=ttk.Button(self.alarm_top_frame, text="Alarm 2", command=lambda: self.switch(1), width=10, style = "big.TButton")
        self.Alarm3=ttk.Button(self.alarm_top_frame, text="Alarm 3", command=lambda: self.switch(2), width=10, style = "big.TButton")
        self.Alarm4=ttk.Button(self.alarm_low_frame, text="Alarm 4", command=lambda: self.switch(3), width=10, style = "big.TButton")
        self.Alarm5=ttk.Button(self.alarm_low_frame, text="Alarm 5", command=lambda: self.switch(4), width=10, style = "big.TButton")
        self.Alarm6=ttk.Button(self.alarm_low_frame, text="Alarm 6", command=lambda: self.switch(5), width=10, style = "big.TButton")
        
        #place alarm 1~6 init        
        self.Alarm1.pack(side='left', padx=20)
        self.Alarm2.pack(side='left', padx=20)#(x=self.root_width/4*2,y = self.root_height/8*6)
        self.Alarm3.pack(side='left', padx=20)#(x=self.root_width/4*3,y = self.root_height/8*6)
        self.Alarm4.pack(side='left', padx=20)#(x=self.root_width/4,y = self.root_height/8*7)
        self.Alarm5.pack(side='left', padx=20)#(x=self.root_width/4*2,y = self.root_height/8*7)
        self.Alarm6.pack(side='left', padx=20)#(x=self.root_width/4*3,y = self.root_height/8*7)
        
        self.init_alarm()
        
        #detail of alarm
        ttk.Style().configure('Font.TLabelframe.Label', font = '25')#, foreground = "red"
        self.detail_frame = ttk.LabelFrame(self.root, text = "".join(self.alarm_Name[0]), borderwidth=2, relief="groove", style = "Font.TLabelframe")#, highlightcolor="green", highlightthickness=5
        self.detail_frame.pack(side='right')
        
        #time top button frame
        self.time_plus_frame = ttk.Frame(self.detail_frame)        
        self.time_plus_frame.pack(anchor=tk.NW)
        
        #plus time
        little_button_Style = ttk.Style ()
        little_button_Style.configure("little.TButton", font = ('Sans','10'))
        self.alarm_plus_hour = ttk.Button(self.time_plus_frame, text="+", command=lambda: self.adjust_alarm(0,1), width=6, style = "little.TButton")
        self.alarm_plus_hour.pack(side='left')
        self.alarm_plus_hour = ttk.Button(self.time_plus_frame, text="+", command=lambda: self.adjust_alarm(1,1), width=6, style = "little.TButton")
        self.alarm_plus_hour.pack(side='left', padx = 15)
        
        #set alarm time         
        self.alarm_set_hour = tk.Label(self.detail_frame, text=str(self.detail_hour[0]).zfill(2)+" : "+str(self.detail_min[0]).zfill(2), font=("Arial",25))
        self.alarm_set_hour.pack(anchor=tk.NW)        
        
        #time bottom button frame
        self.time_minus_frame = ttk.Frame(self.detail_frame)        
        self.time_minus_frame.pack(anchor=tk.NW)
        
        #minus time
        self.alarm_minus_hour = ttk.Button(self.time_minus_frame, text="-", command=lambda: self.adjust_alarm(0,-1), width=6, style = "little.TButton")
        self.alarm_minus_hour.pack(side='left')
        self.alarm_minus_hour = ttk.Button(self.time_minus_frame, text="-", command=lambda: self.adjust_alarm(1,-1), width=6, style = "little.TButton")
        self.alarm_minus_hour.pack(side='left', padx = 15)
        
        #鬧鐘持續時間
        self.ringing_time_label = ttk.Label(self.detail_frame, text = "鬧鐘持續時間", font=("Arial",12))        
        self.ringing_time_label.pack(anchor=tk.NW)
        
        #ringing time frame
        self.ring_time_frame = ttk.Frame(self.detail_frame)        
        self.ring_time_frame.pack(anchor=tk.NW, padx = 10)                
        
        #ringing time option
        self.v = tk.IntVar()
        self.v.set(self.alarm_RingTime[0]) 
        self.ringtime_1 = ttk.Radiobutton(self.ring_time_frame, text=str(self.alarm_ring_time[0])+"秒", variable=self.v, value=0, command=lambda: self.set_ring_time(0))
        self.ringtime_2 = ttk.Radiobutton(self.ring_time_frame, text=str(self.alarm_ring_time[1])+"秒", variable=self.v, value=1, command=lambda: self.set_ring_time(1))
        self.ringtime_3 = ttk.Radiobutton(self.ring_time_frame, text=str(self.alarm_ring_time[2])+"秒", variable=self.v, value=2, command=lambda: self.set_ring_time(2))
        self.ringtime_4 = ttk.Radiobutton(self.ring_time_frame, text=str(self.alarm_ring_time[3])+"秒", variable=self.v, value=3, command=lambda: self.set_ring_time(3))
        self.ringtime_1.pack(side='left')
        self.ringtime_2.pack(side='left')
        self.ringtime_3.pack(side='left')
        self.ringtime_4.pack(side='left')
        
        #鬧鐘重複次數
        self.alarm_repeat_label = ttk.Label(self.detail_frame, text = "鬧鐘重複次數", font=("Arial",12))        
        self.alarm_repeat_label.pack(anchor=tk.NW)  
        
        #repeat time frame
        self.repeat_frame = ttk.Frame(self.detail_frame)        
        self.repeat_frame.pack(anchor=tk.NW, padx = 10)              
        
        #repeat time option
        self.v1 = tk.IntVar()
        self.v1.set(self.alarm_Repeat[0]) 
        self.repeattime_1 = ttk.Radiobutton(self.repeat_frame, text=" 無  ", variable=self.v1, value=0, command=lambda: self.set_repeat_time(0))
        self.repeattime_2 = ttk.Radiobutton(self.repeat_frame, text=str(self.alarm_repeat[1])+"次  ", variable=self.v1, value=1, command=lambda: self.set_repeat_time(1))
        self.repeattime_3 = ttk.Radiobutton(self.repeat_frame, text=str(self.alarm_repeat[2])+"次  ", variable=self.v1, value=2, command=lambda: self.set_repeat_time(2))
        self.repeattime_4 = ttk.Radiobutton(self.repeat_frame, text=" ∞", variable=self.v1, value=3, command=lambda: self.set_repeat_time(3))
        self.repeattime_1.pack(side='left')
        self.repeattime_2.pack(side='left')
        self.repeattime_3.pack(side='left')
        self.repeattime_4.pack(side='left')
        
        self.hide_alarm()
        
    def hide_alarm(self):
        self.alarm_frame.pack_forget()
        self.detail_frame.pack_forget()
        
    def init_alarm(self):
        point = 0
        fp = open('alarm/alarm_init.txt', "r")
        line = fp.readline()
        while line:
            if(point < 6):
                self.alarm_activate[point] = list(line.replace('\n', ''))
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
        self.Alarm1.config(text="".join(self.alarm_Name[0]))
        self.Alarm2.config(text="".join(self.alarm_Name[1]))
        self.Alarm3.config(text="".join(self.alarm_Name[2]))
        self.Alarm4.config(text="".join(self.alarm_Name[3]))
        self.Alarm5.config(text="".join(self.alarm_Name[4]))
        self.Alarm6.config(text="".join(self.alarm_Name[5]))
        
    def save(self):
        point = 0
        fp = open('alarm/alarm2_init.txt', "w+")
        for i in range(0,36):
            if(point < 6):
                fp.writelines(self.alarm_activate[point])
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
        
    
    def show_alarm(self):
        self.detail_frame.pack(anchor=tk.NW,pady=20,padx=80)
        self.alarm_frame.pack(anchor=tk.S)
        
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
        
    def set_ring_time(self, option):
        self.alarm_RingTime[self.now_detail_alarmID] = option
        
    def set_repeat_time(self, option):
        self.alarm_Repeat[self.now_detail_alarmID] = option

        
        
        
        
        
        
        
        
        
        
