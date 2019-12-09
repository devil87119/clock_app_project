import re
import requests
from googletrans import Translator
from weather_page import *

city_dic={ "Keelung" : "基隆市", "Taipei" : "臺北市", "New Taipei" : "新北市", 
               "Taoyuan" : "桃園市", "Hsinchu" : "新竹","Miaoli" : "苗栗縣", "Taichung" : "臺中市",
               "Changhua" : "彰化縣", "Nantou" : "南投縣", "Yunlin" :"雲林縣", "Chiayi" :"嘉義", 
                "Yilan" :"宜蘭縣", "Hualien" :"花蓮縣", "Taitung" :"臺東縣", "Tainan" :"臺南市",
                "Kaohsiung" :"高雄市", "Pingtung" :"屏東縣", "Lianjiang" :"連江縣", "Jincheng" :"金門縣", 
               "Ma-kung" :"澎湖縣","Beijing":"北京","Tokyo":"東京","Seoul":"首爾",
               "Boston":"波士頓","Canada":"加拿大","usa":"美國"}
class Weather():
    def __init__(self,s):
        self.city_name=s   
        self.detail_city_name=s
    def get_weather(self,name):
        self.weather_key = 'c11aa0e93bd1ecb70d85001f5af276d4'
        self.url = 'https://api.openweathermap.org/data/2.5/weather'
        self.params = {'APPID': self.weather_key, 'q': name, 'units':'Metric'}
        self.response = requests.get(self.url, params=self.params)
        self.weather_json = self.response.json()
        return self.weather_json
        
    
    def trans_to_ch(self,en):
        self.en_translator=Translator()
        self.english=self.en_translator.translate(en,dest='zh-TW').text
        return self.english
    def trans_to_en(self,ch):
        self.ch_translator=Translator()
        self.chinese=self.ch_translator.translate(ch,dest='en').text
        return self.chinese
    def print_city(self):
        if(city_dic[self.city_name]):
            return city_dic[self.city_name]
        return self.trans_to_ch(self.city_name)
    
    def print_night_temperature(self):#今日溫度
        return str(self.get_weather(self.city_name)['main']['temp'])
    
    def print_day_rain_percent(self):#今日濕度
        return str(self.get_weather(self.city_name)['main']['humidity'])
    def print_weather_description(self):
        self.description=self.get_weather(self.detail_city_name)
        return self.description
                
    def icon_name(self):
        return self.get_weather(self.city_name)['weather'][0]['icon']
    def icon_name2(self):
        return self.get_weather(self.detail_city_name)['weather'][0]['icon']
    '''
    def print_night_temperature2(self):#今日溫度
        return self.get_weather(self.trans_to_en(self.detail_city_name))['main']['temp']
    def print_night_rain_percent2(self):#今日濕度
        return self.get_weather(self.trans_to_en(self.detail_city_name))['main']['humidity']
    '''
    
    def change_city(self,s):
        self.city_name=s
        print(self.city_name)
    def detail_change_city(self,c):
        self.detail_city_name=c
        print(self.detail_city_name)
    
