'''

ScreenScraper.py 8.8.8.8

Hostname: google-public-dns-a.google.com
Country: UnitedStates
Region: California
City: MountainView
PostalCode: 94040
Latitude: 37.386
Longitude: -122.0838

'''

import urllib, re, sys

ip = sys.argv[1]
url = 'https://geoiptool.com/en/?ip='

content = urllib.urlopen(url+ip).read()
content = content.replace('\n', '')
content = content.replace(' ', '')
content = content.replace('	', '')
content = content.replace('<', '>')
content = content.split(">")

x = content.index("Hostname:")
Hostname = content[x+6]
x = content.index("Country:")
Country = content[x+6]
x = content.index("Region:")
Region = content[x+4]
x = content.index("City:")
City = content[x+4]
x = content.index("PostalCode:")
PostalCode = content[x+4]
x = content.index("Latitude:")
Latitude = content[x+4]
x = content.index("Longitude:")
Longitude = content[x+4]

print "Hostname: " + Hostname
print "Country: " + Country
print "Region: " + Region
print "City: " + City
print "PostalCode: " + PostalCode
print "Latitude: " + Latitude
print "Longitude: " + Longitude