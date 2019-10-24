import serial
import time
import struct


ser = serial.Serial(
		port='/dev/tty.usbmodem146101',
		baudrate=57600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
)
# Send the hello world as a string and wait for one second

if ser.isOpen():
	while(True):
		print("HELLO")
		ser.write(str('HELLO\n').encode('UTF-8'))
		time.sleep(1)

		print("WORLD")
		ser.write(str('WORLD\n').encode('UTF-8'))
	  	time.sleep(1)
ser.close()
