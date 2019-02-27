#Name-Amandeep Kaur

def find_req(json,n=0,t='03:00:00'):
		"""takes in json,n(0 by default) and t('03:00:00' by default)
		json is the response of the weather query,n is the number of days from the current day for which info is required and t is time of that day.
		the find_req function:
		1)converts the json into a string.
		2)returns the date and time in required format i.e. 2018-09-09 03:00:00
		3)slices the json string to end at the date time. """
	

	c=str(json)                    #stores json string in c

	if len(t)==4: 
		t='0'+t+':00'
	elif len(t)==5:
		t=t+':00'
	elif len(t)==7:
		t='0'+t                    #stores formatted time in t

	from datetime import date,timedelta
	req=str(date.today()+timedelta(days=n))+' '+t             #stores formatted date and time in variable name req
	c=c[:c.find(req)]                                         #slices json string from index 0 to req and stores in c
	return c                                                  #returns required part of the json string

def weather_response(location, API_key="2ab136be1543b5789451a5994364c0d3"):
	"""takes in location name and api key(optional) and returns the response of weather query in string format"""
	import urllib.request as url
	resp=url.urlopen("http://api.openweathermap.org/data/2.5/forecast?q="+location+"&APPID="+API_key)
	json =str(resp.read())[2:-1]
	return json	

def has_error(location,json):
	"""matches location name entered by user to the one returned in the weather query's response.
	Returns True if error is detected,False if entries match.""" 
	b=str(json) 
	loc=b[b.find("name")+7:b.find(",",b.find("name"))-1] #slices the piece of the json string where location name is mentioned and stores it under the variable name 'loc'"""
	if location.lower()!=loc:
		return True
	else:
		return False

def get_temperature (json, n=0,t="03:00:00"):
	"""extracts value of temperature from the response"""
	r=find_req(json,n,t)	
	temp=r[r.rfind('"temp":')+7:r.find(",",r.rfind('"temp":')+7)]
	return float(temp)

def get_humidity(json, n=0,t="03:00:00"):
	"""extracts value of humidity from the response"""
	r=find_req(json,n,t)
	humidity=r[r.rfind('humidity')+10:r.find(",",r.rfind('humidity')+10)]
	return float(humidity)

def get_pressure(json, n=0,t="03:00:00"):
	"""extracts value of temperature from the response"""
	r=find_req(json,n,t)
	pressure=r[r.rfind('pressure')+10:r.find(",",r.rfind('pressure')+10)]
	return float(pressure)

def get_wind(json, n=0,t="03:00:00"):
	"""extracts value of temperature from the response"""
	r=find_req(json,n,t)
	wind=r[r.rfind('wind')+15:r.find(",",r.rfind('wind')+15)]
	return float(wind)

def get_sealevel(json, n=0,t="03:00:00"):
	"""extracts value of temperature from the response"""
	r=find_req(json,n,t)
	sealevel=r[r.rfind('sea_level')+11:r.find(",",r.rfind('sea_level')+11)-1]
	return float(sealevel)




