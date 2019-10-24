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
        
        # Reading One Sensor Values
		inByte = ser.read(2); # reads two bytes
		values = struct.unpack('>H', inByte) #unpacks them into ints
		first_value = values[0] # read first int from tuple
		print(first_value)
		

        # Reading Two Sensor Values
		inByte = ser.read(4); # reads four bytes
		values = struct.unpack('>HH', inByte) #unpacks them into ints
		first_value = values[0] # read first int from tuple
		second_value = values[1] # read second int from tuple
		
		print(first_value,second_value)

ser.close()  		
