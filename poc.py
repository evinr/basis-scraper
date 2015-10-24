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
	#This is assumed to be the manifest of data, ie what is currently contained on the device
		#When no data is present, ie the watch has just been sitting there. Expect
		#01 60 AA 05 00 00 09 07 02 1C 0B 39 00 AB
	#TODO: Determine what this string is and how it is used 

	#this is based on quick and constant syncs, verify as normal behavior
	write('AA 02 00 00 07 06 0D 00 AB')
#Same A
	#Assumed to be tied to the 'firmware update', as when that gets pushed the contents of this change in the same spot.
	# Three char sets change on these over the course of the contant syncs
	# Lots of padding on this one
	#TODO: Determine what this string is and how it is used 

	write('AA 23 00 00 05 04 00 52 BC 52 B9 3C 09 12 1B 64 12 CD 9B FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 5E 18 AB')
	#TODO: Determine if this string is consistant
	#Expect
	#01 60 AA 03 00 00 05 05 01 0B 00 AB

	write('AA 02 00 00 06 04 0A 00 AB')
	#Expect
	#01 60 AA 03 00 00 06 05 01 0C 00 AB

	write('AA 02 00 00 07 06 0D 00 AB')
#Same A	

	write('AA 08 00 00 04 04 1F 01 AC 2A 00 03 03 D8 00 AB')
	#expect
	#01 60 AA 03 00 00 04 05 01 0A 00 AB

# Current time gets sent here
#dynamic
# TODO: Determine how to send specific date times
	write('AA 08 00 00 00 04 45 9B 05 09 5C FE 4C 02 AB') #201510181406
	#expect
	#01 60 AA 03 00 00 00 05 01 06 00 AB

	write('AA 07 00 00 0C 04 00 10 27 00 00 47 00 AB')
	#expect
	#01 60 AA 03 00 00 0C 05 01 12 00 AB

	write('AA 02 00 00 10 04 14 00 AB')
	#expect
	#01 60 AA 03 00 00 10 05 01 16 00 AB

	write('AA 02 00 00 01 06 07 00 AB')
	#Expect
	#01 60 AA 07 00 00 01 07 02 7E 0B 00 00 93 00 AB	
	#01 60 AA 07 00 00 01 07 02 0A 00 00 00 14 00 AB	
	#01 60 AA 07 00 00 01 07 02 14 00 00 00 1E 00 AB	
	#01 60 AA 07 00 00 01 07 02 0A 00 00 00 14 00 AB	
	#01 60 AA 07 00 00 01 07 02 0A 00 00 00 14 00 AB	
	#01 60 AA 07 00 00 01 07 02 0A 00 00 00 14 00 AB	
	#01 60 AA 07 00 00 01 07 02 0A 00 00 00 14 00 AB																			
	
	write('AA 02 00 00 02 06 08 00 AB')
	#expect
	#01 60 AA 05 00 00 02 07 02 01 00 0C 00 AB

	write('AA 04 00 00 03 06 00 00 09 00 AB')
	#expect 
#real data here, with what appears to be aggregates in the header

	write('AA 02 00 00 01 04 05 00 AB')
	#expect
	#01 60 AA 03 00 00 01 05 01 07 00 AB

	write('')


def chilling():
	isChilling = read()
	if isChilling == '01 60 AA 07 00 00 00 03 01 3D 02 06 00 49 00 AB':
		print "device is ready for data transfer"

def deletingData():
	write('AA 02 00 00 08 06 0E 00 AB')
	print "are we done transfering data?"

	isDeletingData = read()

	if isDeletingData == '01 60 AA 04 00 00 08 07 02 01 12 00 AB':
		print "device is still deleting data from memory"
	elif isDeletingData == '01 60 AA 04 00 00 08 07 02 00 11 00 AB':
		print "device is done deleting data from memory"
	else:
		print "something unexpected happened"
	#at this point steady chilling is what happens every so many seconds	

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
	