#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import requests
#from requests.models import Response

city_name = 'Нарьян-Мар'

def pogoda(city_name):
    api_key = 'f58506a15948f751314a3023408b4aa4'
    ap = 'https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+api_key+'&lang=ru'
    response = requests.get(ap)
    data = response.json()
    city = data['name']
    temp = str(round(data['main']['temp']-273.15, 2))+'℃'
    weather = str(data['wind']['speed'])+' м/с'
    humidity = str(data['main']['humidity'])+'%'
    return city, temp, weather, humidity
print(pogoda(city_name))