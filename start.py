#start the programm



import pi_midi

print "running"

while True:
	try:
		if pi_midi.midi() == 2:
			break
	except IOError:
		pass

