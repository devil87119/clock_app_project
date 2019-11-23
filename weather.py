import re
import requests

url="https://www.cwb.gov.tw/Data/js/TableData_36hr_County_C.js?"
res=requests.get(url)
res.encoding="utf-8"
html_doc=res.text
html_doc = re.sub("[A-Za-z\u4e00-\u9fa5!\%\[\]\,\。]", "",html_doc)
data=html_doc.split()


keelung1=str(data[8:11])   #基隆-今晚明晨
keelung1=re.sub("'':","",keelung1)
keelung2=str(data[11:14])  #基隆-明日白天
keelung2=re.sub("'':","",keelung2)
keelung3=str(data[14:17])   #基隆-明日晚上
keelung3=re.sub("'':","",keelung3)

taipei1=str(data[18:21])
taipei1=re.sub("'':","",taipei1)
taipei2=str(data[21:24])
taipei2=re.sub("'':","",taipei2)
taipei3=str(data[24:27])
taipei3=re.sub("'':","",taipei3)

new_taipei1=str(data[28:31])
new_taipei1=re.sub("'':","",taipei1)
new_taipei2=str(data[31:34])
new_taipei2=re.sub("'':","",new_taipei2)
new_taipei3=str(data[34:37])
new_taipei3=re.sub("'':","",new_taipei3)

taoyuan1=str(data[38:41])
taoyuan1=re.sub("'':","",taoyuan1)
taoyuan2=str(data[41:44])
taoyuan2=re.sub("'':","",taoyuan2)
taoyuan3=str(data[44:47])
taoyuan3=re.sub("'':","",taoyuan3)

Hsinchu1=str(data[48:51])
Hsinchu1=re.sub("'':","",taoyuan1)
Hsinchu2=str(data[51:54])
Hsinchu2=re.sub("'':","",Hsinchu2)
Hsinchu3=str(data[54:57])
Hsinchu3=re.sub("'':","",Hsinchu3)

HsinchuS1=str(data[58:61])
HsinchuS1=re.sub("'':","",taoyuan1)
HsinchuS2=str(data[61:64])
HsinchuS2=re.sub("'':","",HsinchuS2)
HsinchuS3=str(data[64:67])
HsinchuS3=re.sub("'':","",HsinchuS3)

miaoli1=str(data[68:71])
miaoli1=re.sub("'':","",miaoli1)
miaoli2=str(data[71:74])
miaoli2=re.sub("'':","",miaoli2)
miaoli3=str(data[74:77])
miaoli3=re.sub("'':","",miaoli3)

taichung1=str(data[78:81])
taichung1=re.sub("'':","",taichung1)
taichung2=str(data[81:84])
taichung2=re.sub("'':","",taichung2)
taichung3=str(data[84:87])
taichung3=re.sub("'':","",taichung3)

Changhua1=str(data[88:91])
Changhua1=re.sub("'':","",Changhua1)
Changhua2=str(data[91:94])
Changhua2=re.sub("'':","",Changhua2)
Changhua3=str(data[94:97])
Changhua3=re.sub("'':","",Changhua3)

Nantou1=str(data[98:101])
Nantou1=re.sub("'':","",Nantou1)
Nantou2=str(data[101:104])
Nantou2=re.sub("'':","",Nantou2)
Nantou3=str(data[104:107])
Nantou3=re.sub("'':","",Nantou3)

Yunlin1=str(data[108:111])
Yunlin1=re.sub("'':","",Yunlin1)
Yunlin2=str(data[111:114])
Yunlin2=re.sub("'':","",Yunlin2)
Yunlin3=str(data[114:117])
Yunlin3=re.sub("'':","",Yunlin3)

Chiayi1=str(data[118:121])
Chiayi1=re.sub("'':","",Chiayi1)
Chiayi2=str(data[121:124])
Chiayi2=re.sub("'':","",Chiayi2)
Chiayi3=str(data[124:127])
Chiayi3=re.sub("'':","",Chiayi3)

ChiayiS1=str(data[128:131])
ChiayiS1=re.sub("'':","",ChiayiS1)
ChiayiS2=str(data[131:134])
ChiayiS2=re.sub("'':","",ChiayiS2)
ChiayiS3=str(data[134:137])
ChiayiS3=re.sub("'':","",ChiayiS3)

Tainan1=str(data[138:141])
Tainan1=re.sub("'':","",Tainan1)
Tainan2=str(data[141:144])
Tainan2=re.sub("'':","",Tainan2)
Tainan3=str(data[144:147])
Tainan3=re.sub("'':","",Tainan3)

Kaohsiung1=str(data[148:151])
Kaohsiung1=re.sub("'':","",Kaohsiung1)
Kaohsiung2=str(data[151:154])
Kaohsiung2=re.sub("'':","",Kaohsiung2)
Kaohsiung3=str(data[154:157])
Kaohsiung3=re.sub("'':","",Kaohsiung3)

Pingtung1=str(data[158:161])
Pingtung1=re.sub("'':","",Pingtung1)
Pingtung2=str(data[161:164])
Pingtung2=re.sub("'':","",Pingtung2)
Pingtung3=str(data[164:167])
Pingtung3=re.sub("'':","",Pingtung3)

Yilan1=str(data[168:171])
Yilan1=re.sub("'':","",Yilan1)
Yilan2=str(data[171:174])
Yilan2=re.sub("'':","",Yilan2)
Yilan3=str(data[174:177])
Yilan3=re.sub("'':","",Yilan3)

Hualien1=str(data[178:181])
Hualien1=re.sub("'':","",Hualien1)
Hualien2=str(data[181:184])
Hualien2=re.sub("'':","",Hualien2)
Hualien3=str(data[184:187])
Hualien3=re.sub("'':","",Hualien3)

Taitung1=str(data[188:191])
Taitung1=re.sub("'':","",Taitung1)
Taitung2=str(data[191:194])
Taitung2=re.sub("'':","",Taitung2)
Taitung3=str(data[194:197])
Taitung3=re.sub("'':","",Taitung3)

Penghu1=str(data[198:201])
Penghu1=re.sub("'':","",Penghu1)
Penghu2=str(data[201:204])
Penghu2=re.sub("'':","",Penghu2)
Penghu3=str(data[204:207])
Penghu3=re.sub("'':","",Penghu3)

Jinmen1=str(data[208:211])
Jinmen1=re.sub("'':","",Jinmen1)
Jinmen2=str(data[211:214])
Jinmen2=re.sub("'':","",Jinmen2)
Jinmen3=str(data[214:217])
Jinmen3=re.sub("'':","",Jinmen3)

Lianjiang1=str(data[218:221])
Lianjiang1=re.sub("'':","",Lianjiang1)
Lianjiang2=str(data[221:224])
Lianjiang2=re.sub("'':","",Lianjiang2)
Lianjiang3=str(data[224:227])
Lianjiang3=re.sub("'':","",Lianjiang3)


