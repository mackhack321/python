# VPN is required
import pyowm as owm
import datetime as dt
from dateutil import tz
key = "b4ba2341c0c5961d7f4bc5a6c5d1c663"
api = owm.OWM(key)
from_zone = tz.gettz("UTC")
to_zone = tz.gettz("America/Chicago")

def getID(location):
    registry = api.city_id_registry()
    ids = registry.ids_for(location)
    count = 1
    for ID in ids:
        print(f"{count}: {ID}")
        count += 1
    idIndex = int(input("ID >>> "))
    usrid = ids[idIndex]
    return usrid

def getWeather(location, usrid):
    if location != None:
        obs = api.weather_at_place(location)
    elif usrid != None:
        obs = api.weather_at_id(usrid)
    w = obs.get_weather()
    return w

def getThreeHourForecast(location):
    fc = api.three_hours_forecast(location)
    f = fc.get_forecast()
    fclist = f.get_weathers()
    return fclist

def timeToCentral(rawtime):
    time = dt.datetime.strptime(str(rawtime), '%Y-%m-%d %H:%M:%S+%f:%s')
    time = time.replace(tzinfo=from_zone)
    local = time.astimezone(to_zone)
    return local

location = input("Location >>> ")
w = getWeather(location = location, usrid = None)
hourlyls = getThreeHourForecast(location)
for item in hourlyls:
    rawtime = item.get_reference_time("date")
    local = timeToCentral(rawtime)
    print(f"{local} :: {item.get_status()}")
