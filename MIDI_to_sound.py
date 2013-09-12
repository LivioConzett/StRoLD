#midi to sound
#Livio Conzett
#Requires: this example was run in Python 2.7 with pygame 1.9.2 installed on Windows XP.

import pygame
import pygame.midi
import time
	
	
def write(d,state):                      #write out the note
	if d == 46:
		print "b0", state
	elif d == 47:
		print "H0", state
	elif d == 48:
		print "C1", state
	elif d == 49:
		print "Cis1", state
	elif d == 50:
		print "D1", state
	elif d == 51:
		print "Dis1", state
	elif d == 52:
		print "E1", state
	elif d == 53:
		print "F1", state
	elif d == 54:
		print "Fis1", state
	elif d == 55:
		print "G1", state
	elif d == 56:
		print "Gis1", state
	elif d == 57:
		print "A1", state
	elif d== 58:
		print "b1", state
	elif d == 59:
		print "H1", state
	elif d== 60:
		print "C2", state
	elif d == 61:
		print "Cis2", state
	elif d == 62:
		print "D2", state
	elif d == 63:
		print "Dis2", state
	elif d == 64:
		print "E2", state
	elif d == 65:
		print "F2", state
	elif d == 66:
		print "Fis2", state
	elif d == 67:
		print "G2", state
	elif d == 68:
		print "Gis2", state
	elif d == 69:
		print "A2", state
	elif d == 70:
		print "b2", state
	elif d == 71:
		print "H2", state
	elif d == 72:
		print "C3", state
	elif d == 73:
		print "Cis3", state
	elif d == 74:
		print "D3", state
	elif d == 75:
		print "Dis3", state
	elif d == 76:
		print "E3", state
	elif d == 77:
		print "F3", state
	elif d == 78:
		print "Fis3", state
	elif d == 79:
		print "G3", state
	elif d == 80:
		print "Gis3", state
	elif d == 81:
		print "A3", state
	elif d == 36:
		print " "


def midi():                              #play the note
	pygame.init()
	pygame.midi.init()

	"""
	pygame.fastevent.init()
	event_get = pygame.fastevent.get
	event_post = pygame.fastevent.post
	"""

	port = pygame.midi.get_default_input_id()

	if port == -1:                       #if the default input is -1 (no device) quit script
		pygame.midi.quit()
		pygame.quit()
		return 0
		
		
	i = pygame.midi.Input(port)
	mo = pygame.midi.Output(3, 0)
	mo.set_instrument(0)
	t1 = time.time()
	
	
	while True:
		if i.poll():                      #is something coming from the port?
			t1 = time.time()              #save time to t1 calc the time between poll & no poll
			sound = i.read(10)            #save the incoming msg to sound
			d = sound[0][0]               #out nest the sound list
			#print d
			
			if d[1] == 84 and d[2] > 110: # if the key C4 is pressed hard enough, exit the loop
				break
				
			if d[0] >= 144:	              #if the first byte from the msg greater than 144 the sound is on
				mo.note_on(d[1],d[2])     #play sound (note,volume)
				#print d[1]
				state = 1
			else:                         #if first byte not greater then 144 then sound off
				mo.note_off(d[1],127)
				state = 0
				
			write(d[1],state)             #write out the note
			
		elif time.time() - t1 > 5:        #if there is no signal for 3 s stop the program
			pygame.midi.quit()
			pygame.quit()
			return 0
			
			
			
	i.close()
	pygame.midi.quit()
	pygame.quit()
	return 1