now_city={"基隆市":0, "臺北市":3, "新北市":6, "桃園市":9, "新竹市":12, "新竹縣":15,
          "苗栗縣":18, "臺中市":21, "彰化縣":24, "南投縣":27, "雲林縣":30, "嘉義市":33,
          "嘉義縣":36, "宜蘭縣":39, "花蓮縣":42, "臺東縣":45, "臺南市":48, "高雄市":51,
          "屏東縣":54, "連江縣":57, "金門縣":60, "澎湖縣":63}

temp=[
      keelung1[41:43]+"℃"+" "+keelung1[19]+" "+keelung1[45:47]+"℃",keelung2[41:43]+"℃"+" "+keelung2[19]+" "+keelung2[45:47]+"℃",keelung3[41:43]+"℃"+" "+keelung3[19]+" "+keelung3[45:47]+"℃"
     ,taipei1[41:43]+"℃"+" "+taipei1[19]+" "+taipei1[45:47]+"℃",taipei2[41:43]+"℃"+" "+taipei2[19]+" "+taipei2[45:47]+"℃",taipei3[41:43]+"℃"+" "+taipei3[19]+" "+taipei3[45:47]+"℃"
     ,new_taipei1[41:43]+"℃"+" "+new_taipei1[19]+" "+new_taipei1[45:47]+"℃",new_taipei2[41:43]+"℃"+" "+new_taipei2[19]+" "+new_taipei2[45:47]+"℃",new_taipei3[41:43]+"℃"+" "+new_taipei3[19]+" "+new_taipei3[45:47]+"℃"
     ,taoyuan1[41:43]+"℃"+" "+taoyuan1[19]+" "+taoyuan1[45:47]+"℃",taoyuan2[41:43]+"℃"+" "+taoyuan2[19]+" "+taoyuan2[45:47]+"℃",taoyuan3[41:43]+"℃"+" "+taoyuan3[19]+" "+taoyuan3[45:47]+"℃"
     ,Hsinchu1[41:43]+"℃"+" "+Hsinchu1[19]+" "+Hsinchu1[45:47]+"℃",Hsinchu2[41:43]+"℃"+" "+Hsinchu2[19]+" "+Hsinchu2[45:47]+"℃",Hsinchu3[41:43]+"℃"+" "+Hsinchu3[19]+" "+Hsinchu3[45:47]+"℃"
     ,HsinchuS1[41:43]+"℃"+" "+HsinchuS1[19]+" "+HsinchuS1[45:47]+"℃",HsinchuS2[41:43]+"℃"+" "+HsinchuS2[19]+" "+HsinchuS2[45:47]+"℃",HsinchuS3[41:43]+"℃"+" "+HsinchuS3[19]+" "+HsinchuS3[45:47]+"℃"
     ,miaoli1[41:43]+"℃"+" "+miaoli1[19]+" "+miaoli1[45:47]+"℃",miaoli2[41:43]+"℃"+" "+miaoli2[19]+" "+miaoli2[45:47]+"℃",miaoli3[41:43]+"℃"+" "+miaoli3[19]+" "+miaoli3[45:47]+"℃"
     ,taichung1[41:43]+"℃"+" "+taichung1[19]+" "+taichung1[45:47]+"℃",taichung2[41:43]+"℃"+" "+taichung2[19]+" "+taichung2[45:47]+"℃",taichung3[41:43]+"℃"+" "+taichung3[19]+" "+taichung3[45:47]+"℃"
     ,Changhua1[41:43]+"℃"+" "+Changhua1[19]+" "+Changhua1[45:47]+"℃",Changhua2[41:43]+"℃"+" "+Changhua2[19]+" "+Changhua2[45:47]+"℃",Changhua3[41:43]+"℃"+" "+Changhua3[19]+" "+Changhua3[45:47]+"℃"
     ,Nantou1[41:43]+"℃"+" "+Nantou1[19]+" "+Nantou1[45:47]+"℃",Nantou2[41:43]+"℃"+" "+Nantou2[19]+" "+Nantou2[45:47]+"℃",Nantou3[41:43]+"℃"+" "+Nantou3[19]+" "+Nantou3[45:47]+"℃"
     ,Yunlin1[41:43]+"℃"+" "+Yunlin1[19]+" "+Yunlin1[45:47]+"℃",Yunlin2[41:43]+"℃"+" "+Yunlin2[19]+" "+Yunlin2[45:47]+"℃",Yunlin3[41:43]+"℃"+" "+Yunlin3[19]+" "+Yunlin3[45:47]+"℃"
     ,Chiayi1[41:43]+"℃"+" "+Chiayi1[19]+" "+Chiayi1[45:47]+"℃",Chiayi2[41:43]+"℃"+" "+Chiayi2[19]+" "+Chiayi2[45:47]+"℃",Chiayi3[41:43]+"℃"+" "+Chiayi3[19]+" "+Chiayi3[45:47]+"℃"
     ,ChiayiS1[41:43]+"℃"+" "+ChiayiS1[19]+" "+ChiayiS1[45:47]+"℃",ChiayiS2[41:43]+"℃"+" "+ChiayiS2[19]+" "+ChiayiS2[45:47]+"℃",ChiayiS3[41:43]+"℃"+" "+ChiayiS3[19]+" "+ChiayiS3[45:47]+"℃"
     ,Tainan1[41:43]+"℃"+" "+Tainan1[19]+" "+Tainan1[45:47]+"℃",Tainan2[41:43]+"℃"+" "+Tainan2[19]+" "+Tainan2[45:47]+"℃",Tainan3[41:43]+"℃"+" "+Tainan3[19]+" "+Tainan3[45:47]+"℃"
     ,Kaohsiung1[41:43]+"℃"+" "+Kaohsiung1[19]+" "+Kaohsiung1[45:47]+"℃",Kaohsiung2[41:43]+"℃"+" "+Kaohsiung2[19]+" "+Kaohsiung2[45:47]+"℃",Kaohsiung3[41:43]+"℃"+" "+Kaohsiung3[19]+" "+Kaohsiung3[45:47]+"℃"
     ,Pingtung1[41:43]+"℃"+" "+Pingtung1[19]+" "+Pingtung1[45:47]+"℃",Pingtung2[41:43]+"℃"+" "+Pingtung2[19]+" "+Pingtung2[45:47]+"℃",Pingtung3[41:43]+"℃"+" "+Pingtung3[19]+" "+Pingtung3[45:47]+"℃"
     ,Yilan1[41:43]+"℃"+" "+Yilan1[19]+" "+Yilan1[45:47]+"℃",Yilan2[41:43]+"℃"+" "+Yilan2[19]+" "+Yilan2[45:47]+"℃",Yilan3[41:43]+"℃"+" "+Yilan3[19]+" "+Yilan3[45:47]+"℃"
     ,Hualien1[41:43]+"℃"+" "+Hualien1[19]+" "+Hualien1[45:47]+"℃",Hualien2[41:43]+"℃"+" "+Hualien2[19]+" "+Hualien2[45:47]+"℃",Hualien3[41:43]+"℃"+" "+Hualien3[19]+" "+Hualien3[45:47]+"℃"
     ,Taitung1[41:43]+"℃"+" "+Taitung1[19]+" "+Taitung1[45:47]+"℃",Taitung2[41:43]+"℃"+" "+Taitung2[19]+" "+Taitung2[45:47]+"℃",Taitung3[41:43]+"℃"+" "+Taitung3[19]+" "+Taitung3[45:47]+"℃"
     ,Penghu1[41:43]+"℃"+" "+Penghu1[19]+" "+Penghu1[45:47]+"℃",Penghu2[41:43]+"℃"+" "+Penghu2[19]+" "+Penghu2[45:47]+"℃",Penghu3[41:43]+"℃"+" "+Penghu3[19]+" "+Penghu3[45:47]+"℃"
     ,Jinmen1[41:43]+"℃"+" "+Jinmen1[19]+" "+Jinmen1[45:47]+"℃",Jinmen2[41:43]+"℃"+" "+Jinmen2[19]+" "+Jinmen2[45:47]+"℃",Jinmen3[41:43]+"℃"+" "+Jinmen3[19]+" "+Jinmen3[45:47]+"℃"
     ,Lianjiang1[41:43]+"℃"+" "+Lianjiang1[19]+" "+Lianjiang1[45:47]+"℃",Lianjiang2[41:43]+"℃"+" "+Lianjiang2[19]+" "+Lianjiang2[45:47]+"℃",Lianjiang3[41:43]+"℃"+" "+Lianjiang3[19]+" "+Lianjiang3[45:47]+"℃"
     ]

