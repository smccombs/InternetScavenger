import socket, threading, sys, time, urllib, re

FileCounter = 0
FileName = "Log" + str(FileCounter) + ".csv"
Logs = open(FileName,"w")

def main(tid, increment):
	logwrite = ''
	
	host1 = 185
	host2 = 127
	host3 = 47
	host4 = 0 + tid

	port = 80
	
	while 1 == 1:
		host4 += increment
		
		if host4 >= 256:
			host4 = host4 - 255
			host3 += 1
			if host3 >= 256:
				host3 = host3 - 255
				host2 += 1
				if host2 >= 256:
					host2 = host2 - 255
					host1 += 1
					if host1 >= 256:
						Logs.close()
						break
		
		host = str(host1) + '.' + str(host2) + '.' + str(host3) + '.' + str(host4)
		
		socket.setdefaulttimeout(1)
		connectionsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		try:
			connectionsocket.connect((host, int(port)))
			connectionsocket.close()
			sys.stdout.write('X')
			export = iplocate(host)
			print export
			logwrite = time.strftime("%Y-%m-%d %H:%M:%S") + ',' + host + ',' + export + ';\r'
		except:
			sys.stdout.write('.')
			
		Logs.write(logwrite)
		
	return
	
def iplocate(host):

	url = 'https://geoiptool.com/en/?ip='

	content = urllib.urlopen(url+host).read()
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
	
	export = Hostname + ',' + Country + ',' + Region + ',' + City + ',' + PostalCode + ',' + Latitude + ',' + Longitude
	
	return export
	
threads = []
increment = 255
for i in range(increment):
    t = threading.Thread(target=main, args=(i,increment))
    threads.append(t)
    t.start()