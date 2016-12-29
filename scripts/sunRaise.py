import serial
import RPi.GPIO

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
#ser.open()

ser.write("H")
try:
	while 1:
		respone = ser.readline()
		print respone
except KeyboardInterrupt:
	ser.close()

