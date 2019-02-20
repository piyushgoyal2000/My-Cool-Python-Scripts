import json

import requests

ip = requests.get('https://api.ipify.org').text
ipreq = requests.get('http://api.ipstack.com/' + ip + '?access_key=')  # for access key visit:-https://ipstack.com
ipdetails = json.loads(ipreq.content.decode('utf-8'))
lat = ipdetails['latitude']
long = ipdetails['longitude']
print('IP: ' + ipdetails['ip'])
print('IP type: ' + ipdetails['type'])
print('City: ' + ipdetails['city'])
print('Pincode/Zipcode: ' + ipdetails['zip'])
print('State: ' + ipdetails['region_name'])
print('Country: ' + ipdetails['country_name'])
print('Capital of ' + ipdetails['country_name'] + ': ' + ipdetails['location']['capital'])
print('Continent:' + ipdetails['continent_name'])
print('Latitude: {}'.format(lat))
print('Longitude: {}'.format(long))
print('Mobile Code:' + ipdetails['location']['calling_code'])
