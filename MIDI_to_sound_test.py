#midi to sound
#Livio Conzett
#Requires: this example was run in Python 2.7 with pygame 1.9.2 installed.

import pygame
import pygame.midi


pygame.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.midi.init()
i = pygame.midi.Input(1)
mo = pygame.midi.Output(3, 0)
mo.set_instrument(0)


while True:
    if i.poll():                      #is something coming from the port?
        sound = i.read(10)            #save the incoming msg to sound
        d = sound[0][0]               #out nest the sound list
        if d[1] == 84 and d[2] > 110: # if the key C4 is pressed hard enough, exit the loop
            break
        if d[0] == 144:	              #if the first byte from the msg is 144 the sound is on
            mo.note_on(d[1],d[2])     #play sound (note,volume)
        else:                         #if first byte not 144 then sound off
            mo.note_off(d[1],127)

pygame.midi.quit()
