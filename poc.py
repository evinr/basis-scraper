import serial


def setup():
	ser = serial.Serial('/dev/ttyUSB0', timeout=2)
	ser.setRTS(True)
	ser.setRTS(False)
	if ser.isOpen():
    	ser.close()
	ser.open()
	ser.isOpen()
	print "USB connection established"

def read():
    rawString = ser.readline()
    print rawString
    return (str(rawString))

def write(stringVariable):
	ser.write(stringVariable.encode())

def handshake():
	write('AA 02 00 00 04 06 0A 00 AB')
	#Expect
	#01 60 AA 07 00 00 04 07 02 3D 02 03 02 51 00 AB
	
	write('AA 02 00 00 05 06 0B 00 AB')
	#Expect
	#01 60 AA 0B 00 00 05 07 02 1A 0D A0 66 00 00 00 00 3B 01 AB
	
	write('AA 02 00 00 0A 06 10 00 AB')
	#Expect
	#01 60 AA 0F 00 00 0A 07 02 30 30 30 34 33 65 30 32 65 64 64 65 63 03 AB
	
	write('AA 02 00 00 09 06 0F 00 AB')
	#should return with a different value, 
	#This is assumed to be the manifest of what data is currently contained on the device
	#TODO: Determine what this string is and how it is used 


def chilling():
	isChilling = read()
	if isChilling == '01 60 AA 07 00 00 00 03 01 3D 02 06 00 49 00 AB':
		print "device is ready for data transfer"

#TODO: define the gathering of all of the possible data sets being extracted
#Biometrics
	# Heart Rate
	# STEPS
	# CALORIES
	# SKIN TEMP
	# PERSPIRATION

#Activity
	# Walking
	# Running
	# Biking

#Sleep
	# REM
	# Mind Refresh
	# Light
	# Deep
	# Body Refresh
	# Interruptions
	# Toss & Turn
	