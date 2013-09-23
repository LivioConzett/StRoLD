#midi for raspberry pi

import libnodave
print "imported libnodave"

dave = libnodave.Libnodave()
print "initiolized class libnodave()"
dave.eth_connection("192.168.22.222")
dave.write_marker_byte(39,1)



def write(d,state):                      #write out the note
	if d == '0x2e':
		print "b0", state
		dave.write_marker_byte(2,state)
	elif d == '0x2f':
		print "H0", state
		dave.write_marker_byte(3,state)
	elif d == '0x30':
		print "C1", state
		dave.write_marker_byte(4,state)
	elif d == '0x31':
		print "Cis1", state
		dave.write_marker_byte(5,state)
	elif d == '0x32':
		print "D1", state
		dave.write_marker_byte(6,state)
	elif d == '0x33':
		print "Dis1", state
		dave.write_marker_byte(7,state)
	elif d == '0x34':
		print "E1", state
		dave.write_marker_byte(8,state)
	elif d == '0x35':
		print "F1", state
		dave.write_marker_byte(9,state)
	elif d == '0x36':
		print "Fis1", state
		dave.write_marker_byte(10,state)
	elif d == '0x37':
		print "G1", state
		dave.write_marker_byte(11,state)
	elif d == '0x38':
		print "Gis1", state
		dave.write_marker_byte(12,state)
	elif d == '0x39':
		print "A1", state
		dave.write_marker_byte(13,state)
	elif d== '0x3a':
		print "b1", state
		dave.write_marker_byte(14,state)
	elif d == '0x3b':
		print "H1", state
		dave.write_marker_byte(15,state)
	elif d== '0x3c':
		print "C2", state
		dave.write_marker_byte(16,state)
	elif d == '0x3d':
		print "Cis2", state
		dave.write_marker_byte(17,state)
	elif d == '0x3e':
		print "D2", state
		dave.write_marker_byte(18,state)
	elif d == '0x3f':
		print "Dis2", state
		dave.write_marker_byte(19,state)
	elif d == '0x40':
		print "E2", state
		dave.write_marker_byte(20,state)
	elif d == '0x41':
		print "F2", state
		dave.write_marker_byte(21,state)
	elif d == '0x42':
		print "Fis2", state
		dave.write_marker_byte(22,state)
	elif d == '0x43':
		print "G2", state
		dave.write_marker_byte(23,state)
	elif d == '0x44':
		print "Gis2", state
		dave.write_marker_byte(24,state)
	elif d == '0x45':
		print "A2", state
		dave.write_marker_byte(25,state)
	elif d == '0x46':
		print "b2", state
		dave.write_marker_byte(26,state)
	elif d == '0x47':
		print "H2", state
		dave.write_marker_byte(27,state)
	elif d == '0x48':
		print "C3", state
		dave.write_marker_byte(28,state)
	elif d == '0x49':
		print "Cis3", state
		dave.write_marker_byte(29,state)
	elif d == '0x4a':
		print "D3", state
		dave.write_marker_byte(30,state)
	elif d == '0x4b':
		print "Dis3", state
		dave.write_marker_byte(31,state)
	elif d == '0x4c':
		print "E3", state
		dave.write_marker_byte(32,state)
	elif d == '0x4d':
		print "F3", state
		dave.write_marker_byte(33,state)
	elif d == '0x4e':
		print "Fis3", state
		dave.write_marker_byte(34,state)
	elif d == '0x4f':
		print "G3", state
		dave.write_marker_byte(35,state)
	elif d == '0x50':
		print "Gis3", state
		dave.write_marker_byte(36,state)
	elif d == '0x51':
		print "A3", state
		dave.write_marker_byte(37,state)
	elif d == '0x24':
		dave.eth_connection("192.168.22.222")
		dave.write_marker_byte(39,1)
	elif d == '0x25':
		dave.write_marker_byte(39,0)
		dave.disconnect()
	elif d == '0x26':
		dave.start_PLC()
	elif d == '0x27':
		dave.stop_PLC()
	elif d == '0x28':
		dave.write_marker_byte(40,1)
		print "drops off"
	elif d == '0x29':
		dave.write_marker_byte(40,0)
		print "drops on"
	elif d == '0x54':
		dave.write_marker_byte(39,0)
		dave.disconnect()
		return 2
	else:
		pass




def midi():
	f = open('/dev/snd/midiC1D0')	
	
	while True:
		try:	
			b = f.read(3)
			c = list(b)
		
			one = hex(ord(c[0]))
			two = hex(ord(c[1]))
	
			if one == '0x90':
				state = 1
			else:
				state = 0
                	if write(two,state) == 2:
				f.closed
                        	return 2
		except IOError:
			print "no file"
			return 1


