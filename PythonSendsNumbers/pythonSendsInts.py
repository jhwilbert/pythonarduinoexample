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
time.sleep(1)
if ser.isOpen():
	print "Serial is open..."

	for i in range(255):
	    ser.write(bytes([i]))
	    print i
	    time.sleep(0.1)
	
	for i in range(255):
	    ser.write(bytes([255-i])) 
	    print i
	    time.sleep(0.1)    
	    
ser.close()
