#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import telebot
import requests
import pandas as pd
#from requests.models import Response

#city_name = 'Нарьян-Мар'
token='1951761639:AAE-ewTNw8w6uyaHY4UP0wVx7hxjC0kbelk'
bot = telebot.TeleBot(token)

def pogoda(city_name):
    api_key = 'f58506a15948f751314a3023408b4aa4'
    ap = 'https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+api_key+'&lang=ru'
    response = requests.get(ap)
    data = response.json()
    city = data['name']
    temp = str(round(data['main']['temp']-273.15, 1))+'℃'
    weather = str(data['wind']['speed'])+' м/с'
    humidity = str(data['main']['humidity'])+'%'
    s= [city, temp, weather, humidity]
    return s


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, str(pd.DataFrame(pogoda(message.text), index=['Город', 'Температура', 'Скорость ветра', 'Влажность'])))
bot.polling(none_stop=True, interval=0)