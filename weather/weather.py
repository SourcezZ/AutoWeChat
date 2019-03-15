import requests
import json
import re
from weather.city import city_json


def getWeather(city):
    href = 'http://www.weather.com.cn/data/sk/{}.html'.format(city_json.get(city))

    res = requests.get(href)
    res.encoding = 'utf-8'
    content = json.loads(res.text)
    weatherinfo = content.get('weatherinfo')
    city_str = weatherinfo.get('city')
    temp = weatherinfo.get('temp')
    wind = weatherinfo.get('WD')
    wind_level = weatherinfo.get('WS')
    sd = weatherinfo.get('SD')
    result = '城市 ： {}\n温度 ： {}\n风向 ： {}\n风力 ： {}\n湿度 ： {}'.format(city_str, temp, wind, wind_level, sd)
    return result




