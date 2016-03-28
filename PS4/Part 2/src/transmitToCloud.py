import serial
import time
import requests
import json


s = None
value = ''

def setup():
 global s
 # Internal Communication with Arduino
 s = serial.Serial("/dev/ttyS0", 57600)

def loop():
	global value
	c=s.read()
 #print "post read"
	print c
	if c == '*':
#		print "Got Value ",value
		valArray = value.split(' ')
		data = {'temperature' : valArray[0], 'humidity': valArray[1], 'heatindex' : valArray[2] }
#		print data
		data_json = json.dumps(data) # Converts to JSON
		headers = {'Content-type': 'application/json'} # Specifies Headers for Post Request
		url = 'https://wireless-ps-4.appspot.com/sign' # Endpoint URL

		# Send data to rest endpoint at Google App Engine
		response = requests.post(url, data=data)
		if response.status_code != 200:
			print "Aww! Something went wrong"
		value = ''
	else:
		# print "got value ",c
		value = value + c

if __name__ == '__main__':
	setup()
	while True:
		loop()



