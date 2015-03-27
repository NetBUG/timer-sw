import requests
import wiringpi2
import time
import math

pinIn = 3
state = 0
t = 0

wiringpi2.wiringPiSetupGpio()
wiringpi2.pinMode(pinIn, 0)

try:
	while True:
		if wiringpi2.digitalRead(pinIn) == 1:
			if state == 0:
				state = 1
				t = time.time()
		else:
			if state == 1:
				state = 0
				delta = time.time() - t
				print("Delta: " + str(delta) + "!\n")
				secs = str(int(math.floor(delta)))
				msec = str(delta)[str(delta).find('.')+1:str(delta).find('.')+3]
				url = 'http://10.9.66.88:15327/exec?cmd=@'+secs+msec
				try:
					l = requests.get(url)
				except:
					pass

except KeyboardInterrupt:
	print ""
