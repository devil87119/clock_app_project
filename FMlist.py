# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:32:25 2019

@author: 士賢
"""

#!/usr/bin/python
import time
import os
import pygame
#import sys
#import RPi.GPIO as GPIO

#words=[]

fm_address={
               #"政大之聲" : "http://140.119.169.34:8000/ade.taiwan.ogg",
               "輔大之聲" : "http://140.136.115.115:8000/fjuvoice885.mp3",
               "東華之聲" : "http://radio.ndhu.edu.tw/radio.mp3",
               "飛特電台" : "https://phate.io/listen.ogg",
               "Family977古典音樂" : "http://59.120.88.155:8000/live.mp3",
               "城市广播" : "http://fm983.cityfm.tw:8080/983.mp3",
               "臺北電台931":"http://flv.ccdntech.com/live/_definst_/mp4:vod256_Live/fm/chunklist_w1096389398.m3u8",
               "民本一台":"rtmp://flv.ccdntech.com:1935/live/mp4:vod194_Live/am1296",
               "民本二台":"rtmp://flv.ccdntech.com:1935/live/mp4:vod194_Live/am855",
               "臺北國際社區廣播電台":"http://live.leanstream.co/ICRTFM-MP3",
               "ICRT":"http://live.leanstream.co/ICRTFM-MP3",
               "大千電台":"http://stream.superfm99-1.com.tw:8554",
               "1766百家知識":"http://livestream.1766.today:1768/live1.mp3",
               "1766店頭音樂":"http://livestream.1766.today:1781/live2.mp3",
               "大汗之音":"http://flv.ccdntech.com/live/_definst_/mp4:vod229_Live/FM971/playlist.m3u8m",
               "金聲廣播電台":"http://60.249.186.105:9000/;?icy=http",
               "台中929":"http://fm929.cityfm.tw:8000/929.mp3",
               "台北健康":"http://fm901.cityfm.tw:8000/901.mp3",
               "大苗栗广播":"http://fm983.cityfm.tw:8080/983.mp3",
               "台南知音":"http://fm971.cityfm.tw:8080/971.mp3",
               "台藝之聲":"http://video.ntua.edu.tw/live/ntua/index.m3u8",
               
           }

fm_code={
               0: "輔大之聲",
               1 : "東華之聲",
               2 : "飛特電台",
               3 : "Family977古典音樂",
               4 : "城市广播",
               5 : "臺北電台931",
               6 : "民本一台",
               7 : "民本二台",
               8 : "臺北國際社區廣播電台",
               9 : "ICRT",
               10: "大千電台",
               11: "1766百家知識",
               12: "1766店頭音樂",
               13: "大汗之音",
               14: "金聲廣播電台",
               15: "台中929",
               16: "台北健康",
               17: "大苗栗广播",
               18: "台南知音",
               19: "台藝之聲",
           }

fm_name_code={
               (0,) : 0,
               (1,) : 1,
               (2,) : 2,
               (3,) : 3,
               (4,) : 4,
               (5,) : 5,
               (6,) : 6,
               (7,) : 7,
               (8,) : 8,
               (9,) : 9,
               (10,) : 10,
               (11,) : 11,
               (12,) : 12,
               (13,) : 13,
               (14,) : 14,
               (15,) : 15,
               (16,) : 16,
               (17,) : 17,
               (18,) : 18,
               (19,) : 19,
               ()  : 0,
           }


class FM():
    def __init__(self):
        self.FM_name_code = 0
        self.FM_code = ()
        self.FM_Address=fm_address[fm_code[self.FM_name_code]]
        #self.out=pd.read_html(self.openhtml)  #網頁抓取


        
    def print_FM_Name(self):
        return fm_code[self.FM_name_code]
    
    def play_FM(self):
        c =fm_name_code[self.FM_code]
        self.FM_Address=fm_address[fm_code[c]]
        
        #pygame
        #track = pygame.mixer.music.load(self.FM_Address)
        #pygame.mixer.music.play()
        
        os.system('mpc clear')
        os.system("sudo mpc add "+self.FM_Address)
        os.system("sudo  mpc play&")
        
        
    def stop_FM(self):
        #os.kill(self.fd)
        #pygame.mixer.music.stop()
        os.system("sudo mpc stop&")



#os.system('mpc play &')
'''#i=0
action=0
wordlen=len(words)
try:
    
    while True:
        print("1")
        if GPIO.input(23) == 1:
            i=i+1
            action=1
            #print("button")
            #os.system("mpc next ")
        if GPIO.input(24)==1:
            i=i-1
            action=1
            #print("3")
            os.system("sudo mpc stop ")
        if action==1:
            if i<0:
                i=wordlen-1
            if i >=wordlen:
                i=0
            print ("-------------------------------")
            print (i)
            print (words[i])
            action=0
            #os.system("sudo mpc stop")
            print("2")
            os.system("sudo mpc del 1")
            print('3')
            os.system("sudo mpc add "+words[i])
            print("add")
            os.system("sudo  mpc play&")
            print("play")
        time.sleep(0.1);
except KeyboardInterrupt:
    os.system("sudo mpc stop")
    print("stop")
GPIO.cleanup()#'''

