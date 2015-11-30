import socket
import threading
import sys
import time

Logs = open("log.csv","w")

def main(tid, increment):

	host1 = 173
	host2 = 194
	host3 = 219
	host4 = 0 + tid

	port = 80
	Counter = 0
	TotalCounter1 = 0
	TotalCounter2 = 0
	
	while 1 == 1:
		TotalCounter2 += 1
		host4 += increment
		sys.stdout.write('.')
		
		if host4 >= 256:
			TotalCounter1 = TotalCounter1 + Counter
			'''
			print ''
			print str(TotalCounter2) + ' : ' + str(Counter) + ' : ' + str(TotalCounter1)
			'''
			Counter = 0
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
		
		host = str(host1)+'.'+str(host2)+'.'+str(host3)+'.'+str(host4)
		
		socket.gethostbyname(host)
		'''socket.setdefaulttimeout(0.04)'''
		socket.setdefaulttimeout(1)
		connectionsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		try:
			connectionsocket.connect((host, int(port)))
			x = str(socket.gethostbyaddr(host))
			reply = time.strftime("%Y-%m-%d %H:%M:%S") + "," +str(socket.gethostbyname(host)) + "," + x[x.find("'")+1:x.find(",")-1]
			connectionsocket.close()
			sys.stdout.write('X')
			Logs.write(reply + "\r")
			Counter += 1
		except:
			reply = "--" + str(socket.gethostbyname(host))
		
		'''print reply'''
	return
	
threads = []
increment = 255
for i in range(increment):
    t = threading.Thread(target=main, args=(i,increment))
    threads.append(t)
    t.start()