#! python3
# pobieranie pogody na przyszle dni

APPID_OWM = '2fdd431af203fd0780edd871909ddc8c'
APPID_PS = '0b9d3f67aba67a58458aa97c10eb9b55'

import json, requests, sys

#Podawanie lokalizacji z command line
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location=','.join(sys.argv[1:])



#Pobieranie lat i lon z positionstack
url_1 = 'http://api.positionstack.com/v1/forward?access_key=%s&query=%s' %(APPID_PS, location)
response_1 = requests.get(url_1)
response_1.raise_for_status()

# JSON danych z Position Stack
Position_data = json.loads(response_1.text)
p = Position_data["data"]
lat = (p[0]['latitude'])
lon = (p[0]['longitude'])



# Pobieranie JSON danych z OpenWeatherMap.org API
url ='https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric' % (lat,lon,
APPID_OWM)
response = requests.get(url)
response.raise_for_status()
print(url)
# raw JSON text
#print(response.text)


#Wczytanie JSON data do zmiennych Pythona
weatherData = json.loads(response.text)

#Print pogoda
w = weatherData['current']
print('Current weather in %s:' %(location))
print('Temperatura w ' + location +' wynosi ' + str(w['temp']))
print('Weather in '+ location + ': ' + w['weather'][0]['description'])
