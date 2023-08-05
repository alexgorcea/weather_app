import datetime
from dateutil import relativedelta

from django.shortcuts import render
import requests

api_key = '8d96729b0eb079b8bb05b7bc8c6d3be1'

def index(request):
    if request.method != 'POST':
        return render(request,'weather/index.html')
    elif request.method == 'POST' and request.POST['city']:
        city = request.POST.get('city')
        current_weather = get_current_weather(city,api_key)
        context = {
            'city':city,
            'current_weather':current_weather,
        }
        return render(request, 'weather/index.html', context)
    else:
        return render(request,'weather/index.html')    

def forecast(request):
    city_name = request.POST.get('city_name')
    forecast = get_forecast(city_name, api_key)
    dates = get_dates(city_name, api_key)
    forecast_data = zip(dates,forecast)
    context = {
        'forecast_data':forecast_data,
        'city_name':city_name
    }
    return render(request,'weather/forecast.html', context)
    
def get_current_weather(city,api_key):
    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response1 = requests.get(current_weather_url).json()

    lat = response1['coord']['lat']
    lon = response1['coord']['lon']

    return {
        'country':response1['sys']['country'],
        'temp':round(response1['main']['temp']),
        'max':round(response1['main']['temp_max']),
        'min':round(response1['main']['temp_min']),
        'pressure':response1['main']['pressure'],
        'humidity':response1['main']['humidity'],
        'description':response1['weather'][0]['description'],
        'wind_speed':response1['wind']['speed'],
        'icon':response1['weather'][0]['icon'],
        'lat':lat,
        'lon':lon
    }
    

def get_forecast(city,api_key):
    data = get_current_weather(city,api_key)
    lat, lon = data['lat'], data['lon']
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"
    response2 = requests.get(forecast_url).json()

    forecasts = response2['list']

    today_datetime = datetime.datetime.strptime(forecasts[0]['dt_txt'],'%Y-%m-%d %H:%M:%S')
    today_date = today_datetime.date()

    day1, day2, day3, day4, day5 = [],[],[],[],[]
    for forecast in forecasts :
        date_time = datetime.datetime.strptime(forecast['dt_txt'],'%Y-%m-%d %H:%M:%S')
        info= {
            'temp' : round(forecast['main']['temp']),
            'weather_description' : forecast['weather'][0]['description'],
            'wind_speed' : forecast['wind']['speed'],
            'precipitation_probability' : forecast['pop']*100,
            'date' : date_time.date(),
            'time':date_time.time(),
            'icon': forecast['weather'][0]['icon']
        }

        diff = relativedelta.relativedelta(info['date'], today_date)

        if diff.days == 0:
            day1.append(info)
        elif diff.days == 1:
            day2.append(info)
        elif diff.days == 2:
            day3.append(info)
        elif diff.days == 3:
            day4.append(info)
        elif diff.days == 4:
            day5.append(info)

    return [day1,day2,day3,day4,day5]

def get_dates(city,api_key):
    data = get_current_weather(city,api_key)
    lat, lon = data['lat'], data['lon']
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"
    response2 = requests.get(forecast_url).json()

    forecasts = response2['list']

    today_datetime = datetime.datetime.strptime(forecasts[0]['dt_txt'],'%Y-%m-%d %H:%M:%S')
    today_date = today_datetime.date()

    day1_date = today_date
    day2_date = today_date + datetime.timedelta(days=1)
    day3_date = today_date + datetime.timedelta(days=2)
    day4_date = today_date + datetime.timedelta(days=3)
    day5_date = today_date + datetime.timedelta(days=4)

    return [day1_date, day2_date, day3_date, day4_date, day5_date]
    
