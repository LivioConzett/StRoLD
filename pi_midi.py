#midi for raspberry pi



def write(d,state):                      #write out the note
	if d == '0x2e':
		print "b0", state
	elif d == '0x2f':
		print "H0", state
	elif d == '0x30':
		print "C1", state
	elif d == '0x31':
		print "Cis1", state
	elif d == '0x32':
		print "D1", state
	elif d == '0x33':
		print "Dis1", state
	elif d == '0x34':
		print "E1", state
	elif d == '0x35':
		print "F1", state
	elif d == '0x36':
		print "Fis1", state
	elif d == '0x37':
		print "G1", state
	elif d == '0x38':
		print "Gis1", state
	elif d == '0x39':
		print "A1", state
	elif d== '0x3a':
		print "b1", state
	elif d == '0x3b':
		print "H1", state
	elif d== '0x3c':
		print "C2", state
	elif d == '0x3d':
		print "Cis2", state
	elif d == '0x3e':
		print "D2", state
	elif d == '0x3f':
		print "Dis2", state
	elif d == '0x40':
		print "E2", state
	elif d == '0x41':
		print "F2", state
	elif d == '0x42':
		print "Fis2", state
	elif d == '0x43':
		print "G2", state
	elif d == '0x44':
		print "Gis2", state
	elif d == '0x45':
		print "A2", state
	elif d == '0x46':
		print "b2", state
	elif d == '0x47':
		print "H2", state
	elif d == '0x48':
		print "C3", state
	elif d == '0x49':
		print "Cis3", state
	elif d == '0x4a':
		print "D3", state
	elif d == '0x4b':
		print "Dis3", state
	elif d == '0x4c':
		print "E3", state
	elif d == '0x4d':
		print "F3", state
	elif d == '0x4e':
		print "Fis3", state
	elif d == '0x4f':
		print "G3", state
	elif d == '0x50':
		print "Gis3", state
	elif d == '0x51':
		print "A3", state
	elif d == '0x24':
		print " "
	elif d == '0x54':
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
                        	return 2
		except IOError:
			print "no file"
			return 1
	f.closed
        return 1



def main():
       midi()



if __name__ == '__main__': main()
