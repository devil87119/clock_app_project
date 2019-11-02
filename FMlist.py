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
               "政大之聲" : "http://140.119.169.34:8000/ade.taiwan.ogg",
               "輔大之聲" : "http://140.136.115.115:8000/fjuvoice885.mp3",
               "東華之聲" : "http://radio.ndhu.edu.tw/radio.mp3",
               "飛特電台" : "https://phate.io/listen.ogg",
               "Family977古典音樂" : "http://59.120.88.155:8000/live.mp3",
               "城市广播" : "http://fm983.cityfm.tw:8080/983.mp3",
               "警廣":"http://www.pbs.gov.tw/live/tps.html",
           }

fm_code={
               0 : "政大之聲",
               1 : "輔大之聲",
               2 : "東華之聲",
               3 : "飛特電台",
               4 : "Family977古典音樂",
               5 : "城市广播",
               6 :  "警廣",
           }

fm_name_code={
               (0,) : 0,
               (1,) : 1,
               (2,) : 2,
               (3,) : 3,
               (4,) : 4,
               (5,) : 5,
               (6,) : 6,
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

