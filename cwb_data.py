#!/usr/bin/env python
import urllib.request as ur
import json
from datetime import datetime, timedelta


class cwb_open_data:
  # CWB Open Data 
  def __init__(self, dataid, dataformat):
    self.dataid = dataid
    self.dataformat = dataformat 
    self.token="CWB-0F2C298D-3769-46D4-8A56-50A8B040EEC9"
    self.url="https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/{}?Authorization={}&format={}".format(self.dataid,self.token,self.dataformat)
    self.filename = self.dataid + '.' + self.dataformat.lower()
    
    print('access data ',self.filename)
    print('uri =' ,self.url)

  # download file
  def get_file(self):
    ur.urlretrieve(self.url,self.filename)
 
  # read json file 
  def read_json(self):
    urldata = ur.urlopen(self.url)
    self.data = json.loads(urldata.read())

  def get_info(self,location):
    self.city = self.data["cwbopendata"]["dataset"]["locations"]["locationsName"]
    for loc in self.data["cwbopendata"]["dataset"]["locations"]["location"]:
      if loc["locationName"] == location:
        self.lat = loc["lat"]
        self.lon = loc["lon"]
        self.info = loc["weatherElement"]
    for ivar in self.info:
      if ivar["description"] == "平均溫度":
        self.T = ivar["time"]
      if ivar["description"] == "平均相對濕度":
        self.RH = ivar["time"]
      if ivar["description"] == "最高體感溫度":
        self.MaxT = ivar["time"]
      if ivar["description"] == "最低體感溫度":
        self.MinT = ivar["time"]
      if ivar["description"] == "12小時降雨機率":
        self.PoP12h = ivar["time"]
      if ivar["description"] == "風向":
        self.WD = ivar["time"]
      if ivar["description"] == "最大風速":
        self.WS = ivar["time"]
      if ivar["description"] == "紫外獻指數":
        self.UVI = ivar["time"]
      if ivar["description"] == "天氣預報綜合描述":
        self.WeatherDescription = ivar["time"]
  def write_info(self,var):
    datetime_dict={'AM':'上午','PM':'下午', \
    'Mon':'星期一','Tue':'星期二','Wed':'星期三','Thu':'星期四','Fri':'星期五','Sat':'星期六','Sun':'星期日'}
    string = ''
    for ifcst in var:
      date = ifcst["startTime"].split('T')[0]
      time = ifcst["startTime"].split('T')[1].split('+')[0]

      dt = datetime(int(date[0:4]),int(date[5:7]),int(date[8:10]),int(time[0:2]),int(time[3:5]))
      dt = dt + timedelta(hours=8)
      time = dt.strftime("%Y-%m-%d %p%H:%M %a")
      time = time.replace(time[11:13],datetime_dict[time[11:13]]).replace(time[19:22],datetime_dict[time[19:22]])
      
      string = string + time + '\n' 

      weather = ifcst["elementValue"]['value'].split('。')
      weather = weather[0]+'，'+weather[1]+'。\n'+weather[2]+'，'+weather[3]+'。\n'+weather[4]+'，'+weather[5]+'。'  
      string = string + weather  + '\n\n'
    return string

if __name__ == '__main__':
  # get data
  dataid="F-D0047-007"
  dataformat='JSON'
  data = cwb_open_data(dataid,dataformat)
  
  # read json file
  data.read_json()
  location='平鎮區'

  data.get_info(location)
  string = data.write_info(data.WeatherDescription)
  print(string)
  #print(data.WeatherDescription)
# for ivar in data.info:
#   print(ivar["description"],ivar["elementName"])

  #print(data["cwbopendata"]["dataset"]["locations"]["location"][1]["locationName"])
  #print(cwbdata.info)



