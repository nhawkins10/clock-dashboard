#! /usr/bin

import urllib2
import json
#from papirus import PapirusComposite
#from papirus import PapirusTextPos

def requestWeather():
	weatherData = urllib2.urlopen("https://api.darksky.net/forecast/19c800f33bf2003db19cc4aae7db507a/39.035005,-94.354064?exclude=minutely,hourly,alerts,flags").read()
	
	weatherJsonData = json.loads(weatherData)
	
	processWeather(weatherJsonData)
	
def processWeather(data):
	currentTemp = int(round(data["currently"]["temperature"]))
	dailyHigh = int(round(data["daily"]["data"][0]["temperatureHigh"]))
	dailyLow = int(round(data["daily"]["data"][0]["temperatureLow"]))
	icon = data["daily"]["data"][0]["icon"]
	iconImage = ""
	
	if icon == "clear-day" or icon == "clear-night":
		iconImage = "clear"
	elif icon == "rain":
		iconImage = icon
	elif icon == "snow" or icon == "sleet" or icon == "hail":
		iconImage = "snow"
	elif icon == "wind":
		iconImage = icon
	elif icon == "fog":
		iconImage == icon
	elif icon == "cloudy":
		iconImage = "cloudy"
	elif icon == "partly-cloudy-day" or icon == "partly-cloudy-night":
		iconImage = "partly-cloudy"
	elif icon == "thunderstorm" or icon == "tornado":
		iconImage = "thunderstorm"
	else:
		iconImage = "clear"
	
	displayWeather(currentTemp, dailyHigh, dailyLow, iconImage)
	
def displayWeather(currentTemp, dailyHigh, dailyLow, iconImage):	
	# screen = PapirusComposite(False [, rotation=0])
	# screen.AddImage("/weatherIcons/" + iconImage + ".png", 175, 13, (39, 39),  Id="weatherIcon")
	# screen.AddText(str(currentTemp) + u"\u00b0", 220, 20, Id="currentTemp")
	# screen.AddText(str(dailyHigh) + u"\u00b0" + " | " + str(dailyLow) + u"\u00b0", 220, 57, Id="highLow")
	# screen.WriteAll()
	
	s = iconImage + " and " + str(currentTemp) + u"\u00b0" + "\n" + str(dailyHigh) + u"\u00b0" + " | " + str(dailyLow) + u"\u00b0"
	print s
	
	
	
	
def requestMaps():
	mapsData = urllib2.urlopen("https://maps.googleapis.com/maps/api/directions/json?destination=yrc+freight+overland+park,ks&origin=4625+s+eastland+center+dr+independence,mo+64055&key=AIzaSyDUVnqGbJmfTwy6t85qwTBqBcDOFkioxDk").read()
	
	mapsJsonData = json.loads(mapsData)
	
	processMaps(mapsJsonData)
	
def processMaps(data):
	time = data["routes"][0]["legs"][0]["duration"]["text"]
	duration = time.split()[0]
	units = time.split()[1]
	route = data["routes"][0]["summary"]
	
	displayMaps(duration, units, route)
	
def displayMaps(duration, units, route):
	# screen = PapirusTextPos([rotation = rot])
	# screen.AddText(duration, 190, 98, Id="duration")
	# screen.AddText(units, 230, 108, Id="units")
	# screen.AddText(route, 190, 148, Id="route")
	
	s = duration + " " + units + "\n" + route
	print s

	
requestWeather()
requestMaps()



# weather icons: http://weathericons.io/ 