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
    #RxTx
ser.isOpen()

# Check if there are any waiting bytes on buffer and flush them
print(ser.inWaiting())
ser.flushInput()
print(ser.inWaiting())


time.sleep(1)

while True:
    if (ser.inWaiting() >= 0): # wait for any bits ccomint
        
       print ser.readline();

ser.close()  		