rain=[
      keelung1[61:63]+"%",keelung3[61:63]+"%",keelung3[61:63]+"%"
     ,taipei1[61:63]+"%",taipei2[61:63]+"%",taipei3[61:63]+"%"
     ,new_taipei1[61:63]+"%",new_taipei2[61:63]+"%",new_taipei3[61:63]+"%"
     ,taoyuan1[61:63]+"%",taoyuan2[61:63]+"%",taoyuan3[61:63]+"%"
     ,Hsinchu1[61:63]+"%",Hsinchu2[61:63]+"%",Hsinchu3[61:63]+"%"
     ,HsinchuS1[61:63]+"%",HsinchuS2[61:63]+"%",HsinchuS3[61:63]+"%"
     ,miaoli1[61:63]+"%",miaoli2[61:63]+"%",miaoli3[61:63]+"%"
     ,taichung1[61:63]+"%",taichung2[61:63]+"%",taichung3[61:63]+"%"
     ,Changhua1[61:63]+"%",Changhua2[61:63]+"%",Changhua3[61:63]+"%"
     ,Nantou1[61:63]+"%",Nantou2[61:63]+"%",Nantou3[61:63]+"%"
     ,Yunlin1[61:63]+"%",Yunlin2[61:63]+"%",Yunlin3[61:63]+"%"
     ,Chiayi1[61:63]+"%",Chiayi2[61:63]+"%",Chiayi3[61:63]+"%"
     ,ChiayiS1[61:63]+"%",ChiayiS2[61:63]+"%",ChiayiS3[61:63]+"%"
     ,Tainan1[61:63]+"%",Tainan2[61:63]+"%",Tainan3[61:63]+"%"
     ,Kaohsiung1[61:63]+"%",Kaohsiung2[61:63]+"%",Kaohsiung3[61:63]+"%"
     ,Pingtung1[61:63]+"%",Pingtung2[61:63]+"%",Pingtung3[61:63]+"%"
     ,Yilan1[61:63]+"%",Yilan2[61:63]+"%",Yilan3[61:63]+"%"
     ,Hualien1[61:63]+"%",Hualien2[61:63]+"%",Hualien3[61:63]+"%"
     ,Taitung1[61:63]+"%",Taitung2[61:63]+"%",Taitung3[61:63]+"%"
     ,Penghu1[61:63]+"%",Penghu2[61:63]+"%",Penghu3[61:63]+"%"
     ,Jinmen1[61:63]+"%",Jinmen2[61:63]+"%",Jinmen3[61:63]+"%"
     ,Lianjiang1[61:63]+"%",Lianjiang2[61:63]+"%",Lianjiang3[61:63]+"%"
     ]

class Weather():
    def __init__(self,s):
        self.city_name=s
        self.citycode = now_city[self.city_name]     
        self.data=data
        self.detail_city_name=""
     
    def print_city(self):
        return self.city_name
    
    def print_night_temperature(self):#今晚到明晨溫度range
        return temp[now_city[self.city_name]]
    
    def print_day_temperature(self):#明日白天溫度range
        return temp[now_city[self.city_name]+1]
    
    def print_night_rain_percent(self):#今晚到明晨降雨機率
        return rain[now_city[self.city_name]]
    
    def print_day_rain_percent(self):#明日白天降雨機率
        return rain[now_city[self.city_name] +1]
    
    def print_night_temperature2(self):#今晚到明晨溫度range
        return temp[now_city[self.detail_city_name]]
    
    def print_day_temperature2(self):#明日白天溫度range
        return temp[now_city[self.detail_city_name]+1]
    
    def print_night_rain_percent2(self):#今晚到明晨降雨機率
        return rain[now_city[self.detail_city_name]]
    
    def print_day_rain_percent2(self):#明日白天降雨機率
        return rain[now_city[self.detail_city_name] +1]
    def change_city(self,s):
        self.city_name=s
    def detail_change_city(self,c):
        self.detail_city_name=c
    

    
