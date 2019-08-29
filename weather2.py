# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:47:05 2019

@author: 阿新
"""
import pandas as pd

order=[0,1,2,3,5,6,8,12,13,14,17,18,20,24,25,26,29,30,32,36,37,38,41,42]#字元陣列中天氣需要的元素

city_weather={
        0 : 'https://www.cwb.gov.tw/V7/forecast/taiwan/Keelung_City.htm',
        1 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm",
        2 : "https://www.cwb.gov.tw/V7/forecast/taiwan/New_Taipei_City.htm",
        3 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Taoyuan_City.htm",
        4 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_City.htm",
        5 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_County.htm",
        6 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Miaoli_County.htm",
        7 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Taichung_City.htm",
        8 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Changhua_County.htm",
        9 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Nantou_County.htm",
        10 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Yunlin_County.htm",
        11 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Chiayi_City.htm",
        13 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Chiayi_County.htm",
        14 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Yilan_County.htm",
        15 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Hualien_County.htm",
        16 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Taitung_County.htm",
        17 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Tainan_City.htm",
        18 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Kaohsiung_City.htm",
        19 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Pingtung_County.htm",
        20 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Lienchiang_County.htm",
        21 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Kinmen_County.htm",
        22 : "https://www.cwb.gov.tw/V7/forecast/taiwan/Penghu_County.htm",
        23 :"https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W42.pdf?"
 }

city_code={
        "基隆市" : 0, "臺北市" : 1, "新北市" : 2, "桃園市" : 3, "新竹市" : 4, "新竹縣" : 5,
        "苗栗縣" : 6, "臺中市" : 7, "彰化縣" : 8, "南投縣" : 9, "雲林縣" :10, "嘉義市" :11,
        "嘉義縣" :13, "宜蘭縣" :14, "花蓮縣" :15, "臺東縣" :16, "臺南市" :17, "高雄市" :18,
        "屏東縣" :19, "連江縣" :20, "金門縣" :21, "澎湖縣" :22
}

class Weather():
    def __init__(self):
        self.city_name = "基隆市"     
        self.openhtml=city_weather[city_code[self.city_name]]
        self.out=pd.read_html(self.openhtml)  #網頁抓取
        self.t = str(self.out[0])
        self.Month_state=self.t.split()
        
    def print_city(self):
        return self.Month_state[order[0]]
    
    def print_night_temperature(self):#今晚到明晨溫度range
        return self.Month_state[order[7]]+self.Month_state[order[2]]
    
    def print_day_temperature(self):#明日白天溫度range
        return self.Month_state[order[13]]+self.Month_state[order[2]]
    
    def print_night_rain_percent(self):#今晚到明晨降雨機率
        return self.Month_state[order[10]]+self.Month_state[order[11]]
    
    def print_day_rain_percent(self):#明日白天降雨機率
        return self.Month_state[order[16]]+self.Month_state[order[17]]
    
    #def set_city_name(self):
        
'''
city_input=input() #縣市input
openhtml=city_weather[city_input]
out=pd.read_html(openhtml)  #網頁抓取
#print(len(out))
t = str(out[0])
Month_state=t.split()
print(Month_state[order[0]]+'       ',end='')   #縣市
print(Month_state[order[1]],end='')  #溫度
print(Month_state[order[2]]+'  ',end='') #天氣概況
print(Month_state[order[3]]+'   ',end='')  
print(Month_state[order[4]],end='') #降雨
print(Month_state[order[5]]+' '+'\n',end='')
print(Month_state[order[6]]+'     ',end='')   #今晚到明晨
print(Month_state[order[7]],end='') #溫度range
print(Month_state[order[8]],end='')
print(Month_state[order[9]]+'                ',end='')
print(Month_state[order[10]],end='') #降雨機率
print(Month_state[order[11]]+'\n',end='')
print(Month_state[order[12]]+'       ',end='')   #明日白天
print(Month_state[order[13]],end='')#溫度
print(Month_state[order[14]],end='')
print(Month_state[order[15]]+'                ',end='')
print(Month_state[order[16]],end='')#降雨機率
print(Month_state[order[17]],end='')
'''
            
            
            
            
 