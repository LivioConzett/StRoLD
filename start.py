#test to start script in python

import midi_to_sound
import time

while True:
	if midi_to_sound.midi() == 0:
		time.sleep(1)
	else:
		break