'''
print("..........................................基隆市.........................................................")
keelung1=str(data[8:11])   #基隆-今晚明晨
keelung1=re.sub("'':","",keelung1)
print("今晚-明晨:"+keelung1[4:15]+" "+keelung1[19]+" "+keelung1[24:35])  #10/13-18:00 ~ 10/14-06:00 
print("溫度:"+keelung1[41:43]+"℃"+" "+keelung1[19]+" "+keelung1[45:47]+"℃")
print("降雨機率:"+keelung1[61:63]+"%")
#print("天氣概況:"+keelung1[79:81])
#print("天氣描述:"+keelung1[73:77])
keelung2=str(data[11:14])  #基隆-明日白天
keelung2=re.sub("'':","",keelung2)
print("明日白天:"+keelung2[4:15]+" "+keelung2[19]+" "+keelung2[24:35])
print("溫度:"+keelung2[41:43]+"℃"+" "+keelung2[19]+" "+keelung2[45:47]+"℃")
print("降雨機率:"+keelung2[61:63]+"%")
#print("天氣概況:"+keelung2[79:81])
#print("天氣描述:"+keelung2[73:77])
keelung3=str(data[14:17])   #基隆-明日晚上
keelung3=re.sub("'':","",keelung3)
print("明日晚上:"+keelung3[4:15]+" "+keelung3[19]+" "+keelung3[24:35])
print("溫度:"+keelung3[41:43]+"℃"+" "+keelung3[19]+" "+keelung3[45:47]+"℃")
print("降雨機率:"+keelung3[61:63]+"%")
#print("天氣概況:"+keelung3[79:81])
#print("天氣描述:"+keelung3[73:77])
print("..........................................臺北市.........................................................")
taipei1=str(data[18:21])
taipei1=re.sub("'':","",taipei1)
print("今晚-明晨:"+taipei1[4:15]+" "+taipei1[19]+" "+taipei1[24:35])
print("溫度:"+taipei1[41:43]+"℃"+" "+taipei1[19]+" "+taipei1[45:47]+"℃")
print("降雨機率:"+taipei1[61:63]+"%")
#print("天氣概況:"+taipei1[79:81])
#print("天氣描述:"+taipei1[73:77])
taipei2=str(data[21:24])
taipei2=re.sub("'':","",taipei2)
print("明日白天:"+taipei2[4:15]+" "+taipei2[19]+" "+taipei2[24:35])
print("溫度:"+taipei2[41:43]+"℃"+" "+taipei2[19]+" "+taipei2[45:47]+"℃")
print("降雨機率:"+taipei2[61:63]+"%")
#print("天氣概況:"+taipei2[79:81])
#print("天氣描述:"+taipei2[73:77])
taipei3=str(data[24:27])
taipei3=re.sub("'':","",taipei3)
print("明日晚上:"+taipei3[4:15]+" "+taipei3[19]+" "+taipei3[24:35])
print("溫度:"+taipei3[41:43]+"℃"+" "+taipei3[19]+" "+taipei3[45:47]+"℃")
print("降雨機率:"+taipei3[61:63]+"%")
#print("天氣概況:"+taipei3[79:81])
#print("天氣描述:"+taipei3[73:77])
print("..........................................新北市.........................................................")
new_taipei1=str(data[28:31])
new_taipei1=re.sub("'':","",taipei1)
print("今晚-明晨:"+new_taipei1[4:15]+" "+new_taipei1[19]+" "+new_taipei1[24:35])
print("溫度:"+new_taipei1[41:43]+"℃"+" "+new_taipei1[19]+" "+new_taipei1[45:47]+"℃")
print("降雨機率:"+new_taipei1[61:63]+"%")
#print("天氣概況:"+new_taipei1[79:81])
#print("天氣描述:"+new_taipei1[73:77])
new_taipei2=str(data[31:34])
new_taipei2=re.sub("'':","",new_taipei2)
print("明日白天:"+new_taipei2[4:15]+" "+new_taipei2[19]+" "+new_taipei2[24:35])
print("溫度:"+new_taipei2[41:43]+"℃"+" "+new_taipei2[19]+" "+new_taipei2[45:47]+"℃")
print("降雨機率:"+new_taipei2[61:63]+"%")
#print("天氣概況:"+new_taipei2[79:81])
#print("天氣描述:"+new_taipei2[73:77])
new_taipei3=str(data[34:37])
new_taipei3=re.sub("'':","",new_taipei3)
print("明日晚上:"+new_taipei3[4:15]+" "+new_taipei3[19]+" "+new_taipei3[24:35])
print("溫度:"+new_taipei3[41:43]+"℃"+" "+new_taipei3[19]+" "+new_taipei3[45:47]+"℃")
print("降雨機率:"+new_taipei3[61:63]+"%")
#print("天氣概況:"+new_taipei3[79:81])
#print("天氣描述:"+new_taipei3[73:77])
print("..........................................桃園市.........................................................")
taoyuan1=str(data[38:41])
taoyuan1=re.sub("'':","",taoyuan1)
print("今晚-明晨:"+taoyuan1[4:15]+" "+taoyuan1[19]+" "+taoyuan1[24:35])
print("溫度:"+taoyuan1[41:43]+"℃"+" "+taoyuan1[19]+" "+taoyuan1[45:47]+"℃")
print("降雨機率:"+taoyuan1[61:63]+"%")
#print("天氣概況:"+taoyuan1[79:81])
#print("天氣描述:"+taoyuan1[73:77])
taoyuan2=str(data[41:44])
taoyuan2=re.sub("'':","",taoyuan2)
print("明日白天:"+taoyuan2[4:15]+" "+taoyuan2[19]+" "+taoyuan2[24:35])
print("溫度:"+taoyuan2[41:43]+"℃"+" "+taoyuan2[19]+" "+taoyuan2[45:47]+"℃")
print("降雨機率:"+taoyuan2[61:63]+"%")
#print("天氣概況:"+taoyuan2[79:81])
#print("天氣描述:"+taoyuan2[73:77])
taoyuan3=str(data[44:47])
taoyuan3=re.sub("'':","",taoyuan3)
print("明日晚上:"+taoyuan3[4:15]+" "+taoyuan3[19]+" "+taoyuan3[24:35])
print("溫度:"+taoyuan3[41:43]+"℃"+" "+taoyuan3[19]+" "+taoyuan3[45:47]+"℃")
print("降雨機率:"+taoyuan3[61:63]+"%")
#print("天氣概況:"+taoyuan3[79:81])
#print("天氣描述:"+taoyuan3[73:77])
print("..........................................新竹市.........................................................")
Hsinchu1=str(data[48:51])
Hsinchu1=re.sub("'':","",taoyuan1)
print("今晚-明晨:"+Hsinchu1[4:15]+" "+Hsinchu1[19]+" "+Hsinchu1[24:35])
print("溫度:"+Hsinchu1[41:43]+"℃"+" "+Hsinchu1[19]+" "+Hsinchu1[45:47]+"℃")
print("降雨機率:"+Hsinchu1[61:63]+"%")
#print("天氣概況:"+Hsinchu1[79:81])
#print("天氣描述:"+Hsinchu1[73:77])
Hsinchu2=str(data[51:54])
Hsinchu2=re.sub("'':","",Hsinchu2)
print("明日白天:"+Hsinchu2[4:15]+" "+Hsinchu2[19]+" "+Hsinchu2[24:35])
print("溫度:"+Hsinchu2[41:43]+"℃"+" "+Hsinchu2[19]+" "+Hsinchu2[45:47]+"℃")
print("降雨機率:"+Hsinchu2[61:63]+"%")
#print("天氣概況:"+Hsinchu2[79:81])
#print("天氣描述:"+Hsinchu2[73:77])
Hsinchu3=str(data[54:57])
Hsinchu3=re.sub("'':","",Hsinchu3)
print("明日晚上:"+Hsinchu3[4:15]+" "+Hsinchu3[19]+" "+Hsinchu3[24:35])
print("溫度:"+Hsinchu3[41:43]+"℃"+" "+Hsinchu3[19]+" "+Hsinchu3[45:47]+"℃")
print("降雨機率:"+Hsinchu3[61:63]+"%")
#print("天氣概況:"+Hsinchu3[79:81])
#print("天氣描述:"+Hsinchu3[73:77])
print("..........................................新竹縣.........................................................")
HsinchuS1=str(data[58:61])
HsinchuS1=re.sub("'':","",taoyuan1)
print("今晚-明晨:"+HsinchuS1[4:15]+" "+HsinchuS1[19]+" "+HsinchuS1[24:35])
print("溫度:"+HsinchuS1[41:43]+"℃"+" "+HsinchuS1[19]+" "+HsinchuS1[45:47]+"℃")
print("降雨機率:"+HsinchuS1[61:63]+"%")
#print("天氣概況:"+HsinchuS1[79:81])
#print("天氣描述:"+HsinchuS1[73:77])
HsinchuS2=str(data[61:64])
HsinchuS2=re.sub("'':","",HsinchuS2)
print("明日白天:"+HsinchuS2[4:15]+" "+HsinchuS2[19]+" "+HsinchuS2[24:35])
print("溫度:"+HsinchuS2[41:43]+"℃"+" "+HsinchuS2[19]+" "+HsinchuS2[45:47]+"℃")
print("降雨機率:"+HsinchuS2[61:63]+"%")
#print("天氣概況:"+HsinchuS2[79:81])
#print("天氣描述:"+HsinchuS2[73:77])
HsinchuS3=str(data[64:67])
HsinchuS3=re.sub("'':","",HsinchuS3)
print("明日晚上:"+HsinchuS3[4:15]+" "+HsinchuS3[19]+" "+HsinchuS3[24:35])
print("溫度:"+HsinchuS3[41:43]+"℃"+" "+HsinchuS3[19]+" "+HsinchuS3[45:47]+"℃")
print("降雨機率:"+HsinchuS3[61:63]+"%")
#print("天氣概況:"+HsinchuS3[79:81])
#print("天氣描述:"+HsinchuS3[73:77])
print("..........................................苗栗縣.........................................................")
miaoli1=str(data[68:71])
miaoli1=re.sub("'':","",miaoli1)
print("今晚-明晨:"+miaoli1[4:15]+" "+miaoli1[19]+" "+miaoli1[24:35])
print("溫度:"+miaoli1[41:43]+"℃"+" "+miaoli1[19]+" "+miaoli1[45:47]+"℃")
print("降雨機率:"+miaoli1[61:63]+"%")
#print("天氣概況:"+miaoli1[79:81])
#print("天氣描述:"+miaoli1[73:77])
miaoli2=str(data[71:74])
miaoli2=re.sub("'':","",miaoli2)
print("明日白天:"+miaoli2[4:15]+" "+miaoli2[19]+" "+miaoli2[24:35])
print("溫度:"+miaoli2[41:43]+"℃"+" "+miaoli2[19]+" "+miaoli2[45:47]+"℃")
print("降雨機率:"+miaoli2[61:63]+"%")
#print("天氣概況:"+miaoli2[79:81])
#print("天氣描述:"+miaoli2[73:77])
miaoli3=str(data[74:77])
miaoli3=re.sub("'':","",miaoli3)
print("明日晚上:"+miaoli3[4:15]+" "+miaoli3[19]+" "+miaoli3[24:35])
print("溫度:"+miaoli3[41:43]+"℃"+" "+miaoli3[19]+" "+miaoli3[45:47]+"℃")
print("降雨機率:"+miaoli3[61:63]+"%")
#print("天氣概況:"+miaoli3[79:81])
#print("天氣描述:"+miaoli3[73:77])
print("..........................................台中市.........................................................")
taichung1=str(data[78:81])
taichung1=re.sub("'':","",taichung1)
print("今晚-明晨:"+taichung1[4:15]+" "+taichung1[19]+" "+taichung1[24:35])
print("溫度:"+taichung1[41:43]+"℃"+" "+taichung1[19]+" "+taichung1[45:47]+"℃")
print("降雨機率:"+taichung1[61:63]+"%")
#print("天氣概況:"+taichung1[79:81])
#print("天氣描述:"+taichung1[73:77])
taichung2=str(data[81:84])
taichung2=re.sub("'':","",taichung2)
print("明日白天:"+taichung2[4:15]+" "+taichung2[19]+" "+taichung2[24:35])
print("溫度:"+taichung2[41:43]+"℃"+" "+taichung2[19]+" "+taichung2[45:47]+"℃")
print("降雨機率:"+taichung2[61:63]+"%")
#print("天氣概況:"+taichung2[79:81])
#print("天氣描述:"+taichung2[73:77])
taichung3=str(data[84:87])
taichung3=re.sub("'':","",taichung3)
print("明日晚上:"+taichung3[4:15]+" "+taichung3[19]+" "+taichung3[24:35])
print("溫度:"+taichung3[41:43]+"℃"+" "+taichung3[19]+" "+taichung3[45:47]+"℃")
print("降雨機率:"+taichung3[61:63]+"%")
#print("天氣概況:"+taichung3[79:81])
#print("天氣描述:"+taichung3[73:77])
print("..........................................彰化縣.........................................................")
Changhua1=str(data[88:91])
Changhua1=re.sub("'':","",Changhua1)
print("今晚-明晨:"+Changhua1[4:15]+" "+Changhua1[19]+" "+Changhua1[24:35])
print("溫度:"+Changhua1[41:43]+"℃"+" "+Changhua1[19]+" "+Changhua1[45:47]+"℃")
print("降雨機率:"+Changhua1[61:63]+"%")
#print("天氣概況:"+Changhua1[79:81])
#print("天氣描述:"+Changhua1[73:77])
Changhua2=str(data[91:94])
Changhua2=re.sub("'':","",Changhua2)
print("明日白天:"+Changhua2[4:15]+" "+Changhua2[19]+" "+Changhua2[24:35])
print("溫度:"+Changhua2[41:43]+"℃"+" "+Changhua2[19]+" "+Changhua2[45:47]+"℃")
print("降雨機率:"+Changhua2[61:63]+"%")
#print("天氣概況:"+Changhua2[79:81])
#print("天氣描述:"+Changhua2[73:77])
Changhua3=str(data[94:97])
Changhua3=re.sub("'':","",Changhua3)
print("明日晚上:"+Changhua3[4:15]+" "+Changhua3[19]+" "+Changhua3[24:35])
print("溫度:"+Changhua3[41:43]+"℃"+" "+Changhua3[19]+" "+Changhua3[45:47]+"℃")
print("降雨機率:"+Changhua3[61:63]+"%")
#print("天氣概況:"+Changhua3[79:81])
#print("天氣描述:"+Changhua3[73:77])
print("..........................................南投縣.........................................................")
Nantou1=str(data[98:101])
Nantou1=re.sub("'':","",Nantou1)
print("今晚-明晨:"+Nantou1[4:15]+" "+Nantou1[19]+" "+Nantou1[24:35])
print("溫度:"+Nantou1[41:43]+"℃"+" "+Nantou1[19]+" "+Nantou1[45:47]+"℃")
print("降雨機率:"+Nantou1[61:63]+"%")
#print("天氣概況:"+Nantou1[79:81])
#print("天氣描述:"+Nantou1[73:77])
Nantou2=str(data[101:104])
Nantou2=re.sub("'':","",Nantou2)
print("明日白天:"+Nantou2[4:15]+" "+Nantou2[19]+" "+Nantou2[24:35])
print("溫度:"+Nantou2[41:43]+"℃"+" "+Nantou2[19]+" "+Nantou2[45:47]+"℃")
print("降雨機率:"+Nantou2[61:63]+"%")
#print("天氣概況:"+miaoli2[79:81])
#print("天氣描述:"+miaoli2[73:77])
Nantou3=str(data[104:107])
Nantou3=re.sub("'':","",Nantou3)
print("明日晚上:"+Nantou3[4:15]+" "+Nantou3[19]+" "+Nantou3[24:35])
print("溫度:"+Nantou3[41:43]+"℃"+" "+Nantou3[19]+" "+Nantou3[45:47]+"℃")
print("降雨機率:"+Nantou3[61:63]+"%")
#print("天氣概況:"+Nantou3[79:81])
#print("天氣描述:"+Nantou3[73:77])
print("..........................................雲林縣.........................................................")
Yunlin1=str(data[108:111])
Yunlin1=re.sub("'':","",Yunlin1)
print("今晚-明晨:"+Yunlin1[4:15]+" "+Yunlin1[19]+" "+Yunlin1[24:35])
print("溫度:"+Yunlin1[41:43]+"℃"+" "+Yunlin1[19]+" "+Yunlin1[45:47]+"℃")
print("降雨機率:"+Yunlin1[61:63]+"%")
#print("天氣概況:"+Yunlin1[79:81])
#print("天氣描述:"+Yunlin1[73:77])
Yunlin2=str(data[111:114])
Yunlin2=re.sub("'':","",Yunlin2)
print("明日白天:"+Yunlin2[4:15]+" "+Yunlin2[19]+" "+Yunlin2[24:35])
print("溫度:"+Yunlin2[41:43]+"℃"+" "+Yunlin2[19]+" "+Yunlin2[45:47]+"℃")
print("降雨機率:"+Yunlin2[61:63]+"%")
#print("天氣概況:"+Yunlin2[79:81])
#print("天氣描述:"+Yunlin2[73:77])
Yunlin3=str(data[114:117])
Yunlin3=re.sub("'':","",Yunlin3)
print("明日晚上:"+Yunlin3[4:15]+" "+Yunlin3[19]+" "+Yunlin3[24:35])
print("溫度:"+Yunlin3[41:43]+"℃"+" "+Yunlin3[19]+" "+Yunlin3[45:47]+"℃")
print("降雨機率:"+Yunlin3[61:63]+"%")
#print("天氣概況:"+Yunlin3[79:81])
#print("天氣描述:"+Yunlin3[73:77])
print("..........................................嘉義市.........................................................")
Chiayi1=str(data[118:121])
Chiayi1=re.sub("'':","",Chiayi1)
print("今晚-明晨:"+Chiayi1[4:15]+" "+Chiayi1[19]+" "+Chiayi1[24:35])
print("溫度:"+Chiayi1[41:43]+"℃"+" "+Chiayi1[19]+" "+Chiayi1[45:47]+"℃")
print("降雨機率:"+Chiayi1[61:63]+"%")
#print("天氣概況:"+Chiayi1[79:81])
#print("天氣描述:"+Chiayi1[73:77])
Chiayi2=str(data[121:124])
Chiayi2=re.sub("'':","",Chiayi2)
print("明日白天:"+Chiayi2[4:15]+" "+Chiayi2[19]+" "+Chiayi2[24:35])
print("溫度:"+Chiayi2[41:43]+"℃"+" "+Chiayi2[19]+" "+Chiayi2[45:47]+"℃")
print("降雨機率:"+Chiayi2[61:63]+"%")
#print("天氣概況:"+Chiayi2[79:81])
#print("天氣描述:"+Chiayi2[73:77])
Chiayi3=str(data[124:127])
Chiayi3=re.sub("'':","",Chiayi3)
print("明日晚上:"+Chiayi3[4:15]+" "+Chiayi3[19]+" "+Chiayi3[24:35])
print("溫度:"+Chiayi3[41:43]+"℃"+" "+Chiayi3[19]+" "+Chiayi3[45:47]+"℃")
print("降雨機率:"+Chiayi3[61:63]+"%")
#print("天氣概況:"+Chiayi3[79:81])
#print("天氣描述:"+Chiayi3[73:77])
print("..........................................嘉義縣.........................................................")
ChiayiS1=str(data[128:131])
ChiayiS1=re.sub("'':","",ChiayiS1)
print("今晚-明晨:"+ChiayiS1[4:15]+" "+ChiayiS1[19]+" "+ChiayiS1[24:35])
print("溫度:"+ChiayiS1[41:43]+"℃"+" "+ChiayiS1[19]+" "+ChiayiS1[45:47]+"℃")
print("降雨機率:"+ChiayiS1[61:63]+"%")
#print("天氣概況:"+ChiayiS1[79:81])
#print("天氣描述:"+ChiayiS1[73:77])
ChiayiS2=str(data[131:134])
ChiayiS2=re.sub("'':","",ChiayiS2)
print("明日白天:"+ChiayiS2[4:15]+" "+ChiayiS2[19]+" "+ChiayiS2[24:35])
print("溫度:"+ChiayiS2[41:43]+"℃"+" "+ChiayiS2[19]+" "+ChiayiS2[45:47]+"℃")
print("降雨機率:"+ChiayiS2[61:63]+"%")
#print("天氣概況:"+ChiayiS2[79:81])
#print("天氣描述:"+ChiayiS2[73:77])
ChiayiS3=str(data[134:137])
ChiayiS3=re.sub("'':","",ChiayiS3)
print("明日晚上:"+ChiayiS3[4:15]+" "+ChiayiS3[19]+" "+ChiayiS3[24:35])
print("溫度:"+ChiayiS3[41:43]+"℃"+" "+ChiayiS3[19]+" "+ChiayiS3[45:47]+"℃")
print("降雨機率:"+ChiayiS3[61:63]+"%")
#print("天氣概況:"+ChiayiS3[79:81])
#print("天氣描述:"+ChiayiS3[73:77])
print("..........................................台南市.........................................................")
Tainan1=str(data[138:141])
Tainan1=re.sub("'':","",Tainan1)
print("今晚-明晨:"+Tainan1[4:15]+" "+Tainan1[19]+" "+Tainan1[24:35])
print("溫度:"+Tainan1[41:43]+"℃"+" "+Tainan1[19]+" "+Tainan1[45:47]+"℃")
print("降雨機率:"+Tainan1[61:63]+"%")
#print("天氣概況:"+Tainan1[79:81])
#print("天氣描述:"+Tainan1[73:77])
Tainan2=str(data[141:144])
Tainan2=re.sub("'':","",Tainan2)
print("明日白天:"+Tainan2[4:15]+" "+Tainan2[19]+" "+Tainan2[24:35])
print("溫度:"+Tainan2[41:43]+"℃"+" "+Tainan2[19]+" "+Tainan2[45:47]+"℃")
print("降雨機率:"+Tainan2[61:63]+"%")
#print("天氣概況:"+Tainan2[79:81])
#print("天氣描述:"+Tainan2[73:77])
Tainan3=str(data[144:147])
Tainan3=re.sub("'':","",Tainan3)
print("明日晚上:"+Tainan3[4:15]+" "+Tainan3[19]+" "+Tainan3[24:35])
print("溫度:"+Tainan3[41:43]+"℃"+" "+Tainan3[19]+" "+Tainan3[45:47]+"℃")
print("降雨機率:"+Tainan3[61:63]+"%")
#print("天氣概況:"+Tainan3[79:81])
#print("天氣描述:"+Tainan3[73:77])
print("..........................................高雄市.........................................................")
Kaohsiung1=str(data[148:151])
Kaohsiung1=re.sub("'':","",Kaohsiung1)
print("今晚-明晨:"+Kaohsiung1[4:15]+" "+Kaohsiung1[19]+" "+Kaohsiung1[24:35])
print("溫度:"+Kaohsiung1[41:43]+"℃"+" "+Kaohsiung1[19]+" "+Kaohsiung1[45:47]+"℃")
print("降雨機率:"+Kaohsiung1[61:63]+"%")
#print("天氣概況:"+Kaohsiung1[79:81])
#print("天氣描述:"+Kaohsiung1[73:77])
Kaohsiung2=str(data[151:154])
Kaohsiung2=re.sub("'':","",Kaohsiung2)
print("明日白天:"+Kaohsiung2[4:15]+" "+Kaohsiung2[19]+" "+Kaohsiung2[24:35])
print("溫度:"+Kaohsiung2[41:43]+"℃"+" "+Kaohsiung2[19]+" "+Kaohsiung2[45:47]+"℃")
print("降雨機率:"+Kaohsiung2[61:63]+"%")
#print("天氣概況:"+Kaohsiung2[79:81])
#print("天氣描述:"+Kaohsiung2[73:77])
Kaohsiung3=str(data[154:157])
Kaohsiung3=re.sub("'':","",Kaohsiung3)
print("明日晚上:"+Kaohsiung3[4:15]+" "+Kaohsiung3[19]+" "+Kaohsiung3[24:35])
print("溫度:"+Kaohsiung3[41:43]+"℃"+" "+Kaohsiung3[19]+" "+Kaohsiung3[45:47]+"℃")
print("降雨機率:"+Kaohsiung3[61:63]+"%")
#print("天氣概況:"+Kaohsiung3[79:81])
#print("天氣描述:"+Kaohsiung3[73:77])
print("..........................................屏東縣.........................................................")
Pingtung1=str(data[158:161])
Pingtung1=re.sub("'':","",Pingtung1)
print("今晚-明晨:"+Pingtung1[4:15]+" "+Pingtung1[19]+" "+Pingtung1[24:35])
print("溫度:"+Pingtung1[41:43]+"℃"+" "+Pingtung1[19]+" "+Pingtung1[45:47]+"℃")
print("降雨機率:"+Pingtung1[61:63]+"%")
#print("天氣概況:"+Pingtung1[79:81])
#print("天氣描述:"+Pingtung1[73:77])
Pingtung2=str(data[161:164])
Pingtung2=re.sub("'':","",Pingtung2)
print("明日白天:"+Pingtung2[4:15]+" "+Pingtung2[19]+" "+Pingtung2[24:35])
print("溫度:"+Pingtung2[41:43]+"℃"+" "+Pingtung2[19]+" "+Pingtung2[45:47]+"℃")
print("降雨機率:"+Pingtung2[61:63]+"%")
#print("天氣概況:"+Pingtung2[79:81])
#print("天氣描述:"+Pingtung2[73:77])
Pingtung3=str(data[164:167])
Pingtung3=re.sub("'':","",Pingtung3)
print("明日晚上:"+Pingtung3[4:15]+" "+Pingtung3[19]+" "+Pingtung3[24:35])
print("溫度:"+Pingtung3[41:43]+"℃"+" "+Pingtung3[19]+" "+Pingtung3[45:47]+"℃")
print("降雨機率:"+Pingtung3[61:63]+"%")
#print("天氣概況:"+Pingtung3[79:81])
#print("天氣描述:"+Pingtung3[73:77])
print("..........................................宜蘭縣.........................................................")
Yilan1=str(data[168:171])
Yilan1=re.sub("'':","",Yilan1)
print("今晚-明晨:"+Yilan1[4:15]+" "+Yilan1[19]+" "+Yilan1[24:35])
print("溫度:"+Yilan1[41:43]+"℃"+" "+Yilan1[19]+" "+Yilan1[45:47]+"℃")
print("降雨機率:"+Yilan1[61:63]+"%")
#print("天氣概況:"+Yilan1[79:81])
#print("天氣描述:"+Yilan1[73:77])
Yilan2=str(data[171:174])
Yilan2=re.sub("'':","",Yilan2)
print("明日白天:"+Yilan2[4:15]+" "+Yilan2[19]+" "+Yilan2[24:35])
print("溫度:"+Yilan2[41:43]+"℃"+" "+Yilan2[19]+" "+Yilan2[45:47]+"℃")
print("降雨機率:"+Yilan2[61:63]+"%")
#print("天氣概況:"+Yilan2[79:81])
#print("天氣描述:"+Yilan2[73:77])
Yilan3=str(data[174:177])
Yilan3=re.sub("'':","",Yilan3)
print("明日晚上:"+Yilan3[4:15]+" "+Yilan3[19]+" "+Yilan3[24:35])
print("溫度:"+Yilan3[41:43]+"℃"+" "+Yilan3[19]+" "+Yilan3[45:47]+"℃")
print("降雨機率:"+Yilan3[61:63]+"%")
#print("天氣概況:"+miaoli3[79:81])
#print("天氣描述:"+miaoli3[73:77])
print("..........................................花蓮縣.........................................................")
Hualien1=str(data[178:181])
Hualien1=re.sub("'':","",Hualie1)
print("今晚-明晨:"+Hualien1[4:15]+" "+Hualien1[19]+" "+Hualien1[24:35])
print("溫度:"+Hualien1[41:43]+"℃"+" "+Hualien1[19]+" "+Hualien1[45:47]+"℃")
print("降雨機率:"+Hualien1[61:63]+"%")
#print("天氣概況:"+Hualien1[79:81])
#print("天氣描述:"+Hualien1[73:77])
Hualien2=str(data[181:184])
Hualien2=re.sub("'':","",Hualien2)
print("明日白天:"+Hualien2[4:15]+" "+Hualien2[19]+" "+Hualien2[24:35])
print("溫度:"+Hualien2[41:43]+"℃"+" "+Hualien2[19]+" "+Hualien2[45:47]+"℃")
print("降雨機率:"+Hualien2[61:63]+"%")
#print("天氣概況:"+Hualien2[79:81])
#print("天氣描述:"+Hualien2[73:77])
Hualien3=str(data[184:187])
Hualien3=re.sub("'':","",Hualien3)
print("明日晚上:"+Hualien3[4:15]+" "+Hualien3[19]+" "+Hualien3[24:35])
print("溫度:"+Hualien3[41:43]+"℃"+" "+Hualien3[19]+" "+Hualien3[45:47]+"℃")
print("降雨機率:"+Hualien3[61:63]+"%")
#print("天氣概況:"+Hualien3[79:81])
#print("天氣描述:"+Hualien3[73:77])
print("..........................................台東縣.........................................................")
Taitung1=str(data[188:191])
Taitung1=re.sub("'':","",Taitung1)
print("今晚-明晨:"+Taitung1[4:15]+" "+Taitung1[19]+" "+Taitung1[24:35])
print("溫度:"+Taitung1[41:43]+"℃"+" "+Taitung1[19]+" "+Taitung1[45:47]+"℃")
print("降雨機率:"+Taitung1[61:63]+"%")
#print("天氣概況:"+Taitung1[79:81])
#print("天氣描述:"+Taitung1[73:77])
Taitung2=str(data[191:194])
Taitung2=re.sub("'':","",Taitung2)
print("明日白天:"+Taitung2[4:15]+" "+Taitung2[19]+" "+Taitung2[24:35])
print("溫度:"+Taitung2[41:43]+"℃"+" "+Taitung2[19]+" "+Taitung2[45:47]+"℃")
print("降雨機率:"+Taitung2[61:63]+"%")
#print("天氣概況:"+Taitung2[79:81])
#print("天氣描述:"+Taitung2[73:77])
Taitung3=str(data[194:197])
Taitung3=re.sub("'':","",Taitung3)
print("明日晚上:"+Taitung3[4:15]+" "+Taitung3[19]+" "+Taitung3[24:35])
print("溫度:"+Taitung3[41:43]+"℃"+" "+Taitung3[19]+" "+Taitung3[45:47]+"℃")
print("降雨機率:"+Taitung3[61:63]+"%")
#print("天氣概況:"+Taitung3[79:81])
#print("天氣描述:"+Taitung3[73:77])
print("..........................................澎湖縣.........................................................")
Penghu1=str(data[198:201])
Penghu1=re.sub("'':","",Penghu1)
print("今晚-明晨:"+Penghu1[4:15]+" "+Penghu1[19]+" "+Penghu1[24:35])
print("溫度:"+Penghu1[41:43]+"℃"+" "+Penghu1[19]+" "+Penghu1[45:47]+"℃")
print("降雨機率:"+Penghu1[61:63]+"%")
#print("天氣概況:"+Penghu1[79:81])
#print("天氣描述:"+Penghu1[73:77])
Penghu2=str(data[201:204])
Penghu2=re.sub("'':","",Penghu2)
print("明日白天:"+Penghu2[4:15]+" "+Penghu2[19]+" "+Penghu2[24:35])
print("溫度:"+Penghu2[41:43]+"℃"+" "+Penghu2[19]+" "+Penghu2[45:47]+"℃")
print("降雨機率:"+Penghu2[61:63]+"%")
#print("天氣概況:"+Penghu2[79:81])
#print("天氣描述:"+Penghu2[73:77])
Penghu3=str(data[204:207])
Penghu3=re.sub("'':","",Penghu3)
print("明日晚上:"+Penghu3[4:15]+" "+Penghu3[19]+" "+Penghu3[24:35])
print("溫度:"+Penghu3[41:43]+"℃"+" "+Penghu3[19]+" "+Penghu3[45:47]+"℃")
print("降雨機率:"+Penghu3[61:63]+"%")
#print("天氣概況:"+Penghu3[79:81])
#print("天氣描述:"+Penghu3[73:77])
print("..........................................金門縣.........................................................")
Jinmen1=str(data[208:211])
Jinmen1=re.sub("'':","",Jinmen1)
print("今晚-明晨:"+Jinmen1[4:15]+" "+Jinmen1[19]+" "+Jinmen1[24:35])
print("溫度:"+Jinmen1[41:43]+"℃"+" "+Jinmen1[19]+" "+Jinmen1[45:47]+"℃")
print("降雨機率:"+Jinmen1[61:63]+"%")
#print("天氣概況:"+Jinmen1[79:81])
#print("天氣描述:"+Jinmen1[73:77])
Jinmen2=str(data[211:214])
Jinmen2=re.sub("'':","",Jinmen2)
print("明日白天:"+Jinmen2[4:15]+" "+Jinmen2[19]+" "+Jinmen2[24:35])
print("溫度:"+Jinmen2[41:43]+"℃"+" "+Jinmen2[19]+" "+Jinmen2[45:47]+"℃")
print("降雨機率:"+Jinmen2[61:63]+"%")
#print("天氣概況:"+Jinmen2[79:81])
#print("天氣描述:"+Jinmen2[73:77])
Jinmen3=str(data[214:217])
Jinmen3=re.sub("'':","",Jinmen3)
print("明日晚上:"+Jinmen3[4:15]+" "+Jinmen3[19]+" "+Jinmen3[24:35])
print("溫度:"+Jinmen3[41:43]+"℃"+" "+Jinmen3[19]+" "+Jinmen3[45:47]+"℃")
print("降雨機率:"+Jinmen3[61:63]+"%")
#print("天氣概況:"+Jinmen3[79:81])
#print("天氣描述:"+Jinmen3[73:77])
print("..........................................連江縣.........................................................")
Lianjiang1=str(data[218:221])
Lianjiang1=re.sub("'':","",Lianjiang1)
print("今晚-明晨:"+Lianjiang1[4:15]+" "+Lianjiang1[19]+" "+Lianjiang1[24:35])
print("溫度:"+Lianjiang1[41:43]+"℃"+" "+Lianjiang1[19]+" "+Lianjiang1[45:47]+"℃")
print("降雨機率:"+Lianjiang1[61:63]+"%")
#print("天氣概況:"+Lianjiang1[79:81])
#print("天氣描述:"+Lianjiang1[73:77])
Lianjiang2=str(data[221:224])
Lianjiang2=re.sub("'':","",Lianjiang2)
print("明日白天:"+Lianjiang2[4:15]+" "+Lianjiang2[19]+" "+Lianjiang2[24:35])
print("溫度:"+Lianjiang2[41:43]+"℃"+" "+Lianjiang2[19]+" "+Lianjiang2[45:47]+"℃")
print("降雨機率:"+Lianjiang2[61:63]+"%")
#print("天氣概況:"+Lianjiang2[79:81])
#print("天氣描述:"+Lianjiang2[73:77])
Lianjiang3=str(data[224:227])
Lianjiang3=re.sub("'':","",Lianjiang3)
print("明日晚上:"+Lianjiang3[4:15]+" "+Lianjiang3[19]+" "+Lianjiang3[24:35])
print("溫度:"+Lianjiang3[41:43]+"℃"+" "+Lianjiang3[19]+" "+Lianjiang3[45:47]+"℃")
print("降雨機率:"+Lianjiang3[61:63]+"%")
#print("天氣概況:"+Lianjiang3[79:81])
#print("天氣描述:"+Lianjiang3[73:77])
'''