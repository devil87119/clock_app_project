# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:52:48 2019

@author: 楊秉翰
"""

import tkinter as tk
import time

class Alarm:
    def __init__(self, root, root_height):
        #page size
        self.root = root
        self.root_height = root_height
        self.root_width = int(self.root_height/5.1*7.6)
        
        #alarm attribute
        self.alarm_activate = [0, 0, 0, 0, 0, 0]#0 : 關閉,  1: 啟動
        self.alarm_set = dict()#設定鬧鐘時間
        self.alarm_song = dict()#設定歌曲
        self.alarm_ring_time = [30, 180, 300]#響鈴時間
        self.alarm_repeat = [0, 3, 5, 10000]#重複次數
        self.alarm_temp = dict()#站存鬧鈴時間

    