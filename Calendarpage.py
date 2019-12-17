# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:49:40 2019

@author: chimo
"""

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk 
import os
import time
import pygame
import pyaudio
import wave
from PIL import ImageTk,Image

set = False
#input_filepath = "event/"    
inpt_filepath = "/home/pi/Desktop/clock/clock_app_project-master/event/"  

date = {0:0}

class CalendarPage():
    def __init__(self, root,main_frame, root_height):
        #page size
        self.root = root
        self.root.grid_columnconfigure(9, minsize=20)
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        self.main_frame = main_frame;
        self.detail_hour=0#設定鬧鐘時間
        self.detail_min =0#設定鬧鐘時間
        self.detail = dict()
        self.selyear = 0
        self.file_path = ""
        self.selmonth =0
        self.selday = 0
        self.point = 0


        
        #Label of time
        self.time_label=tk.Label(self.main_frame, text=time.strftime("%H:%M:%S", time.localtime()), font=("Arial",10),background='black', foreground="white")
        #self.time_label.pack(anchor=tk.NE)
        
        self.a = tk.Frame(self.main_frame,bg="black")#, relief = "groove", borderwidth = 2)
        self.a.pack(side = "top", expand= True,fill = tk.X,padx = (50,0))
        self.calendar = tk.Frame(self.main_frame,bg="black")#, relief = "groove", borderwidth = 2)
        self.calendar.pack(side = "top", expand= True,fill = tk.BOTH)
        #creat page
        self.settingPage = tk.Frame(self.main_frame,bg="black")
        self.settingPage.pack(side = "top", expand= True,fill = tk.BOTH)
        self.left_frame = tk.Frame(self.settingPage,bg="black")
        self.left_frame.pack(side = "left", expand= True,fill = tk.BOTH)  
        #left label
        #date label
        self.date_lable = tk.Label(self.left_frame, font=("Arial",30),background='black', foreground="white")
        self.date_lable.pack(side = "top")
        self.year_label = tk.Label(self.date_lable, font=("Arial",30),background='black', foreground="white")
        self.year_label.pack(side = "left", expand= True,fill = tk.BOTH)
        self.month_label = tk.Label(self.date_lable, font=("Arial",30),background='black', foreground="white")
        self.month_label.pack(side = "left", expand= True,fill = tk.BOTH)
        self.day_label = tk.Label(self.date_lable, font=("Arial",30),background='black', foreground="white")
        self.day_label.pack(side = "right", expand= True,fill = tk.BOTH)
        #time_frame
        self.time_frame = tk.Frame(self.left_frame,bg="black")        
        self.time_frame.pack(side ="top")
        
        
        #time top button frame
        self.time_plus_frame = tk.Frame(self.time_frame,bg="black")        
        self.time_plus_frame.pack(side='left')
        
        #plus time
        little_button_Style = ttk.Style ()
        little_button_Style.configure("little.TButton", font = ('Sans','10'))
        self.alarm_plus_hour = tk.Button(self.time_plus_frame, text="+", command=lambda: self.adjust_alarm(0,1), width=2, font = ('Sans','10'),bg='black', foreground="white")
        self.alarm_plus_hour.pack(anchor=tk.NW)
        self.alarm_minus_hour = tk.Button(self.time_plus_frame, text="-", command=lambda: self.adjust_alarm(0,-1), width=2, font = ('Sans','10'),bg='black', foreground="white")
        self.alarm_minus_hour.pack(anchor=tk.NW)                
        
        #set alarm time         
        self.alarm_set_hour = tk.Label(self.time_frame, text=str(self.detail_hour).zfill(2)+" : "+str(self.detail_min).zfill(2), font=("Arial",36),background='black', foreground="white")
        self.alarm_set_hour.pack(side='left')        
        
        #time bottom button frame
        self.time_minus_frame = tk.Frame(self.time_frame,bg="black")        
        self.time_minus_frame.pack(side='left')
        
        #minus time
        self.alarm_plus_hour = tk.Button(self.time_minus_frame, text="+", command=lambda: self.adjust_alarm(1,1), width=2, font = ('Sans','10'),bg='black', foreground="white")
        self.alarm_plus_hour.pack(anchor=tk.NW, padx = 0)        
        self.alarm_minus_hour = tk.Button(self.time_minus_frame, text="-", command=lambda: self.adjust_alarm(1,-1), width=2, font = ('Sans','10'),bg='black', foreground="white")
        self.alarm_minus_hour.pack(anchor=tk.NW, padx = 0)
        
        #text lable
        self.event_frame = tk.Frame(self.left_frame,bg="black")
        self.event_frame.pack(side ="top",fill=tk.X)
        self.event_label = tk.Label(self.event_frame,text="事件錄音",background='black', foreground="white")
        self.event_label.pack(side = "left")
        self.event = tk.Button(self.event_frame, text="開始錄音", command=lambda: self.show_get_audio(), width=2,bg='black', foreground="white")
        self.event.pack(side = "left", expand= True,fill = tk.BOTH)
        
        #button frame
        self.play_image=ImageTk.PhotoImage(Image.open('picture/play.jpg'))
        self.save_image=ImageTk.PhotoImage(Image.open('picture/save.jpg'))
        self.exit_image=ImageTk.PhotoImage(Image.open('picture/exit.jpg'))
        self.button_frame = tk.Frame(self.left_frame,bg="black")
        self.button_frame.pack(side ="top")
        self.play = tk.Button(self.button_frame,image=self.play_image,text = "播放行程",bg='black', foreground="white",command=lambda: self.play_audio()).pack(side = 'left')
        self.confirm = tk.Button(self.button_frame,image=self.save_image,text = "儲存",bg='black', foreground="white",command=lambda: self.save()).pack(side = 'left')
        self.close = tk.Button(self.button_frame,image=self.exit_image,text = "離開",bg='black', foreground="white",command=lambda: self.close_setting()).pack(side = 'left')

        #event list
        self.lv= tk.StringVar()
        self.event_list_frame =  tk.Frame(self.left_frame,bg="black")
        self.event_list_frame.pack(side ="left")
        self.event_list = tk.Listbox(self.event_list_frame,selectmode=tk.BROWSE,width=20,height=5,bg="light grey",listvariable=self.lv)
        self.event_list.pack(side="left", fill=tk.X)
        #event button
        self.event_play_image=ImageTk.PhotoImage(Image.open('picture/play.jpg'))
        self.event_button_frame = tk.Frame(self.left_frame,bg="black")
        self.event_button_frame.pack(side ="left")
        self.event_play_button = tk.Button(self.event_button_frame,image=self.event_play_image,text = "播放",bg='black', foreground="white",command=lambda: self.play_event()).pack(side = 'top')
        
        
        #play AUDIO
        self.play_success_frame =  tk.Frame(self.main_frame,bg="black")
        self.play_success_frame.place(relx = 0.3,rely = 0.3,height = 100,width = 100)
        self.play_success = tk.Label(self.play_success_frame,text="播放完畢",background='black', foreground="white")
        self.play_success.place(x=25,y = 30)
        self.play_success_confirm =  tk.Button(self.play_success_frame,text = "結束",bg='black', foreground="white",command=lambda: self.hide_play_success()).pack(side = 'bottom')
        
        #get AUDIO
        self.getting_audio_image=ImageTk.PhotoImage(Image.open('picture/record.jpg'))
        self.getting_frame =  tk.Frame(self.main_frame,bg="black")
        self.getting_frame.place(relx = 0.3,rely = 0.3,height = 100,width = 100)
        self.getting_audio = tk.Label(self.getting_frame,text="開始錄音",background='black', foreground="white")
        self.getting_audio.place(x=25,y = 30)
        self.getting_audio_confirm =  tk.Button(self.getting_frame,image=self.getting_audio_image,text = "確認",bg='black', foreground="white",command=lambda: self.get_audio()).pack(side = 'bottom')
        
        #test audio
        self.test_frame = tk.Frame(self.main_frame,bg="black")
        self.test_frame.place(relx = 0.3,rely = 0.3,height = 150,width = 150)
        self.test_text = tk.Label(self.test_frame,text="試聽音檔",background='black', foreground="white")
        self.test_text.place(x=45,y = 60)
        self.test_button_frame = tk.Frame(self.test_frame,bg="black")
        self.test_button_frame.pack(side = "bottom")
        self.test_play_button = tk.Button(self.test_button_frame,text = "試聽",bg='black', foreground="white",command=lambda: self.test_play()).pack(side = 'left')
        self.again =  tk.Button(self.test_button_frame,text = "重錄",bg='black', foreground="white",command=lambda: self.get_audio()).pack(side = 'left')
        self.close =  tk.Button(self.test_button_frame,text = "離開",bg='black', foreground="white",command=lambda: self.hide_test_frame()).pack(side = 'left')
        
        self.drawHeader()
        self.createMonth()
        self.updateDate()
        self.close_setting()
        self.hide_test_frame()
        self.hide_play_success()
        self.hide_get_audio()
        self.hide_calendarpage()
        
        
        
    def time(self):
        self.time_label.config(text=time.strftime("%H:%M:%S", time.localtime()))

        
    def hide_calendarpage(self):
        self.time_label.place_forget()
        self.a.pack_forget()
        self.calendar.pack_forget()

    def show_calendarpage(self):
        self.time_label.place(x=self.root_width//1.15,y = self.root_height//50)
        self.a.pack(side = "top", expand= True,fill = tk.X,padx = (50,0))
        self.calendar.pack(side = "top")
   
    def hide_play_success(self):
        self.play_success_frame.place_forget()
        
    def show_play_success(self):
        self.play_success_frame.place(relx = 0.3,rely = 0.3,height = 100,width = 100)
        
    def hide_get_audio(self):
        self.getting_frame.place_forget()
        
    def show_get_audio(self):
        self.getting_frame.place(relx = 0.3,rely = 0.3,height = 100,width = 100) 
        
    def hide_test_frame(self):
        self.test_frame.place_forget()
        
    def show_test_frame(self):
        self.test_frame.place(relx = 0.3,rely = 0.3,height = 150,width = 150)     
        
    def load_event(self):
        point = 0
        fp = open(input_filepath + 'event_init.txt', "r",encoding="utf-8")
        line = fp.readline()
        while line:
               self.year_tag = int(line.replace('\n',''))
               line = fp.readline()
               print (self.year_tag)
               hour = int(line.replace('\n',' '))
               line = fp.readline()
               print (hour)
               #print line
               print("下一個")
               date[self.year_tag] = 1
               point+=1
        fp.close()
        
    def save(self):
        year = int(self.vYear.get())
        month = int(self.vMonth.get())        
        fp = open(input_filepath + 'event_init.txt', "a+",encoding="utf-8")
        fp.writelines(str(year))
        if month < 10:
         fp.writelines("0"+str(month))
        else:
         fp.writelines(str(month))
        if self.selday < 10:
         fp.writelines("0"+str(self.selday))
        else:
         fp.writelines(str(self.selday))   
        fp.writelines("\n")
        fp.writelines(str(self.detail_hour))
        fp.writelines(str(self.detail_min))
        fp.writelines("\n")
        self.point+=1
        fp.close()
        self.close_setting()
        self.updateDate()
        #self.Alarm1.config(text=self.alarm_activate[0])
        
    def calcFirstDayOfMonth(self,year,month,day):
          '''计算某一日的是星期几'''
          months = (0,31,59,90,120,151,181,212,243,273,304,334)
          if 0 <= month <= 12:
            sum = months[month - 1]
          else:
            print ('data error')
          # 对年月做了判断，日只是加了上下限，没有根据月判断输入的是否合法
          if year < 0 or month < 0 or month > 12 or day < 0 or day >31:
            os._exit(1)
             
          sum += day
          leap = 0
          if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            leap = 1
          if (leap == 1) and (month > 2):
            sum += 1
          # 先计算某年的第一天是星期几
          # (year + (year - 1)/4 - (year - 1)/100 + (year -1)/400)% 7
          return (sum % 7 - 1 + (year + (year - 1)/4 - (year - 1)/100 + (year -1)/400))% 7
      
    def createMonth(self):
          '''创建日历'''
          row = 0
          for i in range(6):
            for j in range(7):
              tk.Button(self.calendar,text = '',width = 5,height=2,bg='black', foreground="white").grid(row = i + 2,column = j)
              
    def updateDate(self):
          ''' 更新日历'''        
          #得到当前选择的日期
          year = int(self.vYear.get())
          month = int(self.vMonth.get())
          #day = int(self.vDay.get())
          months = [31,28,31,30,31,30,31,31,30,31,30,31]  
          # 判断是否瑞年
          if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            months[1] += 1
          fd = self.calcFirstDayOfMonth(year,month,1)
          for i in range(6):
            for j in range(7):
              self.calendar.grid_slaves(i +2,j)[0]['text'] = ''
              tk.Button(self.calendar,width = 5,height = 2,bg='black', foreground="white").grid(row=i+2,column=j)
          row=0
          for i in range(1,months[month - 1] + 1):
             tag = year*10000 + month*100 + i
             date[tag] = 0
             
          self.load_event()
          
          for i in range(1,months[month - 1] + 1):
             tag = year*10000 + month*100 + i
             if(int((i + fd -1)%7)==0):
                row +=1
             self.fku(i,row,fd,tag)
             
    def fku(self,i,row,fd,tag):
        if date[tag] == 1:
                tk.Button(self.calendar,bg='yellow', foreground="black", command=lambda: self.open_setting(i),text= i,width = 5,height = 2).grid(row=int((i + fd - 1)//7 +2),column=int((i + fd -1)%7))
        else:
                tk.Button(self.calendar,bg='black', foreground="white", command=lambda: self.open_setting(i),text= i,width = 5,height = 2).grid(row=int((i + fd - 1)//7 +2),column=int((i + fd -1)%7))  
    
    def adjust_alarm(self, pos, num):#hour or min, +1 or -1
        if(pos == 0):
            self.detail_hour = self.detail_hour + num
            if(self.detail_hour<0 or self.detail_hour>23):
                self.detail_hour = self.detail_hour%24
        if(pos == 1):              
            self.detail_min = self.detail_min+ num
            if(self.detail_min<0 or self.detail_min>59):
                self.detail_min = self.detail_min%60
        self.alarm_set_hour.config(text=str(self.detail_hour).zfill(2)+" : "+str(self.detail_min).zfill(2))
        
    def open_setting(self,day):
        self.selyear = int(self.vYear.get())
        self.selmonth = int(self.vMonth.get())
        self.a.pack_forget()
        self.calendar.pack_forget()
        dictionary = self.get_event(self.selyear,self.selmonth,day)
        self.settingPage.pack(side = "top", expand= True,fill = tk.BOTH)
        self.year_label.config(text =  str(self.selyear)+"年")
        self.month_label.config(text =  str(self.selmonth)+"月")
        self.day_label.config(text = str(day)+"號")
        self.selday = day
        self.event_list.delete(0, self.event_list.size()-1)
        for i in range(0,len(dictionary)):
            self.event_list.insert(i, dictionary[i])
        self.hide_test_frame()
        
    def close_setting(self):
        self.settingPage.pack_forget()
        self.a.pack(side = "top", expand= True,fill = tk.X,padx = (50,0))        
        self.calendar.pack(side = "top")
        
    def cal_year(self,i):
        year = int(self.vYear.get())  + i
        self.vYear.set(str(year))
        self.omYear.config(text =  self.vYear.get())
        self.updateDate()
    def cal_month(self,i):
        month = int(self.vMonth.get()) + i
        if 1 <= month <=12 :
            self.vMonth.set(str(month))
            self.omMonth.config(text =  self.vMonth.get())
            self.updateDate()
            
    def play_event(self):
        tag = self.event_list.curselection()
        file_name =input_filepath+self.event_list.get(tag)     
        pygame.init()
        pygame.mixer.init()
        
        print(file_name)
        pygame.mixer.Sound(file_name).play()
        '''CHUNK = 256
        RATE = 11025                # 采样率
        RECORD_SECONDS = 10
        path = input_filepath + file_name
        f = wave.open(path,"rb")
        p = pyaudio.PyAudio()
        #open stream
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
        				channels = f.getnchannels(),
        				rate = f.getframerate(),
        				output = True)
        #read data
        data = f.readframes(CHUNK)
         
        #paly stream
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        	stream.write(data)
        	data = f.readframes(CHUNK)
         
        #stop stream
        print("stop")
        stream.stop_stream()
        stream.close()
         
        #close PyAudio
        p.terminate()'''
        
    def get_event(self,year,month,day):
        date = year*10000 + month*100 + day
        fp = open(input_filepath + 'event_init.txt', "r",encoding="utf-8")
        line = fp.readline()
        filename_dict = {0:"無"}
        i = 0
        while line:
               year = str(line.replace('\n',''))
               line = fp.readline()
               print (year)
               hour = str(line.replace('\n',''))
               line = fp.readline()
               print (hour)
               #print line
               if ( str(date) == year):
                   file_name = year + hour
                   filename_dict[i] = file_name+".wav"
                   i += 1
        for i in range(0,len(filename_dict)):
            print(filename_dict[i])
        return filename_dict
    
    def test_play(self):
        print(5566)
        CHUNK = 256
        RATE = 11025                # 采样率
        RECORD_SECONDS = 10
        print(self.file_path)
        pygame.init()
        pygame.mixer.init()
        
        print(self.file_name)
        pygame.mixer.Sound(self.file_name).play()
        '''f = wave.open(self.file_path,"rb")
        p = pyaudio.PyAudio()
        #open stream
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
        				channels = f.getnchannels(),
        				rate = f.getframerate(),
        				output = True)
        #read data
        data = f.readframes(CHUNK)
         
        #paly stream
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        	stream.write(data)
        	data = f.readframes(CHUNK)
         
        #stop stream
        print("stop")
        stream.stop_stream()
        stream.close()
         
        #close PyAudio
        p.terminate()'''
    def play_audio(self):
        #define stream chunk 
        CHUNK = 256
        RATE = 11025                # 采样率
        RECORD_SECONDS = 10
        if self.selmonth < 10:
            if self.selday < 10:
               file_name = str(self.selyear)+"0"+str(self.selmonth)+"0"+str(self.selday)
            else:
               file_name = str(self.selyear)+"0"+str(self.selmonth)+str(self.selday)  
        else:
            if self.selday < 10:
               file_name = str(self.selyear)+str(self.selmonth)+"0"+str(self.selday)
            else:
               file_name = str(self.selyear)+str(self.selmonth)+str(self.selday) 
        print(file_name)
        point = 0
        fp = open(input_filepath + 'event_init.txt', "r",encoding="utf-8")
        line = fp.readline()
        while line:
               year = str(line.replace('\n',''))
               line = fp.readline()
               print (year)
               hour = str(line.replace('\n',''))
               line = fp.readline()
               print (hour)
               #print line
               if ( file_name == year):
                    path = input_filepath+file_name + str(hour)+".wav"
                    print(path)
                    pygame.init()
                    pygame.mixer.init()
        
                    print(path)
                    pygame.mixer.Sound(path).play()
                    time.sleep(10)
                    #open a wav format music
               print("下一個")
               point+=1
        fp.close()
        self.show_play_success()
    def get_audio(self):
        if self.selmonth < 10:
            if self.selday < 10:
               self.file_path = input_filepath + str(self.selyear)+"0"+str(self.selmonth)+"0"+str(self.selday)+str(self.detail_hour)+str(self.detail_min)+".wav"
            else:
               self.file_path = input_filepath + str(self.selyear)+"0"+str(self.selmonth)+str(self.selday)+str(self.detail_hour)+str(self.detail_min)+".wav"  
        else:
            if self.selday < 10:
               self.file_path = input_filepath + str(self.selyear)+str(self.selmonth)+"0"+str(self.selday)+str(self.detail_hour)+str(self.detail_min)+".wav"
            else:
               self.file_path = input_filepath + str(self.selyear)+str(self.selmonth)+str(self.selday)+str(self.detail_hour)+str(self.detail_min)+".wav" 
        print(self.file_path)
        CHUNK = 256
        FORMAT = pyaudio.paInt16
        CHANNELS = 1                # 声道数
        RATE = 11025                # 采样率
        RECORD_SECONDS = 10
        WAVE_OUTPUT_FILENAME = self.file_path
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        #开始录音：请在10秒内输入语音"
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        #"录音结束

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        self.hide_get_audio()
        self.show_test_frame()
        
    def drawHeader(self):
      '''添加日历头'''
      # 得到当前的日期，设置为默认值
      now = time.localtime(time.time())
      col_idx = 0
       
      # 创建年份组件
      self.vYear = tk.StringVar()
      self.vYear.set(now[0])
      minus_year = tk.Button(self.a,bg='black', foreground="white", text="-", command=lambda: self.cal_year(-1), width=2, font = ('Sans','10'))
      minus_year.grid(row = 0,column = col_idx);col_idx += 1
      self.omYear = tk.Label(self.a,text=str(self.vYear.get()), font=("Arial",10),background='black', foreground="white",width = 5,height = 2)#tk.OptionMenu(self.calendar,self.vYear , *tuple(range(1998,2080)))
      self.omYear.grid(row = 0,column = col_idx);col_idx += 1
      plus_year = tk.Button(self.a,bg='black', foreground="white", text="+", command=lambda: self.cal_year(1), width=2, font = ('Sans','10'))
      plus_year.grid(row = 0,column = col_idx);col_idx += 1    
      tk.Label(self.a,text = '年',width = 5,height = 2,background='black', foreground="white").grid(row = 0,column = col_idx);col_idx += 1
      # 创建月份组件
      self.vMonth = tk.StringVar()
      self.vMonth.set(now[1])
      self.omMonth = tk.OptionMenu(self.a,self.vMonth, *tuple(range(1,13)))
      self.omMonth.config(bg = "black",foreground = 'white') 
      self.omMonth.grid(row = 0,column = col_idx);col_idx += 1
      tk.Label(self.a,text = '月',width = 5,height = 2,background='black', foreground="white").grid(row = 0,column = col_idx);col_idx += 1
      # 创建年份组件
      #self.vDay = tk.StringVar()
      #self.vDay.set(now[2])
      #tk.Label(self.calendar,text = 'DAY').grid(row = 0,column = col_idx);col_idx += 1
      #omDay = tk.OptionMenu(self.calendar,self.vDay ,*tuple(range(1,32)))
      #omDay.grid(row = 0,column = col_idx);col_idx += 1
     
     
      # 打印星期标签
      weeks = ['Sun.','Mon.','Tues.','Wed.','Thurs.','Fri.','Sat.']
      col = 0
      for week in weeks:
        tk.Label(self.calendar,text = week,background='black', foreground="white").grid(row = 1,column = weeks.index(week)+col) 

    def play_daily_event(self):
        print(time.localtime())
        if time.localtime().tm_mon < 10:
            if time.localtime().tm_mday < 10:
               file_name = str(time.localtime().tm_year)+"0"+str(time.localtime().tm_mon)+"0"+str(time.localtime().tm_mday)
            else:
               file_name = str(time.localtime().tm_year)+"0"+str(time.localtime().tm_mon)+str(time.localtime().tm_mday)  
        else:
            if time.localtime().tm_mday< 10:
               file_name = str(time.localtime().tm_year)+str(time.localtime().tm_mon)+"0"+str(time.localtime().tm_mday)
            else:
               file_name = str(time.localtime().tm_year)+str(time.localtime().tm_mon)+str(time.localtime().tm_mday) 

        pygame.init()
        pygame.mixer.init()
        fp = open('event/event_init.txt', "r",encoding="utf-8")
        line = fp.readline()
        point = 0
        while line:
               year = str(line.replace('\n',''))
               line = fp.readline()
               hour = str(line.replace('\n',''))
               line = fp.readline()
               #print line
               if ( file_name == year):
                   path = input_filepath + file_name+hour+".wav"
                   point = point +1
                   print(path)
                   pygame.mixer.Sound(path).play()
                   time.sleep(10)
               print("end")
        if (point == 0):
            default = input_filepath + "default.mp3"
            print(default)
            pygame.mixer.music.load(default)
            pygame.mixer.music.play()
        fp.close()

        
        
 